import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO

# Set page config for better mobile experience
st.set_page_config(page_title="Event Agenda", page_icon="📅", layout="wide")

# Custom CSS to improve mobile layout and add animated background
st.markdown("""
<style>
    .reportview-container .main .block-container {
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .dataframe {
        font-size: 12px;
    }
    @media (max-width: 600px) {
        .dataframe {
            font-size: 10px;
        }
    }
    /* Animated background */
    body {
        background: linear-gradient(270deg, #f0f0f0, #e0e0e0);
        background-size: 400% 400%;
        animation: gradientAnimation 10s ease infinite;
    }
    @keyframes gradientAnimation {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    /* Floating shapes */
    .shape {
        position: fixed;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        animation: float 5s infinite;
    }
    .shape:nth-child(1) {
        width: 80px;
        height: 80px;
        left: 10%;
        animation-delay: 0s;
    }
    .shape:nth-child(2) {
        width: 50px;
        height: 50px;
        right: 20%;
        animation-delay: 1s;
    }
    .shape:nth-child(3) {
        width: 70px;
        height: 70px;
        left: 35%;
        bottom: 30%;
        animation-delay: 2s;
    }
    @keyframes float {
        0% {transform: translateY(0px);}
        50% {transform: translateY(-20px);}
        100% {transform: translateY(0px);}
    }
</style>
<div class="shape"></div>
<div class="shape"></div>
<div class="shape"></div>
""", unsafe_allow_html=True)

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

# Create two columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    # Add some interactivity
    st.subheader("Session Information")
    selected_session = st.selectbox("Select a session for more details:", df["Content"])
    
    # Display details for the selected session
    st.write("**Session Details**")
    session_info = df[df["Content"] == selected_session].iloc[0]
    st.write(f"Time: {session_info['Time']}")
    st.write(f"Speaker: {session_info['Speaker']}")
    
    # Add a description for each session (you can customize these)
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
