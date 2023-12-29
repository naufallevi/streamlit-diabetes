import pickle
import streamlit as st 

# Load Model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul
st.title("Prediksi Data Mining Diabetes")

# Membagi Kolom
col1, col2 =st.columns(2)

with col1:
    Pregnancies = st.text_input ("Input Nilai Pregnancies/ Kehamilan")

with col2:
    Glucose = st.text_input ("Input Nilai Glucose/ Glukosa")

with col1:
    BloodPressure = st.text_input ("Input Nilai Blood Pressure/ Tekanan Darah")

with col2:
    SkinThickness = st.text_input ("Input Nilai Skin Thickness/ Ketebalan Kulit")

with col1:
    Insulin = st.text_input ("Input Nilai Insulin")

with col2:
    BMI = st.text_input ("Input Nilai BMI")

with col1:
    DiabetesPedigreeFunction = st.text_input ("Input Nilai Diabetes Pedigree Function/ Fungsi Silsilah Diabetes")

with col2:
    Age = st.text_input ("Input Nilai Age/ Usia")

# Kode Prediksi

diab_diagnosis = ''

# Membuat Tombol Prediksi
if st.button('Test Prediksi'):
    diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,
                                               SkinThickness,Insulin,BMI,
                                               DiabetesPedigreeFunction,Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = "Pasien Terkena Diabetes"
    else:
        diab_diagnosis = "Pasien Tidak Terkena Diabetes"
    st.success(diab_diagnosis)