import streamlit as st
import pandas as pd

# Upload file lên Streamlit
st.title("vi.csv")

uploaded_file = st.file_uploader("vi.csv", type=["csv"])

if uploaded_file is not None:
    # Đọc dữ liệu
    df = pd.read_csv(uploaded_file)

    # Lọc dữ liệu có projectName là "Zupad"
    filtered_df = df[df["projectName"].str.lower() == "zupad"]

    # Hiển thị kết quả
    st.write("📊 Dữ liệu giao dịch của Zupad:")
    st.dataframe(filtered_df)

    # Cho phép tải xuống file sau khi lọc
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Tải xuống dữ liệu", data=csv, file_name="filtered_zupad.csv", mime="text/csv")
