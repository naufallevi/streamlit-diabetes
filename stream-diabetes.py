import pickle
import streamlit as st

# Load Model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Set up red background color and white text color
st.markdown(
    """
    <style>
    body {
        color: #FFFFFF; /* Warna teks diatur menjadi putih */
        background-color: #0000FF; /* Warna latar belakang diatur menjadi merah */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul dan deskripsi
st.title("Prediksi Data Mining Diabetes")
st.write(
    "Isi formulir di bawah ini dengan informasi pasien untuk melakukan prediksi apakah pasien terkena diabetes atau tidak."
)

# Membagi Kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input("Pregnancies / Kehamilan", min_value=0, max_value=17, value=0)

with col2:
    Glucose = st.number_input("Glucose / Glukosa", min_value=0, max_value=200, value=0)

with col1:
    BloodPressure = st.number_input("Blood Pressure / Tekanan Darah", min_value=0, max_value=122, value=0)

with col2:
    SkinThickness = st.number_input("Skin Thickness / Ketebalan Kulit", min_value=0, max_value=99, value=0)

with col1:
    Insulin = st.number_input("Insulin", min_value=0, max_value=846, value=0)

with col2:
    BMI = st.number_input("BMI", min_value=0.0, max_value=67.1, value=0.0)

with col1:
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function / Fungsi Silsilah Diabetes", min_value=0.078, max_value=2.42, value=0.078)

with col2:
    Age = st.number_input("Age / Usia", min_value=21, max_value=81, value=21)

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
