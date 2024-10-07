import numpy as np

def mapping(x_adim,y_adim):

    x_step = x_adim # x yönünde x birim ilerlendiğinde yeni harita
    y_step = y_adim # y yönünde y birim ilerlendiğinde yeni harita
    matris_dosya="sonuc_matrisi.txt"
    lidar_dosya="lidar_haritasi.txt"

    # Dosyayı oku
    with open(matris_dosya, "r") as dosya:
        satirlar = dosya.readlines()

    # Her satırı bir liste olarak ayır
    matris_listesi = [satir.strip().split("\t") for satir in satirlar]

    # Liste verilerini bir NumPy dizisine dönüştür
    matris = np.array(matris_listesi, dtype=int)

    satir, sutun = matris.shape
    yeniden_boyutlandirilmis_matris = np.zeros((satir+x_adim, sutun+y_adim))

    yeniden_boyutlandirilmis_matris[:matris.shape[0], :matris.shape[1]] = matris
    matris = np.zeros((satir, sutun))
    #yeniden_boyutlandirilmis_matris[x_adim:, y_adim:] = matris

    
    #dosya_adi = "lidar_haritasi_deneme.pgm"  # Derece ve uzaklık veren lidar bilgisi
    derece=0

    try:
        with open(lidar_dosya, "r") as dosya:
            for line in dosya:
                derece,satir = line.strip().split(',')
                satir = satir.strip()
                x =  x_step + 400 + int(np.float64(satir) * np.cos(np.radians(float(derece))))
                y =  y_step + 400 + int(np.float64(satir) * np.sin(np.radians(float(derece))))
                matris[x,y]=1
    
        for x in range(118,682):
            for y in range(118,682):  
                yeniden_boyutlandirilmis_matris[x+x_adim, y+y_adim] = matris[x,y]
    
        np.savetxt(matris_dosya, yeniden_boyutlandirilmis_matris, fmt="%d", delimiter="\t")    
    except FileNotFoundError:
        print(f"Dosya '{lidar_dosya}' bulunamadı.")
    except Exception as hata:
        print(f"Bir hata oluştu: {hata}")
    
    return yeniden_boyutlandirilmis_matris


"""def main():
    mapping(0,0)

if __name__ == '__main__':
    main()
"""


