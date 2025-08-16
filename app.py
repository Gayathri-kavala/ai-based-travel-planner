import streamlit as st
from datetime import date, timedelta
from ai_utils import generate_itinerary
from utils_visual import get_ai_image


st.set_page_config(page_title="🌍 Travel Itinerary Bot", layout="wide")
st.title("🌍 Travel Itinerary Bot")
st.write("Plan your perfect trip by entering your destination and travel dates!")

# --- Form
with st.form("trip_form"):
    destination = st.text_input("Destination (e.g., Tokyo, Paris)", "")
    start_date = st.date_input("Start Date", date.today())
    end_date = st.date_input("End Date", date.today() + timedelta(days=4))
    submitted = st.form_submit_button("Generate Itinerary")

# --- Handle Submission
if submitted:
    if destination and start_date < end_date:
        st.success(f"Generating plan for {destination} from {start_date} to {end_date}...")

        # Destination image
        st.markdown("## 🗺️ Destination Preview")
        hero_image = get_ai_image(destination)
        if hero_image:
            st.image(hero_image, caption=destination, use_container_width=True)
        else:
            st.caption("📷 No image found for this location.")

        # Itinerary generation
        plan = generate_itinerary(destination, start_date, end_date)

        st.markdown("## 🗓️ Your Day-by-Day Plan")
        st.markdown(plan)

    else:
        st.error("Please enter a valid destination and make sure the start date is before the end date.")
