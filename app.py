import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Modeli yükleme
#best_model = joblib.load('best_model.pkl')

# Veri ölçekleyici
scaler = StandardScaler()

st.title("Sigara İçme Durumunu Tahmin Etme Uygulaması")
st.write("Bu uygulama, biyolojik sinyalleri kullanarak bir bireyin sigara içme durumunu tahmin eder. Lütfen aşağıdaki formu doldurun:")

# Kullanıcıdan veri girişi
age = st.number_input("Yaş", min_value=5, max_value=100, step=1)
height = st.number_input("Boy (cm)", min_value=50, max_value=250, step=1)
weight = st.number_input("Kilo (kg)", min_value=10, max_value=300, step=1)
waist = st.number_input("Bel Çevresi (cm)", min_value=10, max_value=200, step=1)
eyesight_left = st.number_input("Görme (Sol)", min_value=0.0, max_value=2.0, step=0.1)
eyesight_right = st.number_input("Görme (Sağ)", min_value=0.0, max_value=2.0, step=0.1)
hearing_left = st.number_input("Duyma (Sol)", min_value=0, max_value=2, step=1)
hearing_right = st.number_input("Duyma (Sağ)", min_value=0, max_value=2, step=1)
systolic = st.number_input("Sistolik", min_value=50, max_value=250, step=1)
relaxation = st.number_input("Relaksasyon", min_value=30, max_value=150, step=1)
fasting_blood_sugar = st.number_input("Açlık Kan Şekeri", min_value=30, max_value=300, step=1)
cholesterol = st.number_input("Kolesterol", min_value=50, max_value=400, step=1)
triglyceride = st.number_input("Trigliserid", min_value=30, max_value=300, step=1)
hdl = st.number_input("HDL", min_value=10, max_value=100, step=1)
ldl = st.number_input("LDL", min_value=10, max_value=300, step=1)
hemoglobin = st.number_input("Hemoglobin", min_value=5.0, max_value=20.0, step=0.1)
urine_protein = st.number_input("İdrar Proteini", min_value=0, max_value=5, step=1)
serum_creatinine = st.number_input("Serum Kreatinin", min_value=0.1, max_value=10.0, step=0.1)
ast = st.number_input("AST", min_value=0, max_value=1000, step=1)
alt = st.number_input("ALT", min_value=0, max_value=1000, step=1)
gtp = st.number_input("GTP", min_value=0, max_value=1000, step=1)
dental_caries = st.number_input("Diş Çürüğü", min_value=0, max_value=1, step=1)

# Tahmin butonu
''' if st.button("Sigara İçme Durumunu Tahmin Et"):
    # Kullanıcıdan alınan verileri bir araya getirme
    user_data = np.array([age, height, weight, waist, eyesight_left, eyesight_right, hearing_left, hearing_right, 
                          systolic, relaxation, fasting_blood_sugar, cholesterol, triglyceride, hdl, ldl, 
                          hemoglobin, urine_protein, serum_creatinine, ast, alt, gtp, dental_caries]).reshape(1, -1)
    
    # Veriyi ölçeklendirme
    user_data = scaler.fit_transform(user_data)
    
    # Tahmini yapma
    prediction = best_model.predict(user_data)
    
    # Tahmin sonucunu gösterme
    if prediction[0] == 1:
        st.write("Tahmin: Sigara içiyor 🚬")
    else:
        st.write("Tahmin: Sigara içmiyor 🚭")
'''
