import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression   #python -m pip install scikit-learn
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# Load predefined CSV files into a DataFrame
predefined_files = ['Exchange_Rate_Report_2012.csv', 'Exchange_Rate_Report_2013.csv', 'Exchange_Rate_Report_2014.csv',
                    'Exchange_Rate_Report_2015.csv', 'Exchange_Rate_Report_2016.csv',
                    'Exchange_Rate_Report_2017.csv', 'Exchange_Rate_Report_2018.csv', 'Exchange_Rate_Report_2019.csv',
                    'Exchange_Rate_Report_2020.csv', 'Exchange_Rate_Report_2021.csv', 'Exchange_Rate_Report_2022.csv']

# Combine data from all CSV files
combined_data = pd.concat([pd.read_csv(file) for file in predefined_files])

# Convert the 'Date' column to datetime format
combined_data['Date'] = pd.to_datetime(combined_data['Date'])

# Streamlit UI
st.title("Currency Value Prediction")

# Select currency pair
currency = st.selectbox("Select Currency", combined_data.columns[1:])

# Create new columns for year and month
combined_data['Year'] = combined_data['Date'].dt.year
combined_data['Month'] = combined_data['Date'].dt.month

# Calculate the average currency value for each month and year
average_currency_values = combined_data.groupby(['Year', 'Month'])[currency].mean().reset_index()

# Prepare the data for machine learning
X = average_currency_values[['Year', 'Month']]
y = average_currency_values[currency]

# Combine Year and Month into a single feature
X['Combined'] = X['Year'] * 100 + X['Month']

# Reshape the data
X = X['Combined'].values.reshape(-1, 1)
y = y.values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = model.score(X_test, y_test)

# Allow the user to input a specific month and year for prediction
selected_month_year = st.text_input("Enter Month and Year for Prediction (YYYY-MM):")

try:
    year, month = map(int, selected_month_year.split('-'))
    selected_date_feature = year * 100 + month
    predicted_value = model.predict([[selected_date_feature]])[0]
except ValueError:
    predicted_value = None

# Plot the regression line with year as x-axis labels
regression_line_x = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
regression_line_y = model.predict(regression_line_x)

# Extract year from Combined feature for x-axis labels
regression_line_years = regression_line_x.flatten() // 100

# Display regression line and coefficients
st.subheader("Regression Line:")
fig, ax = plt.subplots()
ax.scatter(X.flatten() // 100, y, label='Actual Data')  # Use year for x-axis labels
ax.plot(regression_line_years, regression_line_y, color='red', label='Regression Line')
ax.set_xlabel("Year")  # Change x-axis label
ax.set_ylabel(currency)
ax.legend()
st.pyplot(fig)

st.subheader("Regression Coefficients:")
st.write(f"Intercept: {model.intercept_}")
st.write(f"Coefficient: {model.coef_[0]}")

# Display predicted value and accuracy
st.subheader(f"Predicted {currency} exchange rate in {selected_month_year}:")
if predicted_value is not None:
    st.write(f"*{predicted_value:.4f}*")
else:
    st.write("Please enter a valid Month and Year.")
st.write(f"Model Accuracy: {accuracy:.4f}")
