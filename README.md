# 🌊 Sistem Pakar Mitigasi Bencana Aceh

Aplikasi web berbasis Python Flask untuk prediksi risiko banjir menggunakan logika proposisional dan tabel kebenaran.

## 📋 Deskripsi

Sistem ini mengimplementasikan formula logika matematika untuk memprediksi risiko banjir berdasarkan tiga variabel:
- **p**: Curah Hujan Tinggi (> 100mm/hari)
- **q**: Alih Fungsi Lahan Sawit (Deforestasi)
- **r**: Sungai Dangkal/Sempit (Drainase Buruk)

**Formula**: `S = p ∧ (q ∨ r)`

Dimana S adalah risiko banjir yang terjadi jika hujan tinggi DAN (lahan rusak ATAU drainase buruk).

## 🚀 Cara Menjalankan

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Jalankan Server

```bash
python web_app.py
```

### 3. Buka Browser

Akses aplikasi di: `http://localhost:5000`

## 📁 Struktur Proyek

```
web tabel kebenaran/
├── web_app.py          # Flask backend server
├── app.py              # CLI version (original)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface
└── README.md          # Dokumentasi
```

## 🔌 API Endpoints

### POST /api/calculate
Menghitung risiko banjir berdasarkan input variabel.

**Request Body:**
```json
{
  "p": true,
  "q": false,
  "r": true
}
```

**Response:**
```json
{
  "success": true,
  "p": true,
  "q": false,
  "r": true,
  "q_or_r": true,
  "result": true,
  "recommendation": {
    "icon": "fa-water",
    "color": "text-red-600",
    "title": "🚨 PERINGATAN BANJIR - DRAINASE BURUK",
    "text": "Hujan deras dengan sungai dangkal/sempit..."
  }
}
```

### GET /api/truth-table
Mendapatkan tabel kebenaran lengkap (8 kombinasi).

**Response:**
```json
{
  "success": true,
  "table": [
    {
      "p": false,
      "q": false,
      "r": false,
      "q_or_r": false,
      "result": false
    },
    ...
  ]
}
```

### GET /api/articles
Mendapatkan daftar artikel dan berita mitigasi bencana.

**Response:**
```json
{
  "success": true,
  "articles": [
    {
      "id": 1,
      "category": "Tips",
      "title": "Tips Mitigasi Banjir untuk Masyarakat Aceh",
      "excerpt": "Panduan lengkap untuk masyarakat...",
      "date": "2025-01-15",
      "image": "https://...",
      "image_alt": "...",
      "author": "BNPB Aceh"
    },
    ...
  ]
}
```

### GET /api/health
Health check endpoint.

## 🎯 Fitur

- ✅ **Interactive UI**: Toggle switches untuk mengubah variabel secara real-time
- ✅ **Python Backend**: Perhitungan logika dilakukan di server Python
- ✅ **Truth Table**: Visualisasi lengkap 8 kombinasi kemungkinan
- ✅ **Logic Trace**: Step-by-step perhitungan logika proposisional
- ✅ **Smart Recommendations**: Rekomendasi mitigasi spesifik untuk setiap kombinasi
- ✅ **Responsive Design**: Tampilan optimal di desktop dan mobile
- ✅ **Real-time Updates**: Hasil langsung tanpa reload halaman
- ✅ **Articles & News**: Section artikel dengan foto-foto tentang mitigasi bencana

## 🛠️ Teknologi

- **Backend**: Python 3, Flask, Flask-CORS
- **Frontend**: HTML5, Tailwind CSS, JavaScript (Vanilla)
- **Icons**: Font Awesome 6
- **Logic**: Propositional Logic (Boolean Algebra)

## 📊 Tabel Kebenaran

| p | q | r | q ∨ r | S = p ∧ (q ∨ r) |
|---|---|---|-------|-----------------|
| 0 | 0 | 0 |   0   |        0        |
| 0 | 0 | 1 |   1   |        0        |
| 0 | 1 | 0 |   1   |        0        |
| 0 | 1 | 1 |   1   |        0        |
| 1 | 0 | 0 |   0   |        0        |
| 1 | 0 | 1 |   1   |        1        |
| 1 | 1 | 0 |   1   |        1        |
| 1 | 1 | 1 |   1   |        1        |

## 👨‍💻 Developer

Proyek Akhir Universitas - Sistem Pakar Berbasis Logika Matematika

## 📝 Lisensi

© 2025 - Implementasi Logika Proposisional untuk Mitigasi Bencana