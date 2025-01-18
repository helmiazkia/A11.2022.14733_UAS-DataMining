import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Judul Aplikasi
st.title("Analisis Dataset dan Prediksi dengan Machine Learning")
st.write("Projek Data mining UAS")

# Sidebar untuk Upload Dataset
with st.sidebar:
    st.header("Pengaturan")
    uploaded_file = st.file_uploader("Pilih file dataset (format .csv)", type=["csv"])

if uploaded_file is not None:
    # Membaca dataset
    df = pd.read_csv(uploaded_file)
    st.write("Dataset berhasil diupload:")
    st.dataframe(df)

    # Penanganan Missing Values
    if df.isnull().values.any():
        st.warning("Dataset mengandung nilai kosong.")
        imputation_method = st.radio("Pilih metode penanganan NaN:", ["Drop rows", "Fill with mean"])
        if imputation_method == "Drop rows":
            df = df.dropna()
        elif imputation_method == "Fill with mean":
            df = df.fillna(df.mean())
        st.write("Dataset setelah penanganan nilai kosong:")
        st.dataframe(df)

    # Eksplorasi Dataset
    st.subheader("Informasi Dataset")
    st.write("Dimensi Dataset:", df.shape)
    st.write("Statistik Deskriptif:")
    st.write(df.describe())

    # Memilih Fitur dan Label
    numeric_columns = df.select_dtypes(include=np.number).columns
    st.subheader("Pemilihan Fitur dan Label")
    features = st.multiselect("Pilih Kolom Fitur (hanya numerik)", options=numeric_columns)
    label = st.selectbox("Pilih Kolom Label", options=df.columns)

    if len(features) > 0 and label:
        X = df[features]
        y = df[label]

        # Split Data
        st.subheader("Split Dataset")
        test_size = st.slider("Pilih ukuran data uji (persentase)", 0.1, 0.5, 0.2)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

        st.write("Jumlah data latih:", X_train.shape[0])
        st.write("Jumlah data uji:", X_test.shape[0])

        # Training Model
        st.subheader("Training Model")
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Evaluasi Model
        st.subheader("Hasil Evaluasi Model")
        acc = accuracy_score(y_test, y_pred)
        st.write("Akurasi Model:", acc)
        st.text("Classification Report:")
        st.text(classification_report(y_test, y_pred))

        # Visualisasi Pentingnya Fitur
        st.subheader("Pentingnya Fitur")
        feature_importances = pd.DataFrame({
            'Feature': features,
            'Importance': model.feature_importances_
        }).sort_values(by="Importance", ascending=False)
        st.bar_chart(feature_importances.set_index('Feature'))

        # Prediksi Data Baru
        st.subheader("Prediksi Data Baru")
        input_data = {}
        for feature in features:
            input_data[feature] = st.number_input(f"Masukkan nilai untuk {feature}")

        if st.button("Prediksi"):
            if all(value is not None for value in input_data.values()):
                input_df = pd.DataFrame([input_data])
                prediction = model.predict(input_df)
                st.write("Hasil Prediksi:", prediction[0])
            else:
                st.error("Harap isi semua nilai input.")

else:
    st.write("Silakan upload dataset untuk memulai.")
