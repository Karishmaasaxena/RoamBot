import streamlit as st
from datetime import datetime, timedelta


# Title and introduction
st.title("RoamBot – Smart AI for seamless travel itineraries")
st.write("Generate a customized travel itinerary based on your preferences")

# Sidebar for main trip parameters
with st.sidebar:
    st.header("Trip Details")
    destination = st.text_input("Destination", "Paris, France")
    
    # Date selection
    start_date = st.date_input("Start Date", datetime.now().date() + timedelta(days=30))
    duration = st.slider("Trip Duration (days)", min_value=1, max_value=14, value=3)
    end_date = start_date + timedelta(days=duration-1)
    
    # Trip preferences
    st.header("Preferences")
    budget = st.select_slider("Budget", options=["Budget", "Moderate", "Luxury"], value="Moderate")
    pace = st.select_slider("Pace", options=["Relaxed", "Balanced", "Intensive"], value="Balanced")
    interests = st.multiselect(
        "Interests",
        ["History & Culture", "Food & Dining", "Nature & Outdoors", "Shopping", "Art & Museums", "Nightlife"],
        ["History & Culture", "Food & Dining"]
    )

# Main content area
st.header(f"Your {duration}-day trip to {destination}")
st.write(f"**Dates:** {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}")
st.write(f"**Budget:** {budget} | **Pace:** {pace}")

# Generate itinerary when user clicks button
if st.button("Generate Itinerary"):
    with st.spinner("Creating your perfect itinerary..."):
        # In a real application, this would call an API or use AI to generate the itinerary
        # For now, we'll create a simple template-based itinerary
        
        # Sample activities based on interests
        activities = {
            "History & Culture": ["Visit local museums", "Explore historic sites", "Take a guided city tour"],
            "Food & Dining": ["Try local cuisine", "Food market tour", "Cooking class"],
            "Nature & Outdoors": ["Hike in nearby parks", "Visit gardens", "Boat tour"],
            "Shopping": ["Shopping at local markets", "Visit boutique stores", "Shopping district tour"],
            "Art & Museums": ["Art gallery visits", "Museum exhibitions", "Local artist workshops"],
            "Nightlife": ["Visit local bars", "Attend live music events", "Night city tour"]
        }
        
        # Sample destinations based on location
        paris_attractions = [
            "Eiffel Tower", "Louvre Museum", "Notre Dame Cathedral", 
            "Montmartre", "Champs-Élysées", "Seine River Cruise",
            "Versailles Palace", "Musée d'Orsay", "Luxembourg Gardens",
            "Sainte-Chapelle", "Centre Pompidou", "Sacré-Cœur Basilica"
        ]
        
        # Create daily itinerary
        for day in range(1, duration + 1):
            current_date = start_date + timedelta(days=day-1)
            st.subheader(f"Day {day}: {current_date.strftime('%A, %B %d')}")
            
            # Morning
            st.write("**Morning:**")
            if "History & Culture" in interests or "Art & Museums" in interests:
                attraction = paris_attractions[day % len(paris_attractions)]
                st.write(f"- Visit {attraction}")
            else:
                st.write(f"- Explore the {paris_attractions[day % len(paris_attractions)]} area")
            
            # Lunch
            st.write("**Lunch:**")
            if "Food & Dining" in interests:
                st.write("- Enjoy lunch at a local bistro")
            else:
                st.write("- Quick lunch at a café")
                
            # Afternoon
            st.write("**Afternoon:**")
            selected_interests = [interest for interest in interests if activities.get(interest)]
            if selected_interests:
                selected_activity = activities[selected_interests[day % len(selected_interests)]][day % 3]
                st.write(f"- {selected_activity}")
            else:
                st.write("- Free time to explore the city")
                
            # Evening
            st.write("**Evening:**")
            if "Food & Dining" in interests:
                st.write("- Dinner at a recommended restaurant")
            else:
                st.write("- Dinner at local eatery")
                
            if "Nightlife" in interests and pace != "Relaxed":
                st.write("- Evening entertainment")
                
            st.write("---")
            
    # Add accommodation and transportation recommendations
    st.header("Recommended Accommodations")
    accommodation_types = {"Budget": "Hostels or budget hotels", "Moderate": "3-star hotels", "Luxury": "4-5 star hotels"}
    st.write(f"Based on your **{budget}** preference: {accommodation_types[budget]} in central {destination.split(',')[0]}")
    
    st.header("Transportation Tips")
    st.write(f"Getting around {destination.split(',')[0]}:")
    st.write("- Public transportation: Metro, buses, and trams")
    st.write("- Walking is ideal for central areas")
    st.write("- Taxis and rideshare services are available")
    
    # Export options
    st.header("Export Options")
    st.write("Save your itinerary for your trip:")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Download as PDF")
    with col2:
        st.button("Email Itinerary")

# Footer
st.markdown("---")
st.markdown("*RoamBot creates personalized travel recommendations. Adjust your preferences and regenerate as needed.*")