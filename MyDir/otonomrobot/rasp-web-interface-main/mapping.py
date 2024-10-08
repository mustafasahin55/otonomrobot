import numpy as np

def mapping(x_adim,y_adim):

    x_step = x_adim # x yönünde x birim ilerlendiğinde yeni harita
    y_step = y_adim # y yönünde y birim ilerlendiğinde yeni harita
    matris_dosya="sonuc_matrisi.txt"
    lidar_dosya="veri.txt"

    # Dosyayı oku
    with open(matris_dosya, "r") as dosya:
        satirlar = dosya.readlines()

    # Her satırı bir liste olarak ayır
    matris_listesi = [uzaklik.strip().split("\t") for uzaklik in satirlar]

    # Liste verilerini bir NumPy dizisine dönüştür
    matris = np.array(matris_listesi, dtype=int)

    uzaklik, sutun = matris.shape
    yeniden_boyutlandirilmis_matris = np.zeros((uzaklik+x_adim, sutun+y_adim))

    yeniden_boyutlandirilmis_matris[:matris.shape[0], :matris.shape[1]] = matris
    matris = np.zeros((uzaklik, sutun))
    #yeniden_boyutlandirilmis_matris[x_adim:, y_adim:] = matris

    
    #dosya_adi = "lidar_haritasi_deneme.pgm"  # Derece ve uzaklık veren lidar bilgisi
    derece=0

    try:
        with open(lidar_dosya, "r") as dosya:
            derece_uzaklik_dict = {}
            for line in dosya:
                derece,uzaklik = line.strip().split(',')
                uzaklik = uzaklik.strip()
                uzaklik = np.float64(uzaklik) * 0.1
                """x =  x_step + 400 + int(np.float64(uzaklik) * np.cos(np.radians(float(derece))))
                y =  y_step + 400 + int(np.float64(uzaklik) * np.sin(np.radians(float(derece))))
                matris[x,y]=1"""
                if derece in derece_uzaklik_dict:
                    derece_uzaklik_dict[derece].append(uzaklik)
                else:
                    derece_uzaklik_dict[derece] = [uzaklik]
            for derece, uzaklik_listesi in derece_uzaklik_dict.items():
                ortalama_uzaklik = sum(uzaklik_listesi) / len(uzaklik_listesi)
                if(int(20<ortalama_uzaklik)<=280 and 0<=float(derece)<360):
                    x = x_step + 400 + int(int(ortalama_uzaklik) * np.cos(np.radians(float(derece))))
                    y = y_step + 400 + int(int(ortalama_uzaklik)* np.sin(np.radians(float(derece))))
                    matris[x, y] = 1
                
        for x in range(118,682):
            for y in range(118,682):  
                yeniden_boyutlandirilmis_matris[x+x_adim, y+y_adim] = matris[x,y]
    
        np.savetxt(matris_dosya, yeniden_boyutlandirilmis_matris, fmt="%d", delimiter="\t")    
    except FileNotFoundError:
        print(f"Dosya '{lidar_dosya}' bulunamadı.")
    except Exception as hata:
        print(f"Bir hata oluştu: {hata}")
    
    return yeniden_boyutlandirilmis_matris


def main():
    mapping(0,0)

if __name__ == '__main__':
    main()



