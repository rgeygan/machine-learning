import streamlit as st

# Define functions to add validation and informational messages
def validate_value(value, min_value, max_value):
    if value is None:
        return None
    elif value == 0.0:
        return None
    elif min_value <= value <= max_value:
        return value
    else:
        st.error(f"The value must be between {min_value} and {max_value}")
        return None

def show_info_message(min_value, max_value):
    st.write(f"This value can only be between {min_value} and {max_value}")