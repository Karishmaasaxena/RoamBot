import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image
import requests
from io import BytesIO

# Load environment variables from .env file
load_dotenv()

# Access your API key
GEMINI_API = os.getenv('GOOGLE_API_KEY')

# Set up Google Gemini API key
GOOGLE_API_KEY = GEMINI_API
genai.configure(api_key=GOOGLE_API_KEY)

# Page configuration
st.set_page_config(
    page_title="ROMBOT - AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS to beautify the app with sea colors and improved text visibility
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Playfair+Display:wght@400;600;700&display=swap');
    
    /* Sea-colored background for the entire app */
    .stApp {
        background: linear-gradient(135deg, #0a5d7c 0%, #127899 50%, #1c93b8 100%);
    }
    
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 4rem !important;
        font-weight: 700;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.4rem;
        color: #e0f7fa;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: #003b55;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #3a8fb7;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 12px;
        padding: 1.8rem;
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        margin-bottom: 1.8rem;
    }
    .form-card {
        background-color: rgba(224, 247, 250, 0.9);
        border-radius: 12px;
        padding: 1.8rem;
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        margin-bottom: 1.8rem;
        border-left: 5px solid #003b55;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 1rem;
        font-size: 1rem;
        color: #e0f7fa;
        font-family: 'Montserrat', sans-serif;
    }
    .stButton>button {
        background-color: #003b55;
        color: white;
        font-weight: 600;
        font-family: 'Montserrat', sans-serif;
        border-radius: 6px;
        padding: 0.7rem 1.2rem;
        border: none;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #00546e;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Enhanced itinerary styling with improved text visibility */
    .itinerary-content {
        font-family: 'Montserrat', sans-serif;
        line-height: 1.8;
        font-size: 1.1rem;
        color: #003b55;
    }
    .itinerary-content h2 {
        font-family: 'Playfair Display', serif;
        color: #003b55;
        font-size: 2.2rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #3a8fb7;
        padding-bottom: 0.5rem;
    }
    .itinerary-content h3 {
        font-family: 'Playfair Display', serif;
        color: #003b55;
        font-size: 1.6rem;
        margin-top: 1.5rem;
        border-left: 4px solid #003b55;
        padding-left: 0.8rem;
        background-color: #cfe9f3;
        padding: 0.6rem 0.8rem;
        border-radius: 0 6px 6px 0;
    }
    .itinerary-content p {
        margin-bottom: 1rem;
        color: #00384d;
    }
    .itinerary-content strong {
        color: #003b55;
        font-weight: 700;
    }
    
    /* Improved highlighting elements with better text contrast */
    .highlight-spot {
        background-color: #b3e0f2;
        padding: 1.2rem;
        border-radius: 8px;
        margin: 1.2rem 0;
        border-left: 5px solid #0277bd;
        font-size: 1.1rem;
        color: #003b55;
        font-weight: 500;
    }
    .famous-spot {
        font-size: 1.2rem;
        color: #003b55;
        font-weight: 700;
        background-color: #ffd54f;
        padding: 0.3rem 0.6rem;
        border-radius: 4px;
        display: inline-block;
        margin: 0.2rem 0;
        border-bottom: 2px solid #ff9800;
    }
    .emoji-icon {
        font-size: 1.8rem;
        margin-right: 0.5rem;
        vertical-align: middle;
    }
    .tip-card {
        background-color: #c8e6c9;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #2e7d32;
        color: #1b5e20;
        font-weight: 500;
    }
    .food-item {
        color: #c62828;
        font-weight: 600;
        background-color: #ffebee;
        padding: 0.2rem 0.4rem;
        border-radius: 3px;
    }
    .day-divider {
        height: 3px;
        background: linear-gradient(90deg, #003b55 0%, #0277bd 50%, #4fc3f7 100%);
        margin: 2rem 0;
        border-radius: 3px;
    }
    
    /* Info boxes with improved contrast */
    .weather-info {
        background-color: #0277bd;
        color: white;
        padding: 0.5rem 0.8rem;
        border-radius: 6px;
        display: inline-block;
        margin-right: 0.5rem;
        font-weight: 500;
    }
    .cost-info {
        background-color: #2e7d32;
        color: white;
        padding: 0.5rem 0.8rem;
        border-radius: 6px;
        display: inline-block;
        font-weight: 500;
    }
    
    /* Style for labels and inputs */
    div.row-widget.stSelectbox label, div.row-widget.stSlider label, div.row-widget.stTextInput label {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: #003b55;
    }
    .stTextInput input {
        font-size: 1.1rem;
        padding: 0.7rem;
        border-radius: 6px;
        border: 2px solid #0277bd;
    }
    
    /* Note box styling for better visibility */
    .note-box {
        background-color: #4fc3f7;
        color: #003b55;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-weight: 500;
        border-left: 5px solid #0277bd;
    }
    
    /* Custom styles for streamlit components */
    .stSlider {
        padding-bottom: 1.5rem;
    }
    .stSelectbox {
        padding-bottom: 1.5rem;
    }
    
    /* Make dropdown text more visible */
    .stSelectbox div[data-baseweb="select"] {
        background-color: white;
    }
    .stMultiSelect div[data-baseweb="select"] {
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

# Function to get a destination image
def get_destination_image(destination):
    try:
        search_term = destination.replace(" ", "+")
        response = requests.get(f"https://source.unsplash.com/800x400/?{search_term},travel")
        return Image.open(BytesIO(response.content))
    except:
        return None

# Enhanced function to generate travel itinerary with better formatting
def generate_itinerary(destination, days, budget, purpose, interests):
    prompt = f"""
    Generate a detailed {days}-day travel itinerary for {destination}. 
    - Budget level: {budget} 
    - Purpose: {purpose} 
    - Interests: {', '.join(interests)}

    For each day include:
    - Morning, afternoon, and evening activities
    - Local food recommendations with estimated costs
    - Accommodation suggestions
    - Transportation details
    - Local tips and cultural insights
    
    IMPORTANT FORMATTING INSTRUCTIONS:
    1. Format the itinerary in Markdown with clear headings for each day and section.
    2. Use emoji icons generously for better visual appeal.
    3. Mark famous landmarks and must-visit destinations as <span class="famous-spot">Famous Landmark Name</span>
    4. Put essential travel tips in <div class="tip-card">Tip content goes here</div>
    5. Highlight any must-see attractions or special experiences using <div class="highlight-spot">Content here</div>
    6. Format food recommendations like: <span class="food-item">Dish Name</span> (~$XX)
    7. Use **bold text** for important information like meeting points, opening hours, etc.
    8. Format weather information as <span class="weather-info">🌤️ Weather info</span>
    9. Format cost estimates as <span class="cost-info">💰 Cost info</span>
    10. Add <div class="day-divider"></div> between days
    11. Conclude with a note in <div class="note-box">Note: This itinerary is a suggestion and can be customized based on your interests and the time of year. Festivals in [destination] can significantly alter the atmosphere and crowd levels, so plan accordingly.</div>

    Make the itinerary visually engaging and easy to scan with clear sections and highlights.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text if response else "No itinerary generated."
    except Exception as e:
        return f"Error generating itinerary: {str(e)}"

# Main app interface
def main():
    # App header
    st.markdown('<h1 class="main-title">🌍 ROMBOT</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Your AI Travel Companion for Extraordinary Adventures</p>', unsafe_allow_html=True)
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="section-header">📋 Plan Your Dream Trip</h3>', unsafe_allow_html=True)
        
        destination = st.text_input("📍 Destination", placeholder="Enter your travel destination")
        
        days = st.slider("📅 Trip Duration (days)", 1, 21, 5)
        
        budget_options = {
            "Low": "💰 Budget-friendly options",
            "Moderate": "💰💰 Mid-range expenses",
            "Luxury": "💰💰💰 Premium experiences"
        }
        budget = st.selectbox("Budget Level", options=list(budget_options.keys()), 
                             format_func=lambda x: budget_options[x])
        
        purpose_options = {
            "Adventure": "🧗‍♂️ Adventure & Exploration",
            "Relaxation": "🏖️ Relaxation & Wellness",
            "Work": "💼 Business & Networking",
            "Culture": "🏛️ Cultural Immersion",
            "Family": "👨‍👩‍👧‍👦 Family Vacation",
            "Solo": "🧳 Solo Travel Journey"
        }
        purpose = st.selectbox("Purpose of Travel", options=list(purpose_options.keys()),
                              format_func=lambda x: purpose_options[x])
        
        interest_options = ["Nature & Outdoors", "History & Heritage", "Local Cuisine", "Nightlife & Entertainment", 
                           "Shopping & Markets", "Art & Museums", "Music & Festivals", "Sports & Activities", 
                           "Photography Spots", "Architecture & Design", "Wellness & Spa", "Hidden Gems"]
        interests = st.multiselect("🎭 Interests", interest_options, 
                                  default=["Nature & Outdoors", "Local Cuisine"])
        
        generate_btn = st.button("✨ Generate My Itinerary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Travel tips section
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="section-header">💡 Travel Smart</h3>', unsafe_allow_html=True)
        tips = [
            "📱 Download offline maps before your trip",
            "💳 Notify your bank of your travel plans",
            "🔌 Bring a universal adapter for your electronics",
            "📷 Research photography spots in advance",
            "🗣️ Learn a few basic phrases in the local language",
            "🧳 Pack light and leave room for souvenirs",
            "🔒 Make copies of important documents",
            "💧 Always carry a reusable water bottle",
            "🧢 Pack for the weather and local customs",
            "💊 Prepare a basic travel medical kit"
        ]
        for tip in tips[:4]:
            st.markdown(f"<p style='font-size: 1.05rem; color: #003b55;'>{tip}</p>", unsafe_allow_html=True)
        with st.expander("More Travel Tips"):
            for tip in tips[4:]:
                st.markdown(f"<p style='font-size: 1.05rem; color: #003b55;'>{tip}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        if generate_btn:
            if not destination:
                st.error("⚠️ Please enter a destination!")
            else:
                # Get a nice image for the destination
                img = get_destination_image(destination)
                if img:
                    st.image(img, use_column_width=True, caption=f"✨ Your destination: {destination}")
                
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown(f'<h3 class="section-header">🗺️ Your Personalized {days}-Day {destination} Adventure</h3>', unsafe_allow_html=True)
                
                with st.spinner("🔮 Crafting your perfect travel experience..."):
                    itinerary = generate_itinerary(destination, days, budget, purpose, interests)
                
                # Display the itinerary with enhanced markdown formatting
                st.markdown(f'<div class="itinerary-content">{itinerary}</div>', unsafe_allow_html=True)
                
                # Download button with enhanced styling
                st.download_button(
                    label="📥 Download Your Itinerary",
                    data=itinerary,
                    file_name=f"{destination}_adventure_itinerary.md",
                    mime="text/markdown",
                )
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Welcome screen when no itinerary has been generated
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3 class="section-header">👋 Welcome to Your Travel Adventure!</h3>', unsafe_allow_html=True)
            st.markdown("""
            <p style="font-size: 1.2rem; line-height: 1.6; color: #003b55;">Discover the world with ROMBOT, your AI-powered travel companion that creates personalized itineraries tailored to your unique preferences and travel style.</p>
            
            <div style="background: linear-gradient(135deg, #b3e0f2 0%, #4fc3f7 100%); padding: 1.5rem; border-radius: 10px; margin: 1.5rem 0; border-left: 5px solid #0277bd;">
                <h4 style="font-family: 'Playfair Display', serif; color: #003b55; margin-bottom: 1rem; font-size: 1.4rem;">✨ How ROMBOT Works:</h4>
                <ol style="font-size: 1.1rem; padding-left: 1.5rem; color: #003b55;">
                    <li><strong>Enter your dream destination</strong></li>
                    <li><strong>Set your ideal trip duration</strong></li>
                    <li><strong>Select your budget level and travel purpose</strong></li>
                    <li><strong>Choose your interests and preferences</strong></li>
                    <li><strong>Get a beautifully crafted day-by-day itinerary</strong></li>
                </ol>
            </div>
            
            <p style="font-size: 1.1rem; color: #003b55;"><strong>Popular destinations to explore:</strong> Tokyo, Bali, Morocco, New York, Barcelona, Cape Town, Iceland, Thailand, Peru, New Zealand</p>
            """, unsafe_allow_html=True)
            
            # Show a sample image
            sample_img = get_destination_image("travel destinations")
            if sample_img:
                st.image(sample_img, use_column_width=True, caption="Where will your next adventure take you?")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.markdown("🚀 Powered by Gemini 1.5 Flash & Streamlit | © 2025 ROMBOT - Your AI Travel Companion", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()