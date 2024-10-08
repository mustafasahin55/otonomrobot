import cv2

def selective_search(image):
    # Selective Search algoritmasını oluştur
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

    # Görüntüyü al ve işle
    ss.setBaseImage(image)
    ss.switchToSelectiveSearchFast()  # Hızlı modu seç

    # Bölge önerilerini al
    rects = ss.process()

    return rects

def main():
    # Görüntüyü yükle
    image = cv2.imread('path/to/your/image.jpg')

    # Selective Search ile bölge önerilerini al
    rects = selective_search(image)

    # Sonuçları göster
    for i, rect in enumerate(rects):
        x, y, w, h = rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f'Region {i}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Sonuçları ekranda göster
    cv2.imshow('Selective Search', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

