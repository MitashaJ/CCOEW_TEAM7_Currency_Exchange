import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files into a DataFrame
data_files = ['Exchange_Rate_Report_2012.csv', 'Exchange_Rate_Report_2013.csv', 'Exchange_Rate_Report_2014.csv', 'Exchange_Rate_Report_2015.csv', 'Exchange_Rate_Report_2016.csv',
              'Exchange_Rate_Report_2017.csv', 'Exchange_Rate_Report_2018.csv', 'Exchange_Rate_Report_2019.csv', 'Exchange_Rate_Report_2020.csv', 'Exchange_Rate_Report_2021.csv','Exchange_Rate_Report_2022.csv']

# Combine data from all CSV files
combined_data = pd.concat([pd.read_csv(file) for file in data_files])

# Convert the 'Date' column to datetime format
combined_data['Date'] = pd.to_datetime(combined_data['Date'])

# Set 'Date' as the index for better plotting
combined_data.set_index('Date', inplace=True)

# Streamlit UI
st.title("Exchange Rate Analysis Dashboard")

# Select currency pair
currency1 = 'USD'
currency2 = st.selectbox("Select Currency 2", combined_data.columns[1:])

# Select date range
start_date =pd.to_datetime(st.date_input("Select Start Date", combined_data.index.min())) 
end_date = pd.to_datetime(st.date_input("Select End Date", combined_data.index.max()))
# Filter data based on user input
filtered_data = combined_data[(combined_data.index >= start_date) & (combined_data.index <= end_date)]

# Plot the data
st.line_chart(filtered_data[[currency2]])

# Display highest and lowest rates
max_rate_date = filtered_data[currency2].idxmax()
min_rate_date = filtered_data[currency2].idxmin()

max_rate = filtered_data.loc[max_rate_date, currency2]
min_rate = filtered_data.loc[min_rate_date, currency2]

st.write(f"Highest rate ({currency1}/{currency2}): {max_rate} on {max_rate_date}")
st.write(f"Lowest rate ({currency1}/{currency2}): {min_rate} on {min_rate_date}")


