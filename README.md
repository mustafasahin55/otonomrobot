# LiDAR ve Kamera Destekli Otonom İç Mekan Robotu

Bu proje, iç mekanlarda ve özellikle merdivenli binalarda etkili bir şekilde hareket edebilen altı tekerlekli otonom bir robot geliştirmeyi amaçlamaktadır. Robot, zorlu iç mekan koşullarına uyum sağlayacak şekilde tasarlanmış olup, LiDAR ve kamera sistemleri kullanarak çevresini algılayabilir, haritalandırabilir ve engelleri tanıyabilir. Merdiven çıkma yeteneği ve otonom navigasyon kabiliyeti ile kurtarma operasyonları ve tehlikeli ortamlarda insansız keşif gibi alanlarda kullanılabilir.

## İçindekiler

- [Proje Özellikleri](#proje-özellikleri)
- [Donanım Bileşenleri](#donanım-bileşenleri)
- [Yazılım Bileşenleri](#yazılım-bileşenleri)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)

## Proje Özellikleri

- **Merdiven Çıkma Yeteneği**: Rocker-Bogie süspansiyon sistemi sayesinde merdivenli alanlarda hareket edebilme kabiliyeti
- **Otonom Navigasyon**: LiDAR ve kamera verileri kullanarak çevreyi haritalandırma ve otonom olarak yol planlama
- **Nesne Tanıma**: YOLOv8 algoritması kullanarak çevredeki nesneleri tanıma ve sınıflandırma
- **Derinlik Algılama**: Depth Anything modeli ile kameradan derinlik tahmini
- **İç Mekan Haritalama**: El yapımı LiDAR ile 3D haritalar oluşturma
- **Kontrol Arayüzü**: Web tabanlı kullanıcı dostu kontrol paneli

## Donanım Bileşenleri

### Mekanik Tasarım
- 6 tekerlekli Rocker-Bogie süspansiyon sistemi
- 3B basılmış robot şasisi
- Servo motorlar ve DC motorlar

### Elektronik Bileşenler
- **Ana Kontrol Ünitesi**: Raspberry Pi 5
- **Motor Kontrol**: Arduino Mega
- **LiDAR Kontrol**: Arduino Uno
- **Sensörler**:
  - Özel tasarlanmış LiDAR sistemi (TOF400C sensörü ile)
  - Kamera
  - MPU6050 jiroskop ve ivmeölçer

## Yazılım Bileşenleri

### LiDAR ve Haritalama
- **LiDAR Tarama**: Arduino ile TOF sensörü kontrolü
- **SLAM Algoritması**: Eş zamanlı konum belirleme ve haritalama
- **Haritalandırma**: 2D/3D harita oluşturma ve görselleştirme

### Görüntü İşleme
- **Nesne Tanıma**: YOLOv8 algoritması ile gerçek zamanlı nesne tespiti
- **Derinlik Tahmini**: Depth Anything modeli ile mono kameradan derinlik algılama
- **Uzaklık Tahmini**: Görüntü işleme ile nesnelerin uzaklıklarını hesaplama

### Hareket Kontrolü
- **Yol Planlama**: Hybrid A* algoritması ile optimal yol planlama
- **Ackerman Sürüş**: Tekerleklerin uygun açı ve hızlarda kontrolü
- **Engel Algılama ve Kaçınma**: Sensör verilerine dayanarak dinamik engel kaçınma

### Kontrol Arayüzü
- **Web Tabanlı Arayüz**: Node.js ve Express.js ile geliştirilen kullanıcı arayüzü
- **Gerçek Zamanlı İletişim**: Socket.IO ile robot ve kontrol paneli arasında veri aktarımı
- **Harita Görselleştirme**: Oluşturulan haritanın web arayüzünde gösterimi

## Kurulum

### Donanım Kurulumu

1. Robot mekanik parçalarını 3B yazdırın ve birleştirin
2. Elektronik bileşenleri şemaya göre bağlayın:
   - Raspberry Pi 5'i ana kontrol ünitesi olarak kurun
   - Arduino Mega'yı motor kontrolör olarak bağlayın
   - Arduino Uno'yu LiDAR kontrol sistemi için bağlayın
   - Servo motorları ve DC motorları Arduino Mega'ya bağlayın
   - LiDAR sensörünü Arduino Uno'ya bağlayın
   - Kamera ve MPU6050 sensörünü Raspberry Pi'ye bağlayın

### Yazılım Kurulumu

1. Raspberry Pi 5'e gerekli işletim sistemini kurun:
```bash
# Raspberry Pi OS kurulumu ve güncelleme
sudo apt update
sudo apt upgrade
```

2. Gerekli Python kütüphanelerini yükleyin:
```bash
pip install numpy opencv-python torch torchvision socketio eventlet
pip install ultralyticsplus
```

3. Node.js ve npm kurulumu:
```bash
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt install -y nodejs
```

4. Proje klasörünü klonlayın:
```bash
git clone https://github.com/kullaniciadi/lidar-kamera-otonom-robot.git
cd lidar-kamera-otonom-robot
```

5. Web arayüzü için gerekli bağımlılıkları yükleyin:
```bash
cd web-interface
npm install
```

6. Arduino IDE'yi kurun ve gerekli kütüphaneleri ekleyin:
   - Servo Kütüphanesi
   - VL53L0X Kütüphanesi
   - MPU6050 Kütüphanesi

## Kullanım

### Robot Başlatma

1. Tüm sistemleri açın ve güç kaynağını bağlayın
2. Raspberry üzerinde görüntü algılama fonksiyonunu çalıştır.

```bash
cd /path/to/project/otonomrobot
gcc mainFV2.cpp
```

3. Raspberry Pi üzerinde ana kontrol yazılımını başlatın:
```bash
cd /path/to/project/otonomrobot
python mainP2P.py
```

4. Web arayüzünü başlatın:
```bash
cd /path/to/project/web-interface
npm start
```

5. Tarayıcınızda arayüze erişin:
```
http://[raspberry-pi-ip]:3000
```

### Kontrol Arayüzü Kullanımı

1. **LiDAR Tarama**: Arayüzdeki "LiDAR Tarama" butonuna tıklayarak çevrenin haritasını oluşturun
2. **Otonom Navigasyon**: Harita üzerinde gidilecek hedef noktayı seçin ve "Hedefe Git" butonuna tıklayın
3. **Manuel Kontrol**: Manuel sürüş modunu seçerek robotu doğrudan kontrol edin
4. **Acil Durdurma**: Herhangi bir acil durumda "Acil Durdurma" butonunu kullanın

## Sistem Mimarisi

```
+-------------------+      +-------------------+      +-------------------+
|   Raspberry Pi 5  ||    Arduino Mega   ||    DC Motorlar    |
|                   |      |                   |      |    Servo Motorlar  |
|  - Ana Kontrol    |      |  - Motor Kontrol  |      +-------------------+
|  - SLAM           |      |  - Ackerman Sürüş |
|  - YOLOv8         |      |  - MPU6050 Okuma  |
|  - Depth Anything |      +-------------------+
|  - Web Sunucu     |
+--------^----------+
         |
         v
+-------------------+      +-------------------+
|    Arduino Uno    ||   LiDAR Sistemi   |
|                   |      |   (TOF Sensörü)   |
|  - LiDAR Kontrol  |      |                   |
+-------------------+      +-------------------+
```
## 3D Model
![image](https://github.com/user-attachments/assets/b2b7dca7-3083-4412-bb6d-6994e481c99b)

## Prototip

![image](https://github.com/user-attachments/assets/fc917fcd-366a-431f-afd7-736e6079458f)


## Lisans

Bu proje eğitim amaçlı geliştirilmiş olup Marmara Üniversitesi Teknoloji Fakültesi Mekatronik Mühendisliği bölümü bitirme projesi kapsamında yapılmıştır.

---

*Not: Bu README dosyası, projeyi ve çalışma mantığını genel olarak açıklamaktadır. Daha detaylı teknik bilgiler için lütfen kod dosyalarını ve açıklamalarını inceleyiniz.*
