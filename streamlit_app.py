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

# Tiêu đề ứng dụng
st.title("📊 Phân Tích Đầu Tư Dự Án Crypto")

# Tổng quan
st.header("1️⃣ Tổng Quan Về Đầu Tư")
st.write(f"**Tổng số giao dịch:** {df.shape[0]}")
st.write(f"**Tổng số tiền đầu tư:** ${df['amountInvested'].sum():,.2f}")
st.write(f"**Tổng số token nhận được:** {df['tokensReceived'].sum():,.2f}")

# Biểu đồ phân bổ đầu tư theo dự án
st.header("2️⃣ Phân Bổ Đầu Tư Theo Dự Án")
fig1 = px.pie(df, names="projectName", values="amountInvested", title="Tỷ trọng đầu tư theo dự án")
st.plotly_chart(fig1)

# Biểu đồ mối quan hệ giữa amountInvested và tokensReceived
st.header("3️⃣ Mối Quan Hệ Giữa Số Tiền Đầu Tư Và Token Nhận Được")
fig2 = px.scatter(df, x="amountInvested", y="tokensReceived", color="projectName", title="Tương quan giữa số tiền đầu tư và số token nhận được")
st.plotly_chart(fig2)

# Biểu đồ xu hướng đầu tư theo thời gian
st.header("4️⃣ Xu Hướng Đầu Tư Theo Thời Gian")
df_time = df.groupby(df["investmentDate"].dt.date)["amountInvested"].sum().reset_index()
fig3 = px.line(df_time, x="investmentDate", y="amountInvested", title="Xu hướng tổng vốn đầu tư theo thời gian")
st.plotly_chart(fig3)

# Biểu đồ phân bố số tiền đầu tư theo loại hình đầu tư
st.header("5️⃣ Phân Tích Rủi Ro & Cơ Hội")
fig4 = px.box(df, x="investmentType", y="amountInvested", title="Phân phối số tiền đầu tư theo loại hình")
st.plotly_chart(fig4)

# Lọc dữ liệu chỉ hiển thị các giao dịch liên quan đến dự án Zupad
st.header("6️⃣ Giao Dịch Liên Quan Đến Dự Án Zupad")
zupad_df = df[df["projectName"] == "ZUPAD"]
st.dataframe(zupad_df)
