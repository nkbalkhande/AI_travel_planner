import os
import googlemaps
import streamlit as st
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain import hub

# Load environment variables
load_dotenv()
GOOGLE_API_Map = os.getenv("Gemini_map")
GENAI_API_KEY = os.getenv("Gemini_key")

# Initialize APIs
gmaps = googlemaps.Client(key=GOOGLE_API_Map)
llm = ChatGoogleGenerativeAI(
    google_api_key=GENAI_API_KEY, model="gemini-2.0-flash", temperature=0.7)

# Tool: Get top places for interest in a city


@tool
def get_places(query: str) -> str:
    """Get top 5 places based on a natural language query like 'beaches in Goa'."""
    try:
        results = gmaps.places(query)['results'][:5]
        return "\n".join([place['name'] for place in results])
    except Exception as e:
        return f"Error: {str(e)}"


tools = [get_places]

# Prompt Template for the Agent
prompt_template = hub.pull('hwchase17/react')

# Create the agent
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt_template
)

# Wrap with AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Streamlit UI
st.set_page_config(
    page_title="✈️ AI Travel Itinerary Planner", layout="centered")
st.title("✈️ AI Travel Itinerary Planner")

city = st.text_input("Enter Destination City:")
days = st.number_input("Number of Days:", min_value=1, max_value=30, step=1)
interests = st.text_area("Your Interests (e.g., beaches, museums, food):")

if st.button("Generate Itinerary"):
    if not city or not interests:
        st.error("Please provide both city and interests.")
    else:
        with st.spinner("Planning your perfect trip..."):
            try:
                full_input = (
                    f"Create a detailed {days}-day travel itinerary for {city}. "
                    f"My interests are: {interests}. "
                    "For each day, list 3–4 activities or places to visit including food recommendations, "
                    "local attractions, and the best time to visit them. "
                    "Organize it as:\n\nDay 1:\n- Morning:\n- Afternoon:\n- Evening:\n\nDay 2: ... "
                )

                response = agent_executor.invoke({"input": full_input})
                st.subheader("🗓️ Your Itinerary")
                # response_text = response['output'] if isinstance(
                #     response, dict) else str(response)
                st.markdown(response['output'])
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
