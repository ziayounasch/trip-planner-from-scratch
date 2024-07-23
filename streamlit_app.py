import streamlit as st
from main import TripCrew  # Import the ResearchCrew class from main.py
import datetime
import sys


st.title('🏖️ AI Trip Planner')



today = datetime.datetime.now().date()
next_year = today.year + 1
jan_16_next_year = datetime.date(next_year, 1, 10)

st.sidebar.image("Logo of AI Trip Planner Final.png")
with st.sidebar:
    st.header('Enter Your Trip Details')
    topic = "Create a 7-day travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips."
    origin = st.text_input("From where will you be traveling from?", placeholder="San Mateo, CA")
    cities = st.text_input("What are the cities and Country options you are interested in visiting?", placeholder="Bali, Indonesia")
    date_range = st.date_input(
                "Date range you are interested in traveling?",
                min_value=today,
                value=(today, jan_16_next_year + datetime.timedelta(days=6)),
                format="MM/DD/YYYY",
            )
    interests = st.text_input("What are some of your high level interests and hobbies?", placeholder="2 adults who love swimming, dancing, hiking, and eating")

if st.button('Generate Trip Plan'):
    with st.spinner("Processing... Please be Patient it will take up to 2-3 mins... As your Crew of AI Agents are working,,,"):
        if not topic or not origin or not cities or not date_range or not interests:
            st.error("Please fill all the fields on the left Sidebar.")
        else:
            #inputs = f"Research Topic: {topic}\nOrigin: {origin}\City: {cities}\date_range: {date_range}\nInterests: {interests}"
            # inputs = {topic, origin, cities, date_range, interests}
            research_crew = TripCrew(origin, cities, date_range, interests)
            result = research_crew.run()
            st.subheader("Here is you Trip Plan:")
            st.write(result)