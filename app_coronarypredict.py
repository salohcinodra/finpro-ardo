import pickle
import numpy as np 
import streamlit as st

# load save model
model = pickle.load(open('coronaryheart_disease_final.sav', 'rb'))

#tittle web
st.title('Coronary Heart Disease Prediction')
st.write('- age: age in years  - cp: chest pain type -- Value 0: typical angina -- Value 1: atypical angina -- Value 2: non-anginal pain -- Value 3: asymptomatic - trestbps: resting blood pressure (in mm Hg on admission to the hospital) - chol: serum cholestoral in mg/dl - fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false) - restecg: resting electrocardiographic results -- Value 0: normal -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) -- Value 2: showing probable or definite left ventricular hypertrophy by Estes criteria - thalach: maximum heart rate achieved - exang: exercise induced angina (1 = yes; 0 = no) - oldpeak = ST depression induced by exercise relative to rest - slope: the slope of the peak exercise ST segment -- Value 0: upsloping -- Value 1: flat -- Value 2: downsloping - ca: number of major vessels (0-3) colored by flourosopy - thal: 0 = normal; 1 = fixed defect; 2 = reversable defect and the label - condition: 0 = no disease, 1 = disease')
st.write('- sex: sex (1 = male; 0 = female')
# input for name
name = st.text_input("Enter your name:")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age')
with col2:
    sex = st.number_input ('Sex')
with col3:
    cp = st.number_input('Chest pain Type')
with col1:
    trestbps = st.number_input('Trestbps')
with col2:
    chol = st.number_input('Cholesterol')
with col3:
    fbs = st.number_input('Fasting Blood Sugar')
with col1:
    restecg = st.number_input('Restecg')
with col2:
    thalach = st.number_input('Thalach')
with col3:
    exang = st.number_input('Exang')
with col1:
    oldpeak = st.number_input('Oldpeak')
with col2:
    slope = st.number_input('Slope')
with col3:
    ca = st.number_input('CA Value')
with col1:
    thal = st.number_input('Thal Value')

#code for prediction
heart_diagnosis = ''

#Button prediction
if st.button('Prediction Coronary Heart Disease'):
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if (heart_prediction[0]==1):
        bg_color = 'red'
        heart_diagnosis = 'Patients have Coronary Heart Disease'
    else:
        bg_color = 'green'
        heart_diagnosis = 'Patients does not have Coronary Heart Disease'

# display the prediction result with name
if heart_diagnosis:
    st.markdown(f'<p style="font-size: 24px; color: {bg_color};">{name}, {heart_diagnosis}</p>', unsafe_allow_html=True)
