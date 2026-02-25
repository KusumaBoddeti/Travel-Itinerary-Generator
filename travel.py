import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure Streamlit page
st.set_page_config(page_title="Travel Itinerary Generator")
st.title("🌍 Travel Itinerary Generator")

# Get API key securely from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Check if API key exists
if not api_key:
    st.error("❌ GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_itinerary(destination, days, nights):
    prompt = f"""
    Create a detailed travel itinerary for {destination}
    for {days} days and {nights} nights.

    Include:
    - Day-wise plan
    - Tourist attractions
    - Activities
    - Local food suggestions
    - Travel tips
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


# User Inputs
destination = st.text_input("Enter Destination")
days = st.number_input("Number of Days", min_value=1, step=1)
nights = st.number_input("Number of Nights", min_value=1, step=1)

# Button Action
if st.button("Generate Itinerary"):
    if destination:
        with st.spinner("Generating your itinerary... ✈️"):
            result = generate_itinerary(destination, days, nights)
            st.write(result)
    else:
        st.warning("⚠ Please enter a destination.")