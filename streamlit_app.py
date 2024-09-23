import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Event Agenda", page_icon="", layout="wide")

# Custom CSS
st.markdown("""
<style>
    body {
        color: #2C3E50;  /* Text color - adjust as desired */
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
        background-color: #ffffff;  /* Table background */
        color: #2C3E50;   /* Table text color - adjust as desired */
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .dataframe {
        background-color: #ffffff;  /* DataFrame background */
        color: #2C3E50;   /* DataFrame text color - adjust as desired */
    }
    .dataframe th {
        background-color: #3498DB;
        color: white;
    }
    .dataframe td {
        background-color: #ffffff;
    }
  /* Adjust color for all headings (h1, h2, h3) */
  h1, h2, h3 {
        color: #2C3E50;   /* Adjust as desired */
    }
  /* Adjust color for speaker class */
  .speaker {
        font-weight: bold;
        color: #3498DB;
    }
  /* Adjust color for st-bw and st-ew classes */
  .st-bw {
        color: #2C3E50;   /* Adjust as desired */
    }
  .st-ew {
        color: #2C3E50;   /* Adjust as desired */
    }
  /* Session details section */
  .markdown {  /* Adjust color for markdown elements */
      color: #2C3E50;   /* Adjust as desired */
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
st.table(df.style.set_properties(**
