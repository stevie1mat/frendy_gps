import streamlit as st
import requests
import pandas as pd

# Replace with your AWS Flask API URL
API_URL = "http://your-aws-ip:5000/gps/latest"

st.title("📍 Real-Time GPS Tracker")

# Fetch GPS Data from API
def fetch_gps_data():
    try:
        response = requests.get(API_URL, timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching GPS data: {e}")
    return None

# Display GPS Data
gps_data = fetch_gps_data()

if gps_data:
    st.write("**Latest GPS Data:**")
    st.json(gps_data)

    # Convert to DataFrame for visualization
    df = pd.DataFrame([gps_data])

    # Display table
    st.write("### Data Table")
    st.dataframe(df)

    # Show GPS Location on Map
    st.write("### Location on Map 🌍")
    st.map(pd.DataFrame({"lat": [gps_data["lat"]], "lon": [gps_data["lng"]]}))
else:
    st.warning("No GPS data available")

# Auto-refresh every 5 seconds
st.button("🔄 Refresh", on_click=lambda: st.experimental_rerun())
