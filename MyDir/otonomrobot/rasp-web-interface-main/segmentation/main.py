import cv2
from ultralytics import YOLO

# YOLOv8 segmentasyon modeli yükleniyor
model = YOLO('yolov8n-seg.pt')

# Kameradan video akışı başlatılıyor
cap = cv2.VideoCapture(0)  # 0, varsayılan kamera anlamına gelir. Farklı bir kamera kullanmak isterseniz, doğru kamera indeksini girin.

# Video akışı boyunca her kareyi işleme
while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı.")
        break
    
    # Segmentasyon işlemi gerçekleştiriliyor
    results = model.predict(source=frame, save=False)  # save=False, çıktıları dosyaya kaydetmemek için

    # Sonuçları görüntüye çizme
    annotated_frame = results[0].plot()  # İlk sonuç için anotasyonları çizer

    # Sonuçları gösterme
    cv2.imshow('Segmentasyon', annotated_frame)
    
    # 'q' tuşuna basarak döngüyü sonlandırma
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera ve pencereleri serbest bırakma
cap.release()
cv2.destroyAllWindows()

