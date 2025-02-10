# Bike-Sharing-Dataset
#### Repositori ini menampilkan hasil dari analisis data penyewaan sepeda, saya melakukan proses pengumpulan data, pembersihan data, EDA, dan membuat dashboard sederhana menggunakan streamlit 

#### Data ini membahas tentang tren penyewaan sepeda dari sebuah perusahaan yang memberikan jasa penyewaan sepeda dari tahun 2011 - 2013

# Untuk dapat menjalankan program analisis, pastikan sudah menginstall python 3.12 dengan library berikut:
- pandas
- matplotlib.pyplot
- seaborn
- numpy
## Untuk menginstal library yang dibutuhkan anda dapat menginstall nya dari requirements.txt file:
pip install -r requirements.txt


# Informasi yang didapatkan dari data tersebut:
- dari 4 musim, penyewaan terbanyak terjadi pada musim gugur, karena orang-orang menyukai pemandangan musim gugur, dan suhu yang pas untuk bersepeda
- Rata-rata penyewaan pada hari kerja: 4584.82
- Rata-rata penyewaan pada hari libur: 4330.168831168831
- Rata rata para pelanggan lebih menyukai bersepeda pada suhu hangat

# Dataset
- dateday: Tanggal pencatatan
- season: Musim (1 = semi, 2 = panas, 3 = gugur, 4 = dingin)
- yr: Tahun (0 = 2011, 1 = 2012)
- mnth: Bulan (1 = Januari, ..., 12 = Desember)
- holiday: Apakah hari tersebut hari libur (0 = tidak, 1 = ya)
- weekday: Hari dalam seminggu (0 = Minggu, 6 = Sabtu)
- workingday: Apakah hari kerja (0 = tidak, 1 = ya)
- weathersit: Kondisi cuaca (1 = cerah, 2 = mendung, 3 = hujan, 4 = badai)
- temp: Suhu normalisasi (0–1)
- atemp: Suhu yang dirasakan (0–1)
- hum: Kelembaban (0–1)
- windspeed: Kecepatan angin (0–1)
- casual: Jumlah penyewa sepeda non-terdaftar
- registered: Jumlah penyewa sepeda terdaftar
- cnt: Total jumlah penyewaan sepeda

# Running Dashboard
#### 1. git clone https://github.com/Rulai17/bike-sharing-dataset.git cd bike-sharing-dataset
#### 2. streamlit run dashboard.py
