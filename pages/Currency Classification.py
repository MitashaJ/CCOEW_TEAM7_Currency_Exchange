import pandas as pd
import streamlit as st

# Load your CSV file
file_path = 'E:\\NT_hackathon\\CCOEW_TEAM7_Currency_Exchange\\Exchange_Rate_Report_2022.csv'
df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

# Assuming the CSV has columns like 'Date', 'Country1', 'Country2', ... (where Country1, Country2, etc. are currency exchange values compared to USD)

# Calculate average currency value for each currency
average_currency_values = df.mean()

# Streamlit UI for user input
st.title("Currency Classification App")

# User input for category thresholds
low_threshold = st.slider("Select low valuation threshold", min_value=0, max_value=100, step=1, value=20)
medium_threshold = st.slider("Select medium valuation threshold", min_value=0, max_value=100, step=1, value=50)
high_threshold = st.slider("Select high valuation threshold", min_value=0, max_value=100, step=1, value=100)

# Categorize currencies based on user-selected thresholds
low_valuation_currencies = average_currency_values[average_currency_values <= low_threshold].index
medium_valuation_currencies = average_currency_values[
    (average_currency_values > low_threshold) & (average_currency_values <= medium_threshold)].index
high_valuation_currencies = average_currency_values[average_currency_values > medium_threshold].index

# Display currencies based on user-selected category
selected_category = st.radio("Select category", ['Low', 'Medium', 'High'])

if st.button("Show Currencies"):
    if selected_category == 'Low':
        result_currencies = low_valuation_currencies
    elif selected_category == 'Medium':
        result_currencies = medium_valuation_currencies
    elif selected_category == 'High':
        result_currencies = high_valuation_currencies
    else:
        st.warning("Invalid category selected. Please choose Low, Medium, or High.")

    # Print resultant currencies with their average currency value in increasing order
    result_df = average_currency_values[result_currencies].sort_values()
    st.write(f"Currencies in the {selected_category} category:")
    st.write(result_df)
    st.write(f"Number of currencies: {len(result_df)}")