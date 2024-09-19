import cv2
import numpy as np

# Renk aralığı (örnek olarak mavi renk)
lower_color = np.array([90, 50, 50])
upper_color = np.array([130, 255, 255])

def color_thresholding(frame):
    # Görüntüyü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Belirtilen renk aralığında maske oluştur
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    return mask

def find_objects(mask):
    # Konturları bulma
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    objects = []
    for contour in contours:
        # Konturun sınırlayıcı kutusunu al
        x, y, w, h = cv2.boundingRect(contour)
        
        # Alanı küçük olan konturları filtrele (gürültüyü azaltmak için)
        area = cv2.contourArea(contour)
        if area > min_area_threshold:
            objects.append((x, y, w, h))
    
    return objects

def detect_obstacles(objects, frame_width, frame_height, frame):
    for obj in objects:
        x, y, w, h = obj
        
        # Örneğin, belirli bir boyut sınırı ile engel kontrolü yapabiliriz
        if w > min_obstacle_width and h > min_obstacle_height:
            # Engelin olduğunu belirt
            print(f"Engel algılandı: x={x}, y={y}, width={w}, height={h}")
            
            # Engel konumu ve boyutunu görsel olarak işaretleme
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

def main():
    # Kamera başlat
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera açılamadı.")
        return

    while True:
        # Görüntü yakalama
        ret, frame = cap.read()

        if not ret:
            print("Görüntü alınamadı.")
            break

        # Renk tabanlı eşikleme uygula
        mask = color_thresholding(frame)

        # Nesneleri bul
        objects = find_objects(mask)

        # Engelleri algıla
        detect_obstacles(objects, frame.shape[1], frame.shape[0], frame)

        # Sonuçları ekranda gösterme
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Color Thresholding', mask)

        # 'q' tuşuna basıldığında döngüden çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kaynakları serbest bırak
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

