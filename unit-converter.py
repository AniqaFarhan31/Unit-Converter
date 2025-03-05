import streamlit as st

def convert_units(category, from_unit, to_unit, value):
    conversion_factors = {
   'Length': {
        'meters': 1, 'kilometers': 0.001, 'miles': 0.000621371, 'feet': 3.28084, 'inches': 39.3701
    },
    'Time': {
        'seconds': 1, 'minutes': 1/60, 'hours': 1/3600, 'days': 1/86400
    },
    'Speed': {
        'mps': 1, 'kmph': 3.6, 'mph': 2.23694, 'fps': 3.28084
     }
    }
    return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

st.set_page_config(page_title="Unit Converter", page_icon="⚖️", layout="centered")
st.markdown("<h1 style='text-align: center; color:rgb(34, 6, 70);'>Unit Converter</h1>", unsafe_allow_html=True)

st.sidebar.header("Conversion Settings")
category = st.sidebar.selectbox("Select category", ["Length", "Time", "Speed"], key="category")

units = {
    "Length" : ["meters", "kilometers", "miles", "feet", "inches"],
    "Time": ["seconds", "minutes", "hours", "days"],
    "Speed": ["mps", "kmph", "mph", "fps"]
}

from_unit = st.selectbox("From Unit", units[category], key="from_unit")
to_unit = st.selectbox("To Unit", units[category], key="to_unit")
value = st.number_input("Enter Value", min_value=0.0, value=1.0, key="value")

if st.button("Convert"):
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")
