RoamBot
Smart AI for Seamless Travel Itineraries
RoamBot is a Streamlit-based web application that helps travelers generate customized travel itineraries based on their preferences. The application simplifies trip planning by creating day-by-day schedules tailored to your destination, duration, budget, and personal interests.

Features:

Destination Selection: Choose any location around the world
Date & Duration Planning: Set your travel dates and trip length
Preference-Based Recommendations:

Budget level (Budget, Moderate, Luxury)
Travel pace (Relaxed, Balanced, Intensive)
Interest categories (History & Culture, Food & Dining, Nature & Outdoors, etc.)


Day-by-Day Itineraries: Morning, lunch, afternoon, and evening activities customized to your preferences
Accommodation & Transportation Tips: Recommendations based on your selected budget and destination
Export Options: Download as PDF or email your itinerary (functionality to be implemented)

Installation
Prerequisites

Python 3.7+
pip

Setup

Clone the repository:
git clone https://github.com/yourusername/roambot.git
cd roambot

Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required dependencies:
pip install -r requirements.txt


Requirements

streamlit
datetime

Usage

Start the application:
streamlit run app.py

Open your web browser and navigate to the provided local URL (typically http://localhost:8501)
Enter your trip details:

Destination
Start date
Trip duration
Budget preference
Pace preference
Activity interests


Click "Generate Itinerary" to create your personalized travel plan
Review your day-by-day schedule and recommendations
Use the export options to save or share your itinerary

Current Limitations

The current version uses template-based generation rather than true AI for itinerary creation
Destination-specific attractions are currently limited to Paris as a demo
Export functionality buttons are present but not yet implemented

Future Development

Integration with real AI models for more personalized itineraries
Expanded destination database with attractions and activities worldwide
Weather forecast integration for trip dates
Reservation links for recommended accommodations and activities
User accounts to save and manage multiple itineraries
Mobile app version

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Built with Streamlit
Inspired by the need for simplified travel planning