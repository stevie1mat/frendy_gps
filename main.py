import streamlit as st
import pandas as pd
import json
import socket

# Function to get local IP address
def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return "Unable to determine IP"

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

# Get local IP
server_ip = get_local_ip()

# Display server details
st.sidebar.header("📡 Server Details")
st.sidebar.write(f"**Local Access:** [http://localhost:8501](http://localhost:8501)")
st.sidebar.write(f"**Network Access:** [http://{server_ip}:8501](http://{server_ip}:8501)")

# Run functions
receive_gps_data()
show_gps_data()
