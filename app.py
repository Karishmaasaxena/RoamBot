import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API key
GEMINI_API = os.getenv('GOOGLE_API_KEY')

# Set up Google Gemini API key
GOOGLE_API_KEY = GEMINI_API
genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate travel itinerary
def generate_itinerary(destination, days, budget, purpose, interests):
    prompt = f"""
    Generate a detailed {days}-day travel itinerary for {destination}. 
    - Budget level: {budget} 
    - Purpose: {purpose} 
    - Interests: {', '.join(interests)}

    Include:
    - Morning, afternoon, and evening activities
    - Local food recommendations
    - Accommodation suggestions
    - Transportation details
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text if response else "No itinerary generated."

# Streamlit UI
st.title("🌍 ROMBOT – Smart AI for seamless travel itineraries")
st.write("Plan your next trip with AI-powered recommendations!")

destination = st.text_input("📍 Destination", placeholder="Enter your travel destination")
days = st.slider("📅 Trip Duration (days)", 1, 14, 5)
budget = st.selectbox("💰 Budget Level", ["Low", "Moderate", "Luxury"])
purpose = st.selectbox("🎯 Purpose of Travel", ["Adventure", "Relaxation", "Work", "Culture"])
interests = st.multiselect("🎭 Interests", ["Nature", "History", "Food", "Nightlife", "Shopping"])

if st.button("Generate Itinerary"):
    if destination:
        itinerary = generate_itinerary(destination, days, budget, purpose, interests)
        st.subheader("🗺️ Your AI-Powered Travel Itinerary:")
        st.write(itinerary)
    else:
        st.error("⚠️ Please enter a destination!")

st.markdown("---")
st.caption("🚀 Powered by Gemini 1.5 Flash & Streamlit")
