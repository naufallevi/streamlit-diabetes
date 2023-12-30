import pickle
import streamlit as st

# Load Model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul dan deskripsi
st.title("Prediksi Data Mining Diabetes")
st.write(
    "Isi formulir di bawah ini dengan informasi pasien untuk melakukan prediksi apakah pasien terkena diabetes atau tidak."
)

# Membagi Kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input("Pregnancies / Kehamilan", value=0)

with col2:
    Glucose = st.number_input("Glucose / Glukosa", value=0)

with col1:
    BloodPressure = st.number_input("Blood Pressure / Tekanan Darah", value=0)

with col2:
    SkinThickness = st.number_input("Skin Thickness / Ketebalan Kulit", value=0)

with col1:
    Insulin = st.number_input("Insulin", value=0)

with col2:
    BMI = st.number_input("BMI", min_value=0.0, max_value=67.1, value=0.0)

with col1:
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function / Fungsi Silsilah Diabetes", value=0.000)

with col2:
    Age = st.number_input("Age / Usia", value=0)

# Kode Prediksi
diab_diagnosis = ''

# Membuat Tombol Prediksi
if st.button('Test Prediksi'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,
                                               SkinThickness, Insulin, BMI,
                                               DiabetesPedigreeFunction, Age]])

    if diab_prediction[0] == 1:
        diab_diagnosis = "Pasien Terkena Diabetes"
    else:
        diab_diagnosis = "Pasien Tidak Terkena Diabetes"
    st.success(diab_diagnosis)
