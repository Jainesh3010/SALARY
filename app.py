import streamlit as st
import pickle
import numpy as np


model = pickle.load(open("salary_model.pkl", "rb"))

st.title("💰 Salary Prediction App")


age = st.number_input("Age", 18, 60)
experience = st.number_input("Experience", 0, 40)

education = st.selectbox("Education", ["Bachelors", "Masters", "PhD"])

edu_map = {"Bachelors": 0, "Masters": 1,"Phd":2,"None":3}
education = edu_map[education]


city = st.selectbox("City", ["Ahmedabad", "Mumbai", "Delhi", "Bangalore","Pune","Hyderabad"])

city_map = {
    "Ahmedabad": 1,
    "Mumbai": 0,
    "Delhi": 3,
    "Bangalore": 2,
    "Hyderabad":4,
    "Pune":5
}

city = city_map[city]

ai = int(st.checkbox("AI"))
dl = int(st.checkbox("Deep Learning"))
ml = int(st.checkbox("Machine Learning"))
python_skill = int(st.checkbox("Python"))


if st.button("Predict Salary"):

    input_data = np.array([[
        age,
        experience,
        education,
        city,
        ai,
        dl,
        ml,
        python_skill
    ]])

    prediction = model.predict(input_data)

    st.success(f"Estimated Salary: ₹ {int(prediction[0])}")