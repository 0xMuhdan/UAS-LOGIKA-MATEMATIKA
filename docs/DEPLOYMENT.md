# 🚀 Panduan Deployment

Panduan lengkap untuk deploy aplikasi Sistem Pakar Mitigasi Bencana Aceh ke berbagai platform.

## 📋 Prerequisites

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Git (untuk version control)

## 🏠 Local Development

### 1. Clone Repository
```bash
git clone <repository-url>
cd "web tabel kebenaran"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Development Server
```bash
python web_app.py
```

Aplikasi akan berjalan di: `http://localhost:5000`

## ☁️ Deployment ke Cloud

### Option 1: Heroku

#### Step 1: Install Heroku CLI
```bash
# Download dari https://devcenter.heroku.com/articles/heroku-cli
```

#### Step 2: Login ke Heroku
```bash
heroku login
```

#### Step 3: Create Heroku App
```bash
heroku create nama-app-anda
```

#### Step 4: Buat Procfile
```bash
echo "web: python web_app.py" > Procfile
```

#### Step 5: Update web_app.py untuk Production
Ubah baris terakhir di `web_app.py`:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```

#### Step 6: Deploy
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

#### Step 7: Open App
```bash
heroku open
```

### Option 2: Railway

#### Step 1: Create Account
Buat akun di [railway.app](https://railway.app)

#### Step 2: New Project
- Klik "New Project"
- Pilih "Deploy from GitHub repo"
- Connect repository Anda

#### Step 3: Configure
Railway akan otomatis detect Python dan install dependencies.

#### Step 4: Environment Variables (Optional)
Tambahkan environment variables jika diperlukan.

### Option 3: Render

#### Step 1: Create Account
Buat akun di [render.com](https://render.com)

#### Step 2: New Web Service
- Klik "New +"
- Pilih "Web Service"
- Connect GitHub repository

#### Step 3: Configure Build
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python web_app.py`

#### Step 4: Deploy
Klik "Create Web Service"

### Option 4: PythonAnywhere

#### Step 1: Create Account
Buat akun di [pythonanywhere.com](https://www.pythonanywhere.com)

#### Step 2: Upload Files
Upload semua file project via Files tab

#### Step 3: Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.8 myenv
pip install -r requirements.txt
```

#### Step 4: Configure Web App
- Buka Web tab
- Add new web app
- Pilih Flask
- Set path ke web_app.py

#### Step 5: Reload
Klik "Reload" untuk apply changes

## 🐳 Docker Deployment

### Step 1: Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "web_app.py"]
```

### Step 2: Build Image
```bash
docker build -t sistem-pakar-bencana .
```

### Step 3: Run Container
```bash
docker run -p 5000:5000 sistem-pakar-bencana
```

### Step 4: Deploy ke Docker Hub (Optional)
```bash
docker tag sistem-pakar-bencana username/sistem-pakar-bencana
docker push username/sistem-pakar-bencana
```

## 🌐 VPS Deployment (Ubuntu)

### Step 1: Connect to VPS
```bash
ssh user@your-vps-ip
```

### Step 2: Install Dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip nginx
```

### Step 3: Clone Repository
```bash
git clone <repository-url>
cd "web tabel kebenaran"
```

### Step 4: Install Python Packages
```bash
pip3 install -r requirements.txt
```

### Step 5: Install Gunicorn
```bash
pip3 install gunicorn
```

### Step 6: Create Systemd Service
```bash
sudo nano /etc/systemd/system/sistem-pakar.service
```

Isi file:
```ini
[Unit]
Description=Sistem Pakar Mitigasi Bencana
After=network.target

[Service]
User=your-username
WorkingDirectory=/path/to/web tabel kebenaran
ExecStart=/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:5000 web_app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

### Step 7: Start Service
```bash
sudo systemctl start sistem-pakar
sudo systemctl enable sistem-pakar
```

### Step 8: Configure Nginx
```bash
sudo nano /etc/nginx/sites-available/sistem-pakar
```

Isi file:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Step 9: Enable Site
```bash
sudo ln -s /etc/nginx/sites-available/sistem-pakar /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 🔒 SSL Certificate (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## 📊 Monitoring & Maintenance

### Check Application Status
```bash
sudo systemctl status sistem-pakar
```

### View Logs
```bash
sudo journalctl -u sistem-pakar -f
```

### Restart Application
```bash
sudo systemctl restart sistem-pakar
```

## 🔧 Environment Variables

Untuk production, set environment variables:

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key-here
```

Atau buat file `.env`:
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

## ✅ Post-Deployment Checklist

- [ ] Test semua endpoints API
- [ ] Verify database connections (jika ada)
- [ ] Check error logging
- [ ] Test responsive design di berbagai devices
- [ ] Verify SSL certificate
- [ ] Setup monitoring (Sentry, New Relic, etc.)
- [ ] Configure backups
- [ ] Setup CI/CD pipeline (optional)
- [ ] Update DNS records
- [ ] Test performance dengan load testing

## 📞 Support

Jika ada masalah deployment, check:
1. Application logs
2. Server logs
3. Network connectivity
4. Port availability
5. File permissions

---

**Happy Deploying! 🚀**