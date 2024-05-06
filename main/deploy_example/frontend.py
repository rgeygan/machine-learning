import streamlit as st
import json
import requests

from utils import validate_value, show_info_message

st.title("Wine Quality Predictor Model")

# user inputs

st.markdown("<p style='font-size: 18px;'>Provide Information About Your Wine</p>", unsafe_allow_html=True)

st.markdown("<p style='font-size: 14px;'>Note: You must provide an alcohol percentage or you will recieve an Internal Server Error. If you don't have data for the other values that's ok, just leave the input at 0.0</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 14px;'>The prediction will be improved with more values especially sulphates, volatile acidity, and total sulfur dioxide</p>", unsafe_allow_html=True)

# Frontend should give units and more helpful description around what values are acceptable

# Define the input fields with validation and informational messages
show_info_message(8.4, 14.9)
alcohol = st.number_input(label='Alcohol Percentage', value=0.0, format='%.2f')
alcohol = validate_value(alcohol, 8.4, 14.9)

show_info_message(4.6, 15.9)
fixed_acidity = st.number_input(label='Fixed Acidity', value=0.0, format='%.2f')
fixed_acidity = validate_value(fixed_acidity, 4.6, 15.9)

show_info_message(0.12, 1.58)
volatile_acidity = st.number_input(label='Volatile Acidity', value=0.0, format='%.2f')
volatile_acidity = validate_value(volatile_acidity, 0.12, 1.58)

show_info_message(0.0, 1.0)
citric_acid = st.number_input(label='Citric Acid', value=0.0, format='%.2f')
citric_acid = validate_value(citric_acid, 0.0, 1.0)

show_info_message(0.9, 15.5)
residual_sugar = st.number_input(label='Residual Sugar', value=0.0, format='%.2f')
residual_sugar = validate_value(residual_sugar, 0.9, 15.5)

show_info_message(0.012, 0.611)
chlorides = st.number_input(label='Chlorides', value=0.0, format='%.3f')
chlorides = validate_value(chlorides, 0.012, 0.611)

show_info_message(1.0, 72.0)
free_sulfur_dioxide = st.number_input(label='Free Sulfur Dioxide', value=0.0, format='%.2f')
free_sulfur_dioxide = validate_value(free_sulfur_dioxide, 1.0, 72.0)

show_info_message(6.0, 289.0)
total_sulfur_dioxide = st.number_input(label='Total Sulfur Dioxide', value=0.0, format='%.2f')
total_sulfur_dioxide = validate_value(total_sulfur_dioxide, 6.0, 289.0)

show_info_message(0.99, 1.00)
density = st.number_input(label='Density', value=0.0, format='%.3f')
density = validate_value(density, 0.99, 1.00)

show_info_message(2.74, 4.01)
pH = st.number_input(label='pH', value=0.0, format='%.2f')
pH = validate_value(pH, 2.74, 4.01)

show_info_message(0.33, 2.0)
sulphates = st.number_input(label='Sulphates', value=0.0, format='%.2f')
sulphates = validate_value(sulphates, 0.33, 2.0)



#Converting the inputs to list and making sure they are in the correct order for model input
#This would ideally have more validation around it
inputs = {"fixed_acidity": fixed_acidity, 
            "volatile_acidity": volatile_acidity, 
            "citric_acid": citric_acid, 
            "residual_sugar": residual_sugar, 
            "chlorides": chlorides, 
            "free_sulfur_dioxide": free_sulfur_dioxide, 
            "total_sulfur_dioxide": total_sulfur_dioxide, 
            "density": density, 
            "pH": pH, 
            "sulphates": sulphates, 
            "alcohol": alcohol
            }

# when the user clicks on button it will fetch the API
if st.button('Predict'):
    res = requests.post(url = "http://127.0.0.1:8000/make_prediction", data=json.dumps(inputs))

    cleaned_value = res.text.strip('"')  # Remove the quotes
    response = int(cleaned_value)

    st.subheader(f"Your Expected Wine Quality Rating is {response} out of 10")