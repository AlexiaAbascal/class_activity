import streamlit as st
import pickle
import numpy as np

with open("classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

st.title("Heart Failure Classifier")
st.write("Input your heart measurements to get a heart attack prediction")

age = st.slider("Enter patient's age", min_value=18, max_value=100, step=1)
anemia = st.slider("Does the patient have anemia? Yes:1 No:0", min_value=0, max_value=1, step=1)
creatinine_phosphokinase = st.slider("Enter levels of creatinine_phosphokinase", min_value=0, max_value=10000, step=1)
diabetes = st.slider("Does the patient have diabetes? Yes:1 No:0", min_value=0, max_value=1, step=1)
ejection_fraction =  st.slider("Enter levels of ejection_fraction", min_value=0, max_value=100, step=1)
hbp = st.slider("Does the patient have high blood pressure? Yes:1 No:0", min_value=0, max_value=1, step=1)
platelets = st.slider("Platelets: ", min_value=10000, max_value=1000000, step=1)
serum_creatinine = st.slider("Serum creatinine: ", min_value=0, max_value=15, step=1)
serum_sodium = st.slider("Serum sodium: ", min_value=50, max_value=200, step=1)
sex = st.slider("Sex (0 female, 1 male)", min_value=0, max_value=1, step=1)
smoking = st.slider("Does the patient smoke?", min_value=0, max_value=1, step=1)
time = st.slider("Indicate time", min_value=0, max_value=300, step=1)


if st.button("Predict"):
    features = np.array([[age, anemia,creatinine_phosphokinase,diabetes,ejection_fraction,hbp,platelets,serum_creatinine,serum_sodium,sex,smoking,time]])
    prediction = model.predict(features)
    st.write(f"Predicted (1 you die and 0 you won't): {prediction[0]} ")