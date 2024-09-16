import numpy as np
import matplotlib.pyplot as plt

# Dosyayı oku
with open("sonuc_matrisi.txt", "r") as dosya:
    satirlar = dosya.readlines()

# Her satırı bir liste olarak ayır
matris_listesi = [satir.strip().split("\t") for satir in satirlar]

# Liste verilerini bir NumPy dizisine dönüştür
matris = np.array(matris_listesi, dtype=int)
x = matris[:,0]
y = matris[:,1]

# Matrisi siyah-beyaz olarak çiz
plt.imshow(matris, cmap='gray')
plt.axis('off')  # Eksenleri kapat
plt.show()
