# 🌤️ Fitur Cuaca - Sistem Pakar Mitigasi Bencana

## 🎯 Ringkasan Perubahan

Artikel section telah dihapus dan diganti dengan **Fitur Cuaca Real-time** yang terintegrasi dengan OpenWeatherMap API.

## ✨ Fitur Baru

### 1. Cuaca Real-time
- Suhu saat ini dengan feels-like temperature
- Kelembaban udara
- Kecepatan angin
- Curah hujan
- Jarak pandang
- Tekanan udara
- Waktu sunrise/sunset

### 2. Prakiraan 5 Hari
- Prakiraan cuaca harian
- Suhu min/max
- Kondisi cuaca
- Probabilitas hujan

### 3. Peringatan Risiko Banjir
- **Otomatis mendeteksi** risiko banjir berdasarkan:
  - Curah hujan tinggi (> 50mm/jam)
  - Kelembaban ekstrem (> 90%)
- Alert visual dengan warna:
  - 🔴 Merah = Risiko Tinggi
  - 🟡 Kuning = Risiko Sedang
  - 🟢 Hijau = Aman

### 4. Tips Mitigasi Dinamis
Tips yang menyesuaikan dengan kondisi cuaca:
- Hujan lebat → Evakuasi darurat
- Kelembaban tinggi → Pantau drainase
- Angin kencang → Amankan properti
- Cuaca baik → Maintenance preventif

### 5. Pencarian Kota
- Cari cuaca kota manapun di dunia
- Auto-complete suggestions
- Gunakan GPS untuk lokasi saat ini

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Dapatkan API Key GRATIS
1. Daftar di [OpenWeatherMap](https://openweathermap.org/api)
2. Verifikasi email
3. Copy API key dari dashboard

### 3. Setup Environment
```bash
# Copy example file
cp .env.example .env

# Edit .env dan paste API key Anda
# OPENWEATHER_API_KEY=your_api_key_here
```

### 4. Jalankan Aplikasi
```bash
python web_app_enhanced.py
```

### 5. Buka Browser
```
http://localhost:5000
```

### 6. Akses Tab Cuaca
Klik tab **"Cuaca"** di navigasi atas

## 📸 Screenshot

### Cuaca Saat Ini
```
┌─────────────────────────────────────────┐
│ 🌤️ Banda Aceh, ID                      │
│ Diperbarui: 2025-01-13 10:30:00        │
│                                         │
│ 28°C  ☁️                               │
│ Berawan sebagian                        │
│ Terasa seperti 31°C                     │
│                                         │
│ 💧 75%  💨 12.5 km/h  🌧️ 0mm          │
└─────────────────────────────────────────┘
```

### Peringatan Banjir
```
┌─────────────────────────────────────────┐
│ ⚠️ PERINGATAN RISIKO BANJIR TINGGI     │
│                                         │
│ Curah hujan tinggi (52mm/jam).          │
│ Waspada potensi banjir!                 │
└─────────────────────────────────────────┘
```

## 🔧 Konfigurasi

### Lokasi Default
Edit `.env` untuk mengubah lokasi default:

```env
# Jakarta
DEFAULT_CITY=Jakarta
DEFAULT_LAT=-6.2088
DEFAULT_LON=106.8456

# Medan
DEFAULT_CITY=Medan
DEFAULT_LAT=3.5952
DEFAULT_LON=98.6722

# Surabaya
DEFAULT_CITY=Surabaya
DEFAULT_LAT=-7.2575
DEFAULT_LON=112.7521
```

## 📊 API Endpoints

### GET /api/weather
Mendapatkan data cuaca

**Query Parameters:**
- `city` (optional): Nama kota
- `lat` (optional): Latitude  
- `lon` (optional): Longitude

**Example:**
```bash
curl "http://localhost:5000/api/weather?city=Jakarta"
```

### GET /api/weather/search
Mencari kota

**Query Parameters:**
- `city` (required): Nama kota

**Example:**
```bash
curl "http://localhost:5000/api/weather/search?city=Jakarta"
```

## 🎨 UI/UX Features

### Responsive Design
- ✅ Desktop (3 kolom forecast)
- ✅ Tablet (2 kolom forecast)
- ✅ Mobile (1 kolom forecast)

### Interactive Elements
- 🔄 Refresh button
- 🔍 City search dengan autocomplete
- 📍 Geolocation button
- 💡 Dynamic tips

### Visual Indicators
- 🌡️ Temperature dengan color coding
- 💧 Humidity dengan progress bar
- 🌧️ Rainfall dengan icon
- ⚠️ Alert banners untuk risiko tinggi

## 🐛 Troubleshooting

### API Key Error
```
Error: API key not configured
```
**Solusi:** Pastikan `OPENWEATHER_API_KEY` ada di file `.env`

### Rate Limit
```
Error: Too many requests
```
**Solusi:** Free tier limit 1,000 calls/day. Tunggu atau upgrade.

### Kota Tidak Ditemukan
```
Error: Kota tidak ditemukan
```
**Solusi:** Gunakan nama kota dalam bahasa Inggris

## 📝 Perubahan dari Versi Sebelumnya

### ❌ Dihapus
- Section Artikel & Berita
- API endpoint `/api/articles`
- Function `get_articles()`
- Function `loadArticles()`
- Function `createArticleCard()`

### ✅ Ditambahkan
- Tab Cuaca
- API endpoint `/api/weather`
- API endpoint `/api/weather/search`
- Function `get_weather_data()`
- Function `loadWeather()`
- Function `displayWeather()`
- Function `searchCity()`
- Function `useCurrentLocation()`
- Dependency: `requests`
- Dependency: `python-dotenv`

## 🔐 Keamanan

⚠️ **PENTING:**
1. File `.env` sudah ada di `.gitignore`
2. Jangan commit API key ke repository
3. Jangan share API key secara publik
4. Regenerate API key jika bocor

## 📚 Dokumentasi Lengkap

Lihat [WEATHER_SETUP.md](WEATHER_SETUP.md) untuk:
- Panduan lengkap setup
- Troubleshooting detail
- API documentation
- Best practices

## 🎯 Integrasi dengan Sistem Pakar

Fitur cuaca terintegrasi dengan sistem pakar banjir:

1. **Input Otomatis**: Curah hujan dari weather API bisa digunakan sebagai input variabel `p` (Curah Hujan Tinggi)

2. **Validasi Real-time**: Bandingkan prediksi sistem dengan kondisi cuaca aktual

3. **Early Warning**: Kombinasi prediksi logika + data cuaca real-time = sistem peringatan dini yang lebih akurat

## 🌟 Fitur Mendatang

- [ ] Historical weather data
- [ ] Weather alerts dari BMKG
- [ ] Integrasi dengan sistem pakar (auto-input)
- [ ] Export weather reports
- [ ] Weather statistics dashboard

## 💬 Support

Jika ada pertanyaan atau masalah:
1. Baca [WEATHER_SETUP.md](WEATHER_SETUP.md)
2. Check [OpenWeatherMap Docs](https://openweathermap.org/api)
3. Create issue di repository

---

**Developed with ❤️ for better disaster mitigation**