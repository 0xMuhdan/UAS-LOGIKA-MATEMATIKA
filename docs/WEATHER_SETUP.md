# 🌤️ Panduan Setup Fitur Cuaca

## 📋 Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Cara Mendapatkan API Key](#cara-mendapatkan-api-key)
3. [Konfigurasi](#konfigurasi)
4. [Fitur Cuaca](#fitur-cuaca)
5. [Troubleshooting](#troubleshooting)

## Pendahuluan

Fitur cuaca telah ditambahkan ke aplikasi Sistem Pakar Mitigasi Bencana Alam. Fitur ini menggunakan **OpenWeatherMap API** untuk menampilkan:
- Cuaca saat ini
- Prakiraan 5 hari
- Peringatan risiko banjir berdasarkan cuaca
- Tips mitigasi berdasarkan kondisi cuaca

## Cara Mendapatkan API Key

### Langkah 1: Daftar di OpenWeatherMap

1. Buka [https://openweathermap.org/api](https://openweathermap.org/api)
2. Klik tombol **"Sign Up"** atau **"Get API Key"**
3. Isi formulir pendaftaran:
   - Username
   - Email
   - Password
4. Verifikasi email Anda
5. Login ke akun Anda

### Langkah 2: Dapatkan API Key

1. Setelah login, buka halaman [API Keys](https://home.openweathermap.org/api_keys)
2. Anda akan melihat API key default yang sudah dibuat
3. Copy API key tersebut (format: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)
4. **GRATIS** - Limit: 1,000 calls/day, 60 calls/minute

### Langkah 3: Konfigurasi API Key

1. Buka file `.env` di root project
2. Paste API key Anda:
   ```
   OPENWEATHER_API_KEY=paste_api_key_anda_disini
   ```
3. Simpan file

**Contoh:**
```env
OPENWEATHER_API_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
DEFAULT_CITY=Banda Aceh
DEFAULT_LAT=5.5483
DEFAULT_LON=95.3238
```

## Konfigurasi

### File `.env`

```env
# OpenWeatherMap API Key
OPENWEATHER_API_KEY=your_api_key_here

# Lokasi default (Banda Aceh)
DEFAULT_CITY=Banda Aceh
DEFAULT_LAT=5.5483
DEFAULT_LON=95.3238
```

### Mengubah Lokasi Default

Anda bisa mengubah lokasi default dengan mengedit koordinat di file `.env`:

**Contoh untuk Jakarta:**
```env
DEFAULT_CITY=Jakarta
DEFAULT_LAT=-6.2088
DEFAULT_LON=106.8456
```

**Contoh untuk Medan:**
```env
DEFAULT_CITY=Medan
DEFAULT_LAT=3.5952
DEFAULT_LON=98.6722
```

## Fitur Cuaca

### 1. Cuaca Saat Ini
- Suhu (°C)
- Terasa seperti
- Kelembaban (%)
- Kecepatan angin (km/h)
- Curah hujan (mm)
- Jarak pandang (km)
- Tekanan udara (hPa)
- Waktu matahari terbit/terbenam

### 2. Prakiraan 5 Hari
- Suhu harian
- Kondisi cuaca
- Kelembaban
- Curah hujan

### 3. Peringatan Risiko Banjir
Sistem otomatis mendeteksi risiko banjir berdasarkan:
- **Risiko Tinggi**: Curah hujan > 50mm/jam ATAU Kelembaban > 90%
- **Risiko Sedang**: Curah hujan > 20mm/jam ATAU Kelembaban > 80%
- **Risiko Rendah**: Kondisi normal

### 4. Tips Mitigasi
Tips otomatis berdasarkan kondisi cuaca:
- Hujan lebat → Hindari daerah rawan banjir
- Kelembaban tinggi → Pantau drainase
- Angin kencang → Amankan barang di luar
- Cuaca baik → Periksa sistem drainase

### 5. Pencarian Kota
- Cari kota di seluruh dunia
- Gunakan lokasi saat ini (GPS)
- Refresh data cuaca

## Cara Menggunakan

### 1. Jalankan Aplikasi

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan server
python web_app_enhanced.py
```

### 2. Buka Browser
```
http://localhost:5000
```

### 3. Akses Tab Cuaca
1. Klik tab **"Cuaca"** di menu navigasi
2. Data cuaca Banda Aceh akan dimuat otomatis

### 4. Cari Kota Lain
1. Ketik nama kota di search box
2. Tekan Enter atau klik tombol "Cari"
3. Pilih kota dari daftar (jika ada multiple hasil)

### 5. Gunakan Lokasi Saat Ini
1. Klik tombol lokasi (ikon GPS)
2. Izinkan browser mengakses lokasi Anda
3. Data cuaca lokasi Anda akan dimuat

## Troubleshooting

### Error: "API key not configured"

**Solusi:**
1. Pastikan file `.env` ada di root project
2. Pastikan `OPENWEATHER_API_KEY` sudah diisi
3. Restart aplikasi Flask

### Error: "Failed to fetch weather data"

**Kemungkinan Penyebab:**
1. **API key tidak valid**
   - Cek API key di [dashboard OpenWeatherMap](https://home.openweathermap.org/api_keys)
   - API key baru butuh waktu ~10 menit untuk aktif

2. **Limit API tercapai**
   - Free tier: 1,000 calls/day
   - Tunggu 24 jam atau upgrade plan

3. **Koneksi internet bermasalah**
   - Cek koneksi internet Anda
   - Coba refresh halaman

### Error: "Kota tidak ditemukan"

**Solusi:**
1. Coba nama kota dalam bahasa Inggris
2. Gunakan nama kota yang lebih spesifik
3. Contoh: "Jakarta" bukan "DKI Jakarta"

### Data cuaca tidak update

**Solusi:**
1. Klik tombol "Refresh" di header cuaca
2. Hard refresh browser (Ctrl + F5)
3. Clear cache browser

## API Endpoints

### GET /api/weather
Mendapatkan data cuaca saat ini dan prakiraan

**Parameters:**
- `city` (optional): Nama kota
- `lat` (optional): Latitude
- `lon` (optional): Longitude

**Response:**
```json
{
  "success": true,
  "location": {
    "name": "Banda Aceh",
    "country": "ID",
    "lat": 5.5483,
    "lon": 95.3238
  },
  "current": {
    "temp": 28,
    "feels_like": 31,
    "humidity": 75,
    "wind_speed": 12.5,
    "rain_1h": 0,
    "description": "Berawan"
  },
  "forecast": [...],
  "flood_risk": {
    "level": "low",
    "message": "Kondisi cuaca normal"
  }
}
```

### GET /api/weather/search
Mencari kota berdasarkan nama

**Parameters:**
- `city` (required): Nama kota

**Response:**
```json
{
  "success": true,
  "cities": [
    {
      "name": "Jakarta",
      "country": "ID",
      "state": "Jakarta",
      "lat": -6.2088,
      "lon": 106.8456
    }
  ]
}
```

## Upgrade ke Plan Berbayar

Jika Anda membutuhkan lebih banyak API calls:

| Plan | Calls/day | Calls/minute | Harga |
|------|-----------|--------------|-------|
| Free | 1,000 | 60 | $0 |
| Startup | 100,000 | 600 | $40/month |
| Developer | 1,000,000 | 3,000 | $125/month |

Info lengkap: [https://openweathermap.org/price](https://openweathermap.org/price)

## Keamanan

⚠️ **PENTING:**
1. **Jangan commit file `.env`** ke Git
2. File `.env` sudah ada di `.gitignore`
3. Jangan share API key Anda
4. Regenerate API key jika bocor

## Support

Jika masih ada masalah:
1. Cek [OpenWeatherMap FAQ](https://openweathermap.org/faq)
2. Cek [OpenWeatherMap API Docs](https://openweathermap.org/api)
3. Contact support: [https://openweathermap.org/support](https://openweathermap.org/support)

## Changelog

### v2.0.0 - Weather Feature
- ✅ Integrasi OpenWeatherMap API
- ✅ Cuaca real-time
- ✅ Prakiraan 5 hari
- ✅ Deteksi risiko banjir
- ✅ Tips mitigasi berdasarkan cuaca
- ✅ Pencarian kota global
- ✅ Geolocation support
- ❌ Hapus section artikel

---

**Selamat menggunakan fitur cuaca! 🌤️**