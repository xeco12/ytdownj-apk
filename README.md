# YTDown APK - Kurulum Rehberi

## 📱 Proje Yapısı
```
ytdown_apk/
├── main.py              ← Ana Python/Kivy dosyası
├── buildozer.spec       ← APK ayarları
├── assets/
│   └── index.html       ← Tasarım HTML dosyası
└── .github/
    └── workflows/
        └── build.yml    ← Otomatik build (GitHub Actions)
```

---

## 🚀 ADIM ADIM APK YAPIMI

### 1. GitHub Hesabı Aç
→ https://github.com → Sign Up (ücretsiz)

### 2. Yeni Repository Oluştur
- "New repository" tıkla
- İsim: `ytdown-apk`
- Public seç
- "Create repository" tıkla

### 3. Dosyaları Termux'tan Yükle

Termux'ta şu komutları çalıştır:

```bash
# Git kur
pkg install git

# Klasörü oluştur
mkdir ytdown_apk && cd ytdown_apk

# Git başlat
git init
git config user.email "senin@email.com"
git config user.name "Adın"

# Dosyaları oluştur (sana verildi)
# main.py, buildozer.spec, assets/index.html
# .github/workflows/build.yml

# GitHub'a bağla (kendi repo adresin)
git remote add origin https://github.com/KULLANICI_ADIN/ytdown-apk.git

# Yükle
git add .
git commit -m "İlk yükleme - YTDown APK"
git push -u origin main
```

### 4. GitHub Actions Otomatik Build Başlar
- GitHub'da reponuza gidin
- "Actions" sekmesine tıklayın
- "Build YTDown APK" workflow'unu görürsünüz
- ~15-20 dakika bekleyin ⏳

### 5. APK'yı İndir
- Actions → En son build → "YTDown-APK" artifact
- ZIP indir → APK çıkar
- Telefonuna aktar ve kur!

---

## ⚙️ APK Ayarları (buildozer.spec)

| Ayar | Değer |
|------|-------|
| Paket adı | com.maneviyolculk.ytdown |
| Min Android | 5.0 (API 21) |
| Hedef Android | 14 (API 34) |
| Yönlendirme | Portre |

---

## 🔧 Sorun Giderme

**Build başarısız olursa:**
- Actions → Failed build → "build" step loglarına bak
- Hata mesajını bana gönder, düzeltirim

**APK kurulmuyor:**
- Telefon ayarları → Bilinmeyen kaynaklara izin ver
- Güvenlik → Uygulama kurulumuna izin ver
