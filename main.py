import streamlit as st

def convert_unit(value,unit_from,unit_to):
    conversion={
        "meters_kilometers":0.001,
        "kilometers_meters":1000,
        "grams_kilograms":0.001,
        "kilogram_grams":1000
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversion:
        conversion = conversion[key]
        return value * conversion
    else:
        return "conversion not supported"

st.title("unit covertor")

value = st.number_input("Enter the value:")
unit_from = st.selectbox("convert from:",["meters","kilometers", "grams", "kilograms"])

unit_to = st.selectbox("convert to:",["meters","kilometers", "grams", "kilograms"])

if st.button("convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"converted value: {result }")
                                  
