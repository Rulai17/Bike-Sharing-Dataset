import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load datasets
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Mengubah format tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Streamlit Dashboard
st.title("Bike Sharing Dashboard")

# Sidebar filter
st.sidebar.header("Filters")
selected_season = st.sidebar.selectbox("Select Season", ['All', 'Spring', 'Summer', 'Fall', 'Winter'])

# Filter data berdasarkan musim
if selected_season != 'All':
    season_map = {'Spring': 1, 'Summer': 2, 'Fall': 3, 'Winter': 4}
    day_df = day_df[day_df['season'] == season_map[selected_season]]

# Menampilkan ringkasan data
st.subheader("Data Overview")
st.dataframe(day_df.head())

# Tren jumlah penyewaan sepeda harian
st.subheader("Tren Penyewaan Sepeda Harian")
st.line_chart(day_df.set_index("dteday")["cnt"])

# Distribusi penyewaan sepeda
st.subheader("Distribusi Penyewaan Sepeda")
st.bar_chart(day_df["cnt"])

# Hubungan suhu dengan penyewaan sepeda
st.subheader("Hubungan Suhu dengan Penyewaan Sepeda")
fig, ax = plt.subplots()
sns.scatterplot(x=day_df['temp'], y=day_df['cnt'], alpha=0.6, color='red', ax=ax)
ax.set_xlabel("Temperature (Normalized)")
ax.set_ylabel("Total Rentals")
ax.set_title("Hubungan antara Suhu dan Jumlah Penyewaan Sepeda")
st.pyplot(fig)

# Pola penggunaan sepeda pada hari kerja vs akhir pekan
st.subheader("Pola Penggunaan Sepeda pada Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots()
sns.boxplot(x=day_df['workingday'], y=day_df['cnt'], palette=['blue', 'orange'], ax=ax)
ax.set_xticklabels(['Weekend/Holiday', 'Working Day'])
ax.set_xlabel("Type of Day")
ax.set_ylabel("Total Rentals")
ax.set_title("Pola Penggunaan Sepeda pada Hari Kerja vs Akhir Pekan")
st.pyplot(fig)

# Menampilkan dataset yang telah dibersihkan
st.subheader("Download Cleaned Dataset")
st.download_button("Download CSV", day_df.to_csv(index=False), "cleaned_day.csv", "text/csv")
