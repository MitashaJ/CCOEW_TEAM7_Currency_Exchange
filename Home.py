import streamlit as st
import requests 
import json
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Currency Converter"
)

st.title("Currency Conversion")
st.sidebar.success("Select a page above")

def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

lottie_currency = load_lottiefile("E:\\NT_hackathon\\CCOEW_TEAM7_Currency_Exchange\\animation.json")
st_lottie(lottie_currency, quality='high')

col1, col2 = st.columns(2)

with col1:
    global curr1 
    curr1 = st.selectbox('Currency 1', ['AUD','BHD','BWP','BRL','BND','CAD','CLP','CNY','COP','CZK','DKK','EUR','HUF','ISK','INR','IDR','IRR','ILS','JPY','KZT','KRW','KWD','LYD','MYR','MUR','MXN',
                                        'NPR','NZD','NOK','OMR','PKR','PEN','PHP','PLN','QAR','RUB','SAR','SGD','ZAR','LKR','SEK','CHF','THB','TTD','TND','AED','GBP','USD','UYU','VES'])

with col2:
    global curr2
    curr2 = st.selectbox('Currency 2', ['AUD','BHD','BWP','BRL','BND','CAD','CLP','CNY','COP','CZK','DKK','EUR','HUF','ISK','INR','IDR','IRR','ILS','JPY','KZT','KRW','KWD','LYD','MYR','MUR','MXN',
                                        'NPR','NZD','NOK','OMR','PKR','PEN','PHP','PLN','QAR','RUB','SAR','SGD','ZAR','LKR','SEK','CHF','THB','TTD','TND','AED','GBP','USD','UYU','VES'])

url = f"https://v6.exchangerate-api.com/v6/5063b86e4e65a0219579c7fc/pair/{curr1}/{curr2}/1"

re = requests.get(url)
data = re.json()['conversion_rate']

col1, col2 = st.columns(2)
with col1:
    global amount
    amount = st.number_input(curr1)
with col2:
    converted = amount*data
    st.text('Converted amount')
    st.success(converted)
    
st.markdown('<style> body{text-align:center;}</style>',unsafe_allow_html=True)
