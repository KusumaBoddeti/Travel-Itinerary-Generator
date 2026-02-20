import streamlit as st
from google import genai

st.title("Travel Itinerary Generator")

client = genai.Client(api_key="AIzaSyBNwuTclwKJ3ty0_EDWQNSa2LXm3AkwLHo")

def generate_itinerary(destination, days, nights):
    prompt = f"""
    Create a detailed travel itinerary for {destination}
    for {days} days and {nights} nights.
    Include day-wise plan, activities and food.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

destination = st.text_input("Enter Destination")
days = st.number_input("Days", min_value=1)
nights = st.number_input("Nights", min_value=1)

if st.button("Generate"):
    if destination:
        st.write(generate_itinerary(destination, days, nights))
