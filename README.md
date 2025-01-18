Streamlit App: Analisis Dataset dan Prediksi Machine Learning
Proyek ini merupakan aplikasi berbasis Streamlit untuk menganalisis dataset, melakukan pemilihan fitur dan label, melatih model menggunakan algoritma Random Forest Classifier, dan melakukan prediksi berdasarkan data baru yang diberikan oleh pengguna.

Fitur Aplikasi
Upload Dataset:

Pengguna dapat mengunggah file dataset berformat .csv.
Dataset akan ditampilkan dalam bentuk tabel.
Eksplorasi Dataset:

Menampilkan informasi dimensi dataset.
Menyediakan statistik deskriptif dataset.
Penanganan Missing Values:

Pilihan untuk menghapus baris dengan nilai kosong atau mengganti nilai kosong dengan rata-rata.
Pemilihan Fitur dan Label:

Pengguna dapat memilih kolom sebagai fitur (X) dan kolom sebagai label (y) dari dataset.
Split Dataset:

Dataset dapat dibagi menjadi data latih dan data uji menggunakan slider untuk mengatur ukuran data uji.
Pelatihan Model:

Melatih model Random Forest Classifier menggunakan data latih.
Menampilkan akurasi model dan laporan klasifikasi.
Visualisasi Pentingnya Fitur:

Menampilkan grafik batang yang menunjukkan pentingnya fitur yang dipilih.
Prediksi Data Baru:

Pengguna dapat memasukkan nilai baru untuk fitur yang dipilih, dan model akan memberikan hasil prediksi.
Teknologi yang Digunakan
Python (Bahasa Pemrograman)
Streamlit (Framework untuk aplikasi berbasis web)
Pandas (Analisis data)
NumPy (Komputasi numerik)
Matplotlib (Visualisasi data)
scikit-learn (Library Machine Learning)
Cara Menjalankan Aplikasi
1. Prasyarat
Pastikan Anda memiliki Python 3.8+ di komputer Anda.
Install library yang dibutuhkan dengan menjalankan perintah berikut:
bash
Salin
Edit
pip install streamlit pandas numpy matplotlib scikit-learn
2. Menjalankan Aplikasi
Simpan kode aplikasi di file Python, misalnya app.py.
Jalankan aplikasi dengan perintah:
bash
Salin
Edit
streamlit run app.py
Aplikasi akan terbuka di browser secara otomatis di alamat: http://localhost:8501.
Struktur Input
Dataset
Dataset harus dalam format .csv dengan kolom yang mewakili fitur dan label. Pastikan dataset tidak memiliki nilai kosong atau gunakan fitur yang tersedia untuk menangani missing values.

Prediksi Data Baru
Masukkan nilai untuk setiap fitur yang dipilih sebelum menekan tombol Prediksi.

Contoh Dataset
Berikut adalah contoh dataset sederhana (simpan sebagai data.csv):

csv
Edit
Age,Salary,Purchased
22,20000,0
25,35000,0
30,40000,1
35,60000,1
40,80000,1
Fitur Tambahan
Penanganan otomatis untuk nilai kosong.
Visualisasi dataset dengan histogram.
Sidebar untuk navigasi pengaturan aplikasi.
Deployment
https://a11202214733.streamlit.app/
Kontributor
Dibuat oleh:

Helmi azkia
Proyek ini dibuat untuk keperluan Ujian Akhir Semester mata kuliah Data Mining.
