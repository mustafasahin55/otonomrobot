import cv2
import numpy as np

def detect_obstacle(frame, background, threshold=5000):
    """
    Hareket algılamaya dayalı engel tespiti.
    - frame: Şu anki kare.
    - background: Arkaplan referans görüntüsü.
    - threshold: Engel algılama için fark piksel sayısı eşiği.
    """
    # Kareyi gri tonlamalı hale getir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Arkaplan ile şu anki kare arasındaki farkı hesapla
    diff = cv2.absdiff(background, gray)

    # Farkı eşikleyerek ikili görüntü oluştur
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Beyaz piksel sayısını hesapla
    white_pixels = np.sum(thresh == 255)

    # Beyaz piksel sayısı eşik değerini aşarsa engel vardır
    if white_pixels > threshold:
        return True, thresh
    else:
        return False, thresh

def main():
    # Kameradan görüntü al
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera açılamadı.")
        return

    # İlk kareyi oku ve gri tonlamalı hale getir (arka plan referansı)
    ret, background_frame = cap.read()
    background = cv2.cvtColor(background_frame, cv2.COLOR_BGR2GRAY)

    while True:
        # Kameradan bir kare oku
        ret, frame = cap.read()

        if not ret:
            print("Görüntü alınamadı.")
            break

        # Engel algıla
        obstacle_detected, thresh = detect_obstacle(frame, background)

        # Sonucu ekranda göster
        if obstacle_detected:
            cv2.putText(frame, "Obstacle Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "No Obstacle", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Orijinal görüntü ve ikili fark görüntüsünü göster
        cv2.imshow("Original", frame)
        cv2.imshow("Threshold", thresh)

        # 'q' tuşuna basılınca döngüyü sonlandır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kaynakları serbest bırak
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

