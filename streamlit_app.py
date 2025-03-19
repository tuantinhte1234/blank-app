import streamlit as st
import pandas as pd

# Tải dữ liệu từ GitHub
github_csv_url = "https://raw.githubusercontent.com/David-FPI/blank-app/main/vi.csv"
df = pd.read_csv(github_csv_url)

# Định dạng dữ liệu
df["amountInvested"] = pd.to_numeric(df["amountInvested"], errors="coerce")
df["tokensReceived"] = pd.to_numeric(df["tokensReceived"], errors="coerce")

# 🏆 Hiển thị toàn bộ dataset trước
st.title("📈 Báo Cáo Wallet Address")
st.write("### 🗂 Dữ Liệu Giao Dịch")
st.dataframe(df, use_container_width=True)

def display_overview(df):
    st.header("📊 Tổng Quan Đầu Tư")
    
    # 1. Tổng số đầu tư của từng token
    total_investment_by_token = df.groupby("purchaseTokenSymbol")["amountInvested"].sum().reset_index()
    st.write("### 💰 Tổng Số Đầu Tư Của Từng Token")
    st.dataframe(total_investment_by_token, use_container_width=True)
    
    # 2. Tổng số token đã bán của 21 dự án
    total_tokens_by_project = df.groupby("projectName")["tokensReceived"].sum().reset_index()
    st.write("### 🪙 Tổng Số Token Đã Bán Của 21 Dự Án")
    st.dataframe(total_tokens_by_project, use_container_width=True)
    
    # 3. Tổng số đầu tư quy đổi ra USD
    total_investment_usd = df["amountInvested"].sum()
    st.write(f"### 💵 Tổng Số Đầu Tư Quy Đổi: **${total_investment_usd:,.2f}**")

def search_transactions(df):
    st.header("🔍 Tìm Kiếm Giao Dịch")
    selected_wallet = st.text_input("Nhập Địa Chỉ Ví:", "")
    
    if selected_wallet:
        df_filtered = df[df["walletAddress"].str.contains(selected_wallet, case=False, na=False)]
    else:
        df_filtered = df
    
    # 1. Bảng tổng hợp số tiền đầu tư của từng token
    summary_by_token = df_filtered.groupby("purchaseTokenSymbol")["amountInvested"].sum().reset_index()
    st.write("### 📑 Bảng Tổng Hợp Số Tiền Đầu Tư Của Từng Token")
    st.dataframe(summary_by_token, use_container_width=True)
    
    # 2. Bảng chi tiết đầu tư của từng token cho 21 dự án
    details_by_project = df_filtered.groupby(["purchaseTokenSymbol", "projectName"])["amountInvested"].sum().reset_index()
    st.write("### 📊 Bảng Chi Tiết Đầu Tư Của Từng Token Cho 21 Dự Án")
    st.dataframe(details_by_project, use_container_width=True)

# Hiển thị Tổng Quan Đầu Tư và Tìm Kiếm trước
display_overview(df)
search_transactions(df)

# 🏆 Chi Tiết Đầu Tư Để Ở DƯỚI CÙNG
st.markdown("---")
st.header("🏆 Chi Tiết Đầu Tư Của Từng Token Cho 21 Dự Án")

if df.empty:
    st.warning("Không có dữ liệu giao dịch.")
    detail_investment_summary = pd.DataFrame(columns=["projectName", "purchaseTokenSymbol", "amountInvested", "tokensReceived"])
else:
    detail_investment_summary = df.groupby(["projectName", "purchaseTokenSymbol"]).agg({
        "amountInvested": "sum",
        "tokensReceived": "sum"
    }).reset_index()

st.dataframe(detail_investment_summary, use_container_width=True)
