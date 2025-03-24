import streamlit as st
import pandas as pd
import json

# Store GPS data in memory
if "gps_data" not in st.session_state:
    st.session_state.gps_data = []

# API Endpoint to Receive Data
def receive_gps_data():
    st.subheader("📡 GPS Data Receiver")
    
    gps_input = st.text_area("Paste GPS JSON data here:", height=150)
    
    if st.button("Submit GPS Data"):
        try:
            gps_json = json.loads(gps_input)  # Parse JSON
            st.session_state.gps_data.append(gps_json)  # Store in memory
            st.success("✅ GPS data received!")
        except json.JSONDecodeError:
            st.error("❌ Invalid JSON format!")

# Display GPS Data
def show_gps_data():
    st.subheader("📍 Live GPS Data")
    
    if st.session_state.gps_data:
        df = pd.DataFrame(st.session_state.gps_data)
        st.dataframe(df)

        # Show on Map
        st.map(df.rename(columns={"latitude": "lat", "longitude": "lon"}))
    else:
        st.warning("No GPS data received yet.")

# Run both functions
receive_gps_data()
show_gps_data()
