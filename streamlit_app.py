import streamlit as st
import pandas as pd
import plotly.express as px

# Đọc dữ liệu từ GitHub
github_csv_url = "https://raw.githubusercontent.com/David-FPI/blank-app/main/vi.csv"
df = pd.read_csv(github_csv_url)

# Chuyển đổi investmentDate thành datetime
df["investmentDate"] = pd.to_datetime(df["investmentDate"], errors='coerce')

# Chuẩn hóa tên dự án để đảm bảo thống nhất
df["projectName"] = df["projectName"].str.strip().str.upper()

# Thiết lập giao diện
st.set_page_config(page_title="Phân Tích Đầu Tư Crypto", layout="wide")
st.title("💎 Phân Tích Đầu Tư Dự Án Crypto")

# Tổng quan
st.markdown("## 📌 Tổng Quan Về Đầu Tư")
st.markdown(
    f"""
    **📊 Tổng số giao dịch:** {df.shape[0]}  
    **💰 Tổng số tiền đầu tư:** \${df['amountInvested'].sum():,.2f}  
    **🪙 Tổng số token nhận được:** {df['tokensReceived'].sum():,.2f}
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

# Lọc dữ liệu chỉ hiển thị các giao dịch liên quan đến dự án Zupad
st.markdown("## 🏆 Giao Dịch Liên Quan Đến Dự Án Zupad")
zupad_df = df[df["projectName"] == "ZUPAD"]
st.dataframe(zupad_df.style.set_properties(**{"background-color": "#F8F9FA", "border": "1px solid #DEE2E6"}))
