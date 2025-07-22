import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter your height (cm):", min_value=50, max_value=250)
weight = st.number_input("Enter your weight (kg):", min_value=10, max_value=200)

if st.button("Calculate"):
    if height and weight:
        bmi = weight / ((height/100) ** 2)
        st.write(f"Your BMI is {bmi:.2f}")
