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
df.insert(0, "STT", range(1, len(df) + 1))  # Chèn cột số thứ tự vào vị trí đầu
#st.dataframe(df, use_container_width=True)
st.dataframe(df, use_container_width=True, hide_index=True)

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

    # Chia giao diện thành 3 cột
    col1, col2, col3 = st.columns(3)
    
    # Duyệt qua từng token và hiển thị trong từng cột
    for col, token in zip([col1, col2, col3], tokens):
        df_token = df_filtered[df_filtered["purchaseTokenSymbol"] == token]

        if not df_token.empty:
            # Nhóm dữ liệu theo projectName và tính tổng amountInvested
            summary = df_token.groupby("projectName")["amountInvested"].sum().reset_index()

            # Thêm ký hiệu "$"
            summary["amountInvested"] = summary["amountInvested"].apply(lambda x: f"${x:,.2f}")

            # Tính tổng số tiền đầu tư của token đó
            total_amount = df_token["amountInvested"].sum()
        else:
            # Nếu không có dữ liệu, tạo bảng rỗng với thông báo
            summary = pd.DataFrame({"projectName": ["Không có giao dịch"], "amountInvested": ["-"]})
            total_amount = 0
        # Đảm bảo bảng có đúng 9 hàng
        while len(summary) < 10:
            summary = pd.concat([summary, pd.DataFrame({"projectName": [""], "amountInvested": [""]})], ignore_index=True)
        summary.insert(0, "Số thứ tự", range(1, len(summary) + 1))
        # Hiển thị bảng trong từng cột
        with col:
            st.subheader(f"{token}")
            st.dataframe(summary, use_container_width=True)
            st.markdown(f"**Tổng {token}:** ${total_amount:,.2f}")

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
search_transactions(df)
