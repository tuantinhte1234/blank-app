import streamlit as st
import pandas as pd
import plotly.express as px

# Đọc dữ liệu từ GitHub
github_csv_url = "https://raw.githubusercontent.com/David-FPI/blank-app/main/vi.csv"
df = pd.read_csv(github_csv_url)

# Chuẩn hóa dữ liệu
df["investmentDate"] = pd.to_datetime(df["investmentDate"], errors='coerce')
df["projectName"] = df["projectName"].str.strip().str.upper()

# Thiết lập giao diện
st.set_page_config(page_title="Phân Tích Đầu Tư Crypto", layout="wide")
st.title("💎 Phân Tích Đầu Tư Dự Án Crypto")

# Tổng quan
total_transactions = df.shape[0]
total_investment = df['amountInvested'].sum()
total_tokens = df['tokensReceived'].sum()
total_projects = df['projectName'].nunique()

st.markdown("## 📌 Tổng Quan Về Đầu Tư")
st.markdown(
    f"""
    **📊 Tổng số giao dịch:** {total_transactions}  
    **💰 Tổng số tiền đầu tư:** \${total_investment:,.2f}  
    **🪙 Tổng số token nhận được:** {total_tokens:,.2f}  
    **📌 Tổng số dự án:** {total_projects}  
    """
)

# Biểu đồ phân bổ đầu tư theo dự án
st.markdown("## 📊 Phân Bổ Đầu Tư Theo Dự Án")
fig1 = px.pie(df, names="projectName", values="amountInvested", title="Tỷ Trọng Đầu Tư Theo Dự Án")
st.plotly_chart(fig1, use_container_width=True)

# Biểu đồ mối quan hệ giữa số tiền đầu tư và token nhận được
st.markdown("## 🔗 Mối Quan Hệ Giữa Số Tiền Đầu Tư & Token Nhận Được")
fig2 = px.scatter(df, x="amountInvested", y="tokensReceived", color="projectName", title="Tương Quan Giữa Số Tiền Đầu Tư & Token Nhận Được")
st.plotly_chart(fig2, use_container_width=True)

# Biểu đồ xu hướng đầu tư theo thời gian
st.markdown("## 📈 Xu Hướng Đầu Tư Theo Thời Gian")
df_time = df.groupby(df["investmentDate"].dt.date)["amountInvested"].sum().reset_index()
fig3 = px.line(df_time, x="investmentDate", y="amountInvested", title="Xu Hướng Tổng Vốn Đầu Tư Theo Thời Gian")
st.plotly_chart(fig3, use_container_width=True)

# Biểu đồ phân bố số tiền đầu tư theo loại hình đầu tư
st.markdown("## ⚖️ Phân Tích Rủi Ro & Cơ Hội")
fig4 = px.box(df, x="investmentType", y="amountInvested", title="Phân Phối Số Tiền Đầu Tư Theo Loại Hình")
st.plotly_chart(fig4, use_container_width=True)

# Hiển thị bảng dữ liệu với Zupad lên đầu
st.markdown("## 🏆 Giao Dịch Đầu Tư")
df_sorted = df.copy()
df_sorted["is_zupad"] = df_sorted["projectName"].apply(lambda x: 1 if x == "ZUPAD" else 0)
df_sorted = df_sorted.sort_values(by=["is_zupad", "investmentDate"], ascending=[False, False]).drop(columns=["is_zupad"])

# Hướng dẫn sao chép địa chỉ ví
st.markdown("### 🔎 Tìm Kiếm Giao Dịch")
st.info("Nhấn Ctrl + C để sao chép địa chỉ ví và dán vào ô dưới để kiểm tra")

# Lựa chọn Wallet Address để xem giao dịch chi tiết
selected_wallet = st.selectbox("🔍 Chọn Ví Để Xem Giao Dịch:", ["Tất cả"] + df_sorted["walletAddress"].unique().tolist())

if selected_wallet != "Tất cả":
    df_wallet = df_sorted[df_sorted["walletAddress"] == selected_wallet]
    
    # Thống kê số lần sử dụng, tổng amountInvested và tokensReceived theo purchaseTokenSymbol
    purchase_token_stats = df_wallet.groupby("purchaseTokenSymbol").agg({
        "amountInvested": "sum",
        "tokensReceived": "sum",
        "purchaseTokenSymbol": "count"
    }).rename(columns={"purchaseTokenSymbol": "Số lần sử dụng"}).reset_index()

    # Đảm bảo không có giá trị NaN hoặc None
    purchase_token_stats = purchase_token_stats.fillna(0)
    
    # Loại bỏ dòng tổng hợp
    purchase_token_stats = purchase_token_stats[purchase_token_stats["purchaseTokenSymbol"] != "Tổng"]


# Hiển thị thông tin
st.markdown(f"### 📌 Tổng Kết Đầu Tư Của Ví {selected_wallet}")
st.markdown("#### 🏦 Thống Kê PurchaseTokenSymbol")
st.dataframe(purchase_token_stats, use_container_width=True)



# Nếu không chọn ví cụ thể, lấy toàn bộ dữ liệu
if selected_wallet == "Tất cả":
    df_wallet = df_sorted.copy()
else:
    df_wallet = df_sorted[df_sorted["walletAddress"] == selected_wallet]

# Thống kê tổng hợp đầu tư theo projectName
investment_summary = df_wallet.groupby("projectName").agg({
    "amountInvested": "sum",
    "tokensReceived": "sum",
    "projectName": "count"
}).rename(columns={"projectName": "Số lần đầu tư"}).reset_index()

# Đảm bảo không có giá trị NaN hoặc None
investment_summary = investment_summary.fillna(0)

# Dòng tổng hợp
total_row_summary = pd.DataFrame({
    "projectName": ["Tổng"],
    "Số lần đầu tư": [investment_summary["Số lần đầu tư"].sum()],
    "amountInvested": [investment_summary["amountInvested"].sum()],
    "tokensReceived": [investment_summary["tokensReceived"].sum()]
})

# Gộp dữ liệu lại
investment_summary = pd.concat([investment_summary, total_row_summary], ignore_index=True)

# Hiển thị bảng Tổng Hợp Đầu Tư
st.markdown("#### 📊 Tổng Hợp Đầu Tư")
st.dataframe(investment_summary, use_container_width=True)

# Hiển thị bảng giao dịch
df_sorted = df_wallet  # Cập nhật dữ liệu hiển thị
st.data_editor(df_sorted, height=500, use_container_width=True, hide_index=True)

