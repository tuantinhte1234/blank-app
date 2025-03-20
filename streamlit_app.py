import streamlit as st
import pandas as pd

# Tải dữ liệu từ GitHub
github_csv_url = "https://raw.githubusercontent.com/David-FPI/blank-app/main/vi.csv"
df = pd.read_csv(github_csv_url)

# Định dạng dữ liệu
df["amountInvested"] = pd.to_numeric(df["amountInvested"], errors="coerce")
df["tokensReceived"] = pd.to_numeric(df["tokensReceived"], errors="coerce")

# Tùy chỉnh giao diện
st.set_page_config(page_title="Báo Cáo Wallet", layout="wide")

# CSS để làm chữ to, dễ đọc hơn
st.markdown("""
    <style>
        h1, h2, h3, h4 { font-size: 24px !important; }
        .stDataFrame { font-size: 18px !important; }
        .stTextInput>div>div>input { font-size: 18px !important; height: 40px; }
        .stMarkdown { font-size: 18px !important; }
        div[data-testid="stVerticalBlock"] { padding: 10px 20px; }
    </style>
""", unsafe_allow_html=True)

# Hiển thị toàn bộ dataset trước
st.title("📈 Báo Cáo Wallet Address")
st.subheader("📋 Dữ Liệu Giao Dịch")
st.dataframe(df, use_container_width=True)

# === PHẦN 1: TỔNG QUAN ĐẦU TƯ ===
def display_overview(df):
    st.header("📊 Tổng Quan Đầu Tư")
    
    col1, col2 = st.columns(2)
    
    with col1:
        total_investment_by_token = df.groupby("purchaseTokenSymbol")["amountInvested"].sum().reset_index()
        st.subheader("💰 Tổng Số Đầu Tư Của Từng Token")
        st.dataframe(total_investment_by_token, use_container_width=True)

    with col2:
        total_tokens_by_project = df.groupby("projectName")["tokensReceived"].sum().reset_index()
        st.subheader("🪙 Tổng Số Token Đã Bán Của 21 Dự Án")
        st.dataframe(total_tokens_by_project, use_container_width=True)
    
    # Hiển thị tổng số tiền đầu tư dưới dạng chữ đậm
    total_investment_usd = df["amountInvested"].sum()
    st.markdown(f"### 💵 **Tổng Số Đầu Tư Quy Đổi: ${total_investment_usd:,.2f}**", unsafe_allow_html=True)

# #=== PHẦN 2: TÌM KIẾM GIAO DỊCH ===
# def search_transactions(df):
#     st.header("🔍 Tìm Kiếm Giao Dịch")
    
#     selected_wallet = st.text_input("Nhập Địa Chỉ Ví:", "")
    
#     if selected_wallet:
#         df_filtered = df[df["walletAddress"].str.contains(selected_wallet, case=False, na=False)]
#     else:
#         df_filtered = df
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         summary_by_token = df_filtered.groupby("purchaseTokenSymbol")["amountInvested"].sum().reset_index()
#         st.subheader("📑 Tổng Hợp Số Tiền Đầu Tư Của Từng Token")
#         st.dataframe(summary_by_token, use_container_width=True)
    
#     with col2:
#         details_by_project = df_filtered.groupby(["purchaseTokenSymbol", "projectName"])["amountInvested"].sum().reset_index()
#         st.subheader("📊 Chi Tiết Đầu Tư Của Từng Token Cho 21 Dự Án")
#         st.dataframe(details_by_project, use_container_width=True)
#=== PHẦN 2: TÌM KIẾM GIAO DỊCH ===
def search_transactions(df):
    st.header("🔍 Tìm Kiếm Giao Dịch")

    selected_wallet = st.text_input("Nhập Địa Chỉ Ví:", "")

    if selected_wallet:
        df_filtered = df[df["walletAddress"].str.contains(selected_wallet, case=False, na=False)]
    else:
        df_filtered = df

    # Danh sách token cần hiển thị bảng riêng
    tokens = ["USDT", "ZUKIPOINT", "ZUKIVERSE"]
    
    for token in tokens:
        df_token = df_filtered[df_filtered["purchaseTokenSymbol"] == token]
        
        if not df_token.empty:
            # Nhóm dữ liệu theo projectName và tính tổng amountInvested
            summary = df_token.groupby("projectName")["amountInvested"].sum().reset_index()
            
            # Thêm ký hiệu "$"
            summary["amountInvested"] = summary["amountInvested"].apply(lambda x: f"${x:,.2f}")

            # Tính tổng số tiền đầu tư của token đó
            total_amount = df_token["amountInvested"].sum()

            # Hiển thị bảng
            st.subheader(f"📊 Chi Tiết Đầu Tư: {token}")
            st.dataframe(summary, use_container_width=True)

            # Hiển thị tổng số tiền đầu tư
            st.markdown(f"**Tổng {token}:** ${total_amount:,.2f}")

# === PHẦN 3: CHI TIẾT ĐẦU TƯ (ĐỂ CUỐI CÙNG) ===
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

# === HIỂN THỊ CÁC PHẦN ===
display_overview(df)
#search_transactions(df)
