# LIDAR ve Kamera Destekli Otonom İç Mekan Robotu

Bu proje, iç mekanlarda, özellikle merdivenli binalarda etkin bir şekilde hareket edebilen altı tekerlekli bir robot geliştirmeyi amaçlamaktadır. Robot, zorlu iç mekân koşullarına uyum sağlayacak şekilde tasarlanmıştır ve otonom olarak çevresel engelleri algılayarak hareket edebilir.

## İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Özellikler](#özellikler)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Proje Hakkında

Bu proje, Marmara Üniversitesi Teknoloji Fakültesi Mekatronik Mühendisliği Bölümü öğrencileri tarafından hazırlanmıştır. Proje, özellikle kurtarma operasyonları ve tehlikeli ortamlarda insansız keşif gibi alanlarda büyük potansiyel taşımaktadır.

## Özellikler

- **LIDAR Tabanlı Haritalama**: Robot, el yapımı bir LIDAR ile donatılmıştır ve bu, bulunduğu ortamı tarayarak 3D haritalar oluşturmasını sağlar.
- **Görüntü İşleme**: Python ve OpenCV kullanılarak geliştirilen görüntü işleme algoritmaları, nesne tespiti ve çevresel farkındalık için kullanılır.
- **Otonom Navigasyon**: Robotun hareket algoritması, çevresel verileri kullanarak otonom navigasyonu optimize eder.
- **Merdiven Çıkabilme**: Robot, merdiven çıkma yeteneği ile çok katlı binalarda etkin bir şekilde hareket edebilir.

## Kullanılan Teknolojiler

- **Python**: Ana programlama dili olarak kullanılmıştır.
- **OpenCV**: Görüntü işleme için kullanılmıştır.
- **LIDAR**: Ortam taraması ve haritalama için kullanılmıştır.
- **Node.js & Socket.IO**: Kontrol arayüzü ve gerçek zamanlı iletişim için kullanılmıştır.
- **Arduino**: Motor kontrolü ve sensör entegrasyonu için kullanılmıştır.

## Kurulum

Projeyi yerel ortamınıza klonlayın:
```bash
git clone https://github.com/Yunsst/otonomrobot
cd otonomrobot
```

## Kullanım

- Arduino kartlarının COM portlarını kod içerisinden kontrol et.
- Raspberry üzerinde görüntü algılama fonksiyonunu çalıştır(mainFV2.cpp).
- moveP2P.py dosyasını çalıştır.
