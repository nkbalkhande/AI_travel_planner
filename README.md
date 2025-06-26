# ✈️ AI Travel Itinerary Planner

This Streamlit app helps you plan a multi-day travel itinerary based on your destination, duration, and interests using **Google Maps API** and **Gemini (Generative AI)** via LangChain.

---

## 🚀 Features

- 🌍 Get tailored travel plans for any city
- 🎯 Customize based on your interests (e.g., beaches, food, nature)
- 🗓️ Plan multi-day itineraries (up to 30 days)
- 📍 Real-time places from **Google Maps**
- 🧠 Powered by **Gemini AI** + LangChain Agents

---

## 🛠️ Tech Stack

- **LangChain** (ReAct Agent)
- **Gemini 2.0 Flash**
- **Google Maps API**
- **Streamlit** (UI)
- **Python + dotenv** (for secret management)

---

## 📦 Installation

```bash
git clone https://github.com/nkbalkhande/your_repo_name.git
cd your_repo_name
pip install -r requirements.txt
```
## 🔐 .env Format
```
Gemini_key=your_gemini_api_key
Gemini_map=your_google_maps_api_key

```

## 🤖 How It Works
  - Uses LangChain ReAct agent
 
  - Your natural query is passed to agent_executor

  - Tool get_places calls Google Maps API to find top places

  - Gemini LLM generates the itinerary with reasoning

##  ▶️ Run the App
```
streamlit run your_script_name.py
```

## ScreenShot
![image_alt](https://github.com/nkbalkhande/AI_travel_planner/blob/main/Screenshot%202025-06-26%20171655.png?raw=true)

![image_alt](https://github.com/nkbalkhande/AI_travel_planner/blob/main/Screenshot%202025-06-26%20171718.png?raw=true)

# requirements.txt
```
streamlit
langchain
langchain-core
langchain-google-genai
googlemaps
python-dotenv
```
