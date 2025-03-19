import streamlit as st
import pandas as pd

# Đúng đường dẫn RAW của file CSV trên GitHub
github_csv_url = "https://raw.githubusercontent.com/David-FPI/blank-app/main/vi.csv"

st.title("📊 Dữ liệu giao dịch Zupad từ GitHub")

try:
    # Đọc dữ liệu từ GitHub
    df = pd.read_csv(github_csv_url)

    # Lọc dữ liệu có projectName là "Zupad"
    filtered_df = df[df["projectName"].str.lower() == "zupad"]

    # Hiển thị dữ liệu
    st.write("📊 Dữ liệu giao dịch của Zupad:")
    st.dataframe(filtered_df)

    # Cho phép tải xuống dữ liệu sau khi lọc
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Tải xuống dữ liệu", data=csv, file_name="filtered_zupad.csv", mime="text/csv")

except Exception as e:
    st.error("🚨 Không thể tải dữ liệu. Kiểm tra lại đường link GitHub hoặc file có đúng định dạng không.")
