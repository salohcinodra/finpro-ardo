import pickle
import numpy as np 
import streamlit as st

# load saved model
model = pickle.load(open('coronaryheart_disease_final.sav', 'rb'))

# Title web
st.title('Prediction Application of Coronary Heart Disease')
st.write('---')

st.subheader('Explanation of Coronary Heart Disease')
st.write('Coronary heart disease (CHD), also known as coronary artery disease (CAD), is a condition in which the blood vessels that supply blood to the heart (coronary arteries) become narrowed or blocked. This results in less blood supply to the heart muscle, which can lead to a variety of serious symptoms and complications, including heart attack.')

st.subheader('The causes of coronary heart disease:')
st.write('1. Atherosclerosis: This is the main cause of narrowing of the coronary arteries. Atherosclerosis occurs when fat, cholesterol, and other substances build up inside the artery walls, forming plaques that narrow the artery lumen.')
st.write('2. Narrowing of the arteries: Besides atherosclerosis, other conditions such as arterial inflammation, arterial spasm, and blood clots can also lead to narrowing of the coronary arteries.')
st.write('3. Risk factors: These include smoking, diabetes, high blood pressure, high cholesterol, obesity, lack of exercise, unhealthy diet, and family history of heart disease.')

st.subheader('Symptoms of coronary heart disease:')
st.write('1. Chest pain: This is the most common symptom. Pain or discomfort in the chest (angina) often occurs during physical exertion or stress.')
st.write('2. Pain in the arms, shoulders, back, neck or jaw: This symptom may occur along with chest pain or on its own.')
st.write('3. Shortness of breath: Especially during physical activity.')
st.write('4. Unreasonable fatigue: Feeling suddenly tired for no apparent reason.')
st.write('5. Nausea and vomiting: Especially in women.')
st.write('6. Irregular or rapid heartbeat: Palpitations are another possible symptom.')

st.subheader('Treatment for coronary heart disease:')
st.write('1. Lifestyle changes: These include quitting smoking, having a healthy low-fat and low-salt diet, exercising regularly, and managing stress.')
st.write('2. Medications: Such as antiplatelets, statins, beta blockers, and ACE inhibitors.')
st.write('3. Medical procedures: Such as coronary angioplasty with stents or heart bypass surgery.')

st.subheader('Prevention of coronary heart disease:')
st.write('1. Healthy living: By controlling risk factors such as smoking, blood pressure, cholesterol and diabetes.')
st.write('2. Healthy diet: Eat foods low in saturated fat, rich in fibre, and low in salt.')
st.write('3. Regular exercise: At least 30 minutes a day, most days of the week.')

st.write('---')
st.subheader('Please predict your coronary heart disease below: ')


# input for name
name = st.text_input("Enter your name:")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', help='Input your age')
with col2:
    sex_mapping = {"Male": 1, "Female": 0}
    sex = st.selectbox("Select your gender:", options=list(sex_mapping.keys()), help='Select your gender')
    # Mapping selected sex to binary value
    sex_binary = sex_mapping[sex]
with col3:
    cp_mapping = {"Typical angina": 0, "Atypical angina": 1, "Non-anginal pain": 2, "Asymptomatic": 3}
    cp = st.selectbox('Chest pain Type:', options=list(cp_mapping.keys()), help='Typical Angina defined as substernal Chest Pain caused by physical exertion or emotional stress. Atypical Angina is a Symptom that is similar with Typical Angina but these symptoms may include chest pain that is milders, inconsistent or occurs in unusual Situations. Non Anginal Pain, is a symptom that is not caused by narrowing of the coronary Blood Vessels or Cardialischaemia and caused by other issues such as muscle, cartilage or digestive problems not always related to physical activity and stress.')
    # Mapping selected cp to binary value
    cp_binary = cp_mapping[cp]
with col1:
    trestbps = st.number_input('Trestbps', help='Resting Blood Pressure (in mm Hg on admission to the hospital)')
with col2:
    chol = st.number_input('Cholesterol', help='serum cholestoral in mg/dl')
with col3:
    fbs_mapping = {"True": 1, "False": 0}
    fbs = st.selectbox('Fasting Blood Sugar', options=list(fbs_mapping.keys()), help='fasting blood sugar > 120 mg/dl')
    # Mapping selected fbs to binary value
    fbs_binary = fbs_mapping[fbs]
with col1:
    restecg_mapping = {"Normal": 0, "ST-T wave abnormality": 1, "Definite left ventricular hypertrophy": 2}
    restecg = st.selectbox('Restecg:', options=list(restecg_mapping.keys()), help='Resting Electrocardiographic Results')
    # Mapping selected restecg to binary value
    restecg_binary = restecg_mapping[restecg]
with col2:
    thalach = st.number_input('Thalach', help='Maximum Heart Rate Achieved')
with col3:
    exang_mapping = {"Yes": 1, "No" : 0}
    exang = st.selectbox('Exang(Exercised Induced Angina)', options=list(exang_mapping.keys()), help='Condition where a person experiences chest pain or discomfort in the chest while exercising or performing certain physical activities')
    exang_binary = exang_mapping[exang]
with col1:
    oldpeak = st.number_input('Oldpeak', help='ST-Segment reduction on Electrocardiogram after physical training, compared while at rest.')
with col2:
    slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    slope = st.selectbox('Slope', options=list(slope_mapping.keys()), help='ST Segment on Electrocardiogram')
    slope_binary = slope_mapping[slope]
with col3:
    ca = st.number_input('CA Value', min_value=0, max_value=3, help='Number of major vessels (0-3) colored by flourosopy')
with col1:
    thal_mapping = {"Normal": 0, "Fixed Defect": 1, "Reversable Defect": 2}
    thal = st.selectbox('Thal', options=list(thal_mapping.keys()), help='Type of Thalassemia, a group of Blood Disorders characterised by abnormal production or low amounts of Haemoglobin')
    thal_binary = thal_mapping[thal]

# code for prediction
heart_diagnosis = ''

# Button prediction
if st.button('Prediction Coronary Heart Disease'):
    heart_prediction = model.predict([[age, sex_binary, cp_binary, trestbps, chol, fbs_binary, restecg_binary, thalach, exang_binary, oldpeak, slope_binary, ca, thal_binary]])

    if heart_prediction[0] == 1:
        bg_color = 'red'
        heart_diagnosis = 'have Coronary Heart Disease'
    else:
        bg_color = 'green'
        heart_diagnosis = 'does not have Coronary Heart Disease'

# display the prediction result with name
if heart_diagnosis:
    st.markdown(f'<p style="font-size: 24px; color: {bg_color};">{name}, {heart_diagnosis}</p>', unsafe_allow_html=True)
