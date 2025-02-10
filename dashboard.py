import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# memuat dataset
day_df = pd.read_csv("day.csv")


day_df['dateday'] = pd.to_datetime(day_df['dateday'])

#judul
st.title("Bike Sharing Dashboard")

selected_year = st.sidebar.selectbox("Select Year", ["All", 2011, 2012])
if selected_year != "All":
    day_df = day_df[day_df['yr'] == (selected_year - 2011)]

st.subheader("Dataset Preview")
st.dataframe(day_df.head())

# line chart
st.subheader("Daily Bike Rentals Trend")
st.line_chart(day_df.set_index("dteday")["cnt"])

# scatter plot 
st.subheader("Temperature vs Bike Rentals")
fig, ax = plt.subplots()
sns.scatterplot(x=day_df['temp'], y=day_df['cnt'], ax=ax)
ax.set_xlabel("Temperature (Normalized)")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

# boxplot
st.subheader("Bike Rentals on Working vs Non-Working Days")
fig, ax = plt.subplots()
sns.boxplot(x=day_df['workingday'], y=day_df['cnt'], ax=ax)
ax.set_xticklabels(['Non-Working Day', 'Working Day'])
st.pyplot(fig)

# Download data 
st.subheader("Download Dataset")
st.download_button("Download CSV", day_df.to_csv(index=False), "cleaned_day.csv", "text/csv")
