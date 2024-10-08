import cv2
import numpy as np

def color_segmentation(frame):
    # Görüntüyü BGR formatından HSV formatına dönüştürme
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Renk aralığını belirleme (mavi örneği)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Maske oluşturma
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Maskenin uygulandığı görüntüyü al
    segmented_image = cv2.bitwise_and(frame, frame, mask=mask)

    return segmented_image, mask

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

        # Renk segmentasyonu uygulama
        segmented_image, mask = color_segmentation(frame)

        # Sonuçları ekranda gösterme
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Segmented Image', segmented_image)
        cv2.imshow('Mask', mask)

        # 'q' tuşuna basıldığında döngüden çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kaynakları serbest bırak
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

