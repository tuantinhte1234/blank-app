import streamlit as st
import pandas as pd

# Set page title and favicon
st.set_page_config(page_title="Event Agenda", page_icon="📅")

# Title of the event
st.title("Problem-Solving Skills for Learning Challenges")

# Create a DataFrame for the agenda
data = {
    "Content": ["Welcome", "Introduction to Problem-Solving", "How to improve your problem-solving skills", "Mini game", "Group practice", "Conclusion and Q&A"],
    "Time": ["1:15 PM", "1:20 PM", "1:50 PM", "2:20 PM", "2:40 PM", "3:00 PM"],
    "Speaker": ["Ms. Hoa", "Ms. Hoa", "Ms. Hoa", "Ms. Hien", "Ms. Hien", "Ms. Hien"]
}

df = pd.DataFrame(data)

# Display the agenda as a table
st.subheader("Detailed Agenda")
st.table(df)

# Add some interactivity
st.sidebar.header("Session Information")
selected_session = st.sidebar.selectbox("Select a session for more details:", df["Content"])

# Display details for the selected session
st.sidebar.subheader("Session Details")
session_info = df[df["Content"] == selected_session].iloc[0]
st.sidebar.write(f"Time: {session_info['Time']}")
st.sidebar.write(f"Speaker: {session_info['Speaker']}")

# Add a description for each session (you can customize these)
descriptions = {
    "Welcome": "A warm welcome to all participants and brief overview of the event.",
    "Introduction to Problem-Solving": "An overview of problem-solving techniques and their importance in learning.",
    "How to improve your problem-solving skills": "Practical strategies and exercises to enhance problem-solving abilities.",
    "Mini game": "An interactive game to apply problem-solving skills in a fun way.",
    "Group practice": "Collaborative session where participants work together on problem-solving challenges.",
    "Conclusion and Q&A": "Wrap-up of key takeaways and opportunity for participants to ask questions."
}

st.sidebar.write("Description:", descriptions.get(selected_session, "No description available."))

# Footer
st.markdown("---")
st.write("We hope you enjoy the event! If you have any questions, please don't hesitate to ask.")
