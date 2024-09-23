import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Event Agenda", page_icon="📅", layout="wide")

# Custom CSS
st.markdown("""
<style>
    body {
        background-color: #f0f8ff;  /* Light blue background */
    }
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 25%, #e6f3ff 25%, #e6f3ff 50%, #f0f8ff 50%, #f0f8ff 75%, #e6f3ff 75%, #e6f3ff 100%);
        background-size: 40px 40px;
        animation: move 4s linear infinite;
    }
    @keyframes move {
        0% {background-position: 0 0;}
        100% {background-position: 40px 40px;}
    }
    .css-18e3th9 {
        padding-top: 0;
    }
    .css-1d391kg {
        padding-top: 3.5rem;
    }
    .stTable {
        background-color: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("Problem-Solving Skills for Learning Challenges")

# Create DataFrame for agenda
data = {
    "Content": ["Welcome", "Introduction to Problem-Solving", "How to improve your problem-solving skills", "Mini game", "Group practice", "Conclusion and Q&A"],
    "Time": ["1:15 PM", "1:20 PM", "1:50 PM", "2:20 PM", "2:40 PM", "3:00 PM"],
    "Speaker": ["Ms. Hoa", "Ms. Hoa", "Ms. Hoa", "Ms. Hien", "Ms. Hien", "Ms. Hien"]
}
df = pd.DataFrame(data)

# Display agenda
st.subheader("Detailed Agenda")
st.table(df)

# Session information
st.subheader("Session Information")
selected_session = st.selectbox("Select a session for more details:", df["Content"])

# Display session details
st.write("**Session Details**")
session_info = df[df["Content"] == selected_session].iloc[0]
st.write(f"Time: {session_info['Time']}")
st.write(f"Speaker: {session_info['Speaker']}")

# Session descriptions
descriptions = {
    "Welcome": "A warm welcome to all participants and brief overview of the event.",
    "Introduction to Problem-Solving": "An overview of problem-solving techniques and their importance in learning.",
    "How to improve your problem-solving skills": "Practical strategies and exercises to enhance problem-solving abilities.",
    "Mini game": "An interactive game to apply problem-solving skills in a fun way.",
    "Group practice": "Collaborative session where participants work together on problem-solving challenges.",
    "Conclusion and Q&A": "Wrap-up of key takeaways and opportunity for participants to ask questions."
}
st.write("**Description:**", descriptions.get(selected_session, "No description available."))

# Footer
st.markdown("---")
st.write("We hope you enjoy the event! If you have any questions, please don't hesitate to ask.")
