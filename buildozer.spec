[app]
# Uygulama bilgileri
title = YTDown
package.name = ytdown
package.domain = com.maneviyolculk

# Kaynak dosyalar
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# Versiyon
version = 1.0.0

# Gereksinimler
requirements = python3,kivy,pyjnius,android

# Yönlendirme (portre mod)
orientation = portrait

# Android izinleri
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,DOWNLOAD_WITHOUT_NOTIFICATION

# Android API seviyeleri
android.minapi = 21
android.sdk = 34 
android.accept_sdk_license = True
android.build_tools_version = 34.0.0
android.ndk = 25b
android.ndk_api = 21

# Tam ekran (status bar gizle)
android.fullscreen = 0

# Uygulama ikonları (assets klasöründe olmalı)
# icon.filename = %(source.dir)s/assets/icon.png
# presplash.filename = %(source.dir)s/assets/splash.png

# Uygulama teması (Material Design için)
android.manifest.intent_filters = 
android.add_src = 
android.gradle_dependencies = 

# Build modu
[buildozer]
log_level = 2
warn_on_root = 1
