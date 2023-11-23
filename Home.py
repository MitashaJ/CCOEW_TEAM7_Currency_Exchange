import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

# Function to load a Lottie animation from a file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Function to get the conversion rate from an API
def get_conversion_rate(curr1, curr2):
    # API endpoint for currency conversion
    url = f"https://v6.exchangerate-api.com/v6/5063b86e4e65a0219579c7fc/pair/{curr1}/{curr2}/1"
    
    # Make an HTTP GET request to the API
    response = requests.get(url)
    data = response.json()

    # Check if the API request was successful
    if data['result'] == 'success':
        return data['conversion_rate']
    else:
        # Display an error message if the API request fails
        st.error("Error fetching conversion rate.")
        return None

# Main function for the Streamlit app
def main():
    # Set page configuration and title
    st.set_page_config(page_title="Currency Converter")
    st.title("Currency Conversion")
    st.sidebar.success("Select a page above")

    # Load and display a Lottie animation
    lottie_currency = load_lottiefile("E:\\NT_hackathon\\CCOEW_TEAM7_Currency_Exchange\\animation.json")
    st_lottie(lottie_currency, quality='high')

    # Create a form for the currency converter
    with st.form("currency_converter_form"):
        # Create two columns for currency selection
        col1, col2 = st.columns(2)
        
        # Currency 1 selection dropdown
        with col1:
            curr1 = st.selectbox('Currency 1', ['AUD', 'BHD', 'BWP', 'BRL', 'BND', 'CAD', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'EUR', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'ILS', 'JPY', 'KZT', 'KRW', 'KWD', 'LYD', 'MYR', 'MUR', 'MXN',
                                                'NPR', 'NZD', 'NOK', 'OMR', 'PKR', 'PEN', 'PHP', 'PLN', 'QAR', 'RUB', 'SAR', 'SGD', 'ZAR', 'LKR', 'SEK', 'CHF', 'THB', 'TTD', 'TND', 'AED', 'GBP', 'USD', 'UYU', 'VES'])
        
        # Currency 2 selection dropdown
        with col2:
            curr2 = st.selectbox('Currency 2', ['AUD', 'BHD', 'BWP', 'BRL', 'BND', 'CAD', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'EUR', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'ILS', 'JPY', 'KZT', 'KRW', 'KWD', 'LYD', 'MYR', 'MUR', 'MXN',
                                                'NPR', 'NZD', 'NOK', 'OMR', 'PKR', 'PEN', 'PHP', 'PLN', 'QAR', 'RUB', 'SAR', 'SGD', 'ZAR', 'LKR', 'SEK', 'CHF', 'THB', 'TTD', 'TND', 'AED', 'GBP', 'USD', 'UYU', 'VES'])
        
        # Input field for the amount
        amount = st.number_input('Enter amount')

        # Center-align the button using HTML and inline CSS
        st.write("<div style='text-align: center;'>", unsafe_allow_html=True)
        
        # Submit button to perform the conversion
        if st.form_submit_button("Convert"):
            conversion_rate = get_conversion_rate(curr1, curr2)

            # Check if conversion rate is obtained successfully
            if conversion_rate is not None:
                converted_amount = amount * conversion_rate
                st.success(f"Converted amount: {converted_amount:.2f} {curr2}")
        
        st.write("</div>", unsafe_allow_html=True)

        #styling
        st.markdown('<style> body{text-align:center;}</style>',unsafe_allow_html=True)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
