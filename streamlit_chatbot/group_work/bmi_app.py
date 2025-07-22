import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🧮")

st.title("🧮 BMI Calculator")
st.write("Welcome! This app calculates your **Body Mass Index (BMI)** and gives you health info.")

# Add some inputs
name = st.text_input("What is your name?")
age = st.number_input("How old are you?", min_value=1, max_value=120, value=18)
gender = st.radio("Select your gender:", ("Female", "Male"))

# Input height and weight
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=250.0, value=160.0, step=0.1)
weight = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=200.0, value=50.0, step=0.1)

# Calculate BMI
if st.button("Calculate My BMI!"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.subheader(f"Hello {name}, your BMI is: **{bmi:.2f}**")

    # Show result with emoji
    if bmi < 18.5:
        st.info("You are underweight. 🦴 Eat more balanced meals!")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight. 🥗 Keep it up!")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight. 🚶‍♀️ Consider more activity!")
    else:
        st.error("You are obese. 💡 Time to check with a doctor and eat healthier.")

    st.caption("Note: BMI is just a general guide and doesn't reflect muscle mass or overall health.")
