
import streamlit as st
import pickle
import numpy as np

# تحميل النموذج
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Diagnosis of gestational diabetes")

preg = st.number_input("عدد مرات الحمل", 0)
glucose = st.number_input("مستوى الجلوكوز", 0)
bp = st.number_input("ضغط الدم", 0)
skin = st.number_input("سُمك الجلد", 0)
insulin = st.number_input("الإنسولين", 0)
bmi = st.number_input("BMI", 0.0)
dpf = st.number_input("DPF", 0.0)
age = st.number_input("العمر", 0)

if st.button("تشخيص"):
    data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    pred = model.predict(data)
    if pred[0] == 1:
        st.error("⚠️ احتمال الإصابة بسكر الحمل.")
    else:
        st.success("✅ لا يوجد احتمال.")
