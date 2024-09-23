import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Event Agenda", page_icon="📅", layout="wide")

# Custom CSS
st.markdown("""
<style>
    body {
        color: #2C3E50;
        background-color: #f0f8ff;
    }
    .stApp {
        background: linear-gradient(135deg, #e6f3ff 25%, #d9ecff 25%, #d9ecff 50%, #e6f3ff 50%, #e6f3ff 75%, #d9ecff 75%, #d9ecff 100%);
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
        background-color: #ffffff;
        color: #2C3E50;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .dataframe {
        background-color: #ffffff;
        color: #2C3E50;
    }
    .dataframe th {
        background-color: #3498DB;
        color: black; /* Đổi màu chữ thành đen */
    }
    .dataframe td {
        background-color: #ffffff;
        color: black; /* Đổi màu chữ thành đen */
    }
    h1, h2, h3 {
        color: #2C3E50;
    }
    .speaker {
        font-weight: bold;
        color: #3498DB;
    }
    .st-bw {
        color: #2C3E50;
    }
    .st-ew {
        color: #2C3E50;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>Problem-Solving Skills for Learning Challenges</h1>", unsafe_allow_html=True)



# Create DataFrame for agenda
data = {
    "Content": ["Welcome", "Introduction to Problem-Solving", "How to improve your problem-solving skills", "Mini game", "Group practice", "Conclusion and Q&A"],
    "Time": ["1:15 PM", "1:20 PM", "1:50 PM", "2:20 PM", "2:40 PM", "3:00 PM"],
    "Speaker": ["Ms. Hoa", "Ms. Hoa", "Ms. Hoa", "Ms. Hien", "Ms. Hien", "Ms. Hien"]
}
df = pd.DataFrame(data)

# Display agenda
st.subheader("Detailed Agenda")
st.table(df.style
          .set_properties(**{'background-color': 'white', 'color': 'black', 'text-align': 'center'})
          .set_table_attributes('style="border: 1px solid black;"')
          .set_table_styles([{
              'selector': 'th',
              'props': [('border', '1px solid black'), ('color', 'black'), ('text-align', 'center')]
          }, {
              'selector': 'td',
              'props': [('border', '1px solid black'), ('color', 'black'), ('text-align', 'center')]
          }]))

# Session information
st.subheader("Session Information")
st.markdown("<span style='color: black;'>Select a session for more details:</span>", unsafe_allow_html=True)
selected_session = st.selectbox("", df["Content"])

# Display session details
st.markdown("<div style='background-color: #ffffff; padding: 10px; border-radius: 5px;'>", unsafe_allow_html=True)
st.markdown("<span style='color: black;'>Session Details</span>", unsafe_allow_html=True)
session_info = df[df["Content"] == selected_session].iloc[0]

st.write("<span style='color: black;'>Time: {}</span>".format(session_info['Time']), unsafe_allow_html=True)
st.markdown(f"<span style='color: black;'>Speaker: <span class='speaker'>{session_info['Speaker']}</span></span>", unsafe_allow_html=True)

# Session descriptions
descriptions = {
    "Welcome": "A warm welcome to all participants and brief overview of the event.",
    "Introduction to Problem-Solving": "An overview of problem-solving techniques and their importance in learning.",
    "How to improve your problem-solving skills": "Practical strategies and exercises to enhance problem-solving abilities.",
    "Mini game": "An interactive game to apply problem-solving skills in a fun way.",
    "Group practice": "Collaborative session where participants work together on problem-solving challenges.",
    "Conclusion and Q&A": "Wrap-up of key takeaways and opportunity for participants to ask questions."
}
st.write("<span style='color: black;'>Description: {}</span>".format(descriptions.get(selected_session, "No description available.")), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='background-color: #ffffff; padding: 10px; border-radius: 5px; color: #2C3E50;'>We hope you enjoy the event! If you have any questions, please don't hesitate to ask.</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'><a href='https://www.facebook.com/btecsocomshcm' target='_blank'><img src='https://img.icons8.com/?size=100&id=uLWV5A9vXIPu&format=png&color=000000' alt='Facebook' width='50' height='50'></a></div>", unsafe_allow_html=True)
