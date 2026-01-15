# 📖 Panduan Penggunaan Sistem Pakar Mitigasi Bencana Aceh

## 🎯 Cara Menggunakan Aplikasi Web

### 1. Menjalankan Server

```bash
# Install dependencies (hanya sekali)
py -m pip install -r requirements.txt

# Jalankan server
py web_app.py
```

Server akan berjalan di: **http://localhost:5000**

### 2. Menggunakan Interface Web

#### Panel Kontrol Variabel (Kiri)
Gunakan toggle switch untuk mengatur kondisi:

- **p (Curah Hujan Tinggi)**: ON = Hujan deras (>100mm/hari), OFF = Tidak hujan
- **q (Alih Fungsi Lahan Sawit)**: ON = Ada deforestasi, OFF = Hutan terjaga
- **r (Sungai Dangkal/Sempit)**: ON = Drainase buruk, OFF = Sungai lancar

#### Panel Visualisasi (Kanan)
Menampilkan hasil perhitungan secara real-time:

1. **Formula Logika**: Menampilkan formula `S = p ∧ (q ∨ r)`
2. **Trace Perhitungan**: Step-by-step evaluasi logika dari Python backend
3. **Status Card**: Indikator visual risiko banjir
   - 🟢 Hijau = KONDISI AMAN
   - 🔴 Merah = PERINGATAN BANJIR (animasi pulse)
4. **Rekomendasi Mitigasi**: Saran tindakan spesifik berdasarkan kombinasi input

#### Section Artikel & Berita
Menampilkan artikel dan berita terkini tentang mitigasi bencana:
- **6 Artikel** dengan foto-foto berkualitas tinggi
- **Kategori**: Tips, Teknologi, Lingkungan, Infrastruktur, Kesiapsiagaan, Edukasi
- **Informasi**: Judul, tanggal, penulis, dan ringkasan artikel
- **Responsive**: Layout grid yang menyesuaikan dengan ukuran layar

Topik artikel meliputi:
1. Tips mitigasi banjir untuk masyarakat
2. Sistem peringatan dini bencana
3. Program reboisasi hutan
4. Normalisasi sungai dan drainase
5. Kesiapsiagaan menghadapi musim hujan
6. Pelatihan tanggap darurat untuk relawan

#### Tabel Kebenaran
- Menampilkan semua 8 kombinasi kemungkinan
- Baris yang sesuai dengan input saat ini akan **di-highlight kuning**
- Scroll otomatis ke baris yang aktif

## 🧪 Contoh Skenario

### Skenario 1: Kondisi Ideal ✅
- p = OFF (Tidak hujan)
- q = OFF (Hutan terjaga)
- r = OFF (Sungai lancar)
- **Hasil**: KONDISI AMAN

### Skenario 2: Peringatan Banjir 🚨
- p = ON (Hujan deras)
- q = OFF (Hutan terjaga)
- r = ON (Sungai dangkal)
- **Hasil**: PERINGATAN BANJIR - DRAINASE BURUK

### Skenario 3: Bahaya Maksimal 🔴
- p = ON (Hujan deras)
- q = ON (Deforestasi)
- r = ON (Sungai dangkal)
- **Hasil**: BAHAYA MAKSIMAL - EVAKUASI DARURAT

## 🔧 Troubleshooting

### Server tidak bisa dijalankan
```bash
# Pastikan Python terinstall
py --version

# Install ulang dependencies
py -m pip install --upgrade -r requirements.txt
```

### Port 5000 sudah digunakan
Edit `web_app.py` baris terakhir:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Ganti port
```

### Browser tidak bisa akses
- Pastikan firewall tidak memblokir port 5000
- Coba akses: `http://127.0.0.1:5000` atau `http://192.168.x.x:5000`

## 📱 Akses dari Perangkat Lain

Jika ingin akses dari HP/tablet di jaringan yang sama:
1. Lihat IP address komputer server di output terminal
2. Buka browser di perangkat lain
3. Akses: `http://[IP_ADDRESS]:5000`

Contoh: `http://192.168.100.19:5000`

## 🎓 Penjelasan Logika

### Formula: S = p ∧ (q ∨ r)

**Langkah Evaluasi:**
1. Evaluasi `(q ∨ r)` → Cek apakah lahan rusak ATAU sungai buruk
2. Evaluasi `p ∧ (hasil step 1)` → Cek apakah hujan DAN step 1 TRUE
3. Jika hasil = TRUE → Risiko banjir terdeteksi

**Tabel Kebenaran:**
- Banjir terjadi pada 3 dari 8 kombinasi
- Kombinasi berbahaya: (1,0,1), (1,1,0), (1,1,1)
- Kombinasi aman: 5 kombinasi lainnya

## 💡 Tips Penggunaan

1. **Real-time Update**: Setiap perubahan toggle langsung menghitung ulang
2. **Scroll Otomatis**: Tabel kebenaran akan scroll ke baris yang aktif
3. **Visual Feedback**: Perhatikan animasi pulse pada status bahaya
4. **Python Backend**: Semua perhitungan dilakukan di server Python

## 📞 Support

Jika ada pertanyaan atau masalah:
- Cek console browser (F12) untuk error JavaScript
- Cek terminal server untuk error Python
- Pastikan semua dependencies terinstall dengan benar