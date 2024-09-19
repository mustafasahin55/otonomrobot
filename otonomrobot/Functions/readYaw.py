import serial
mega = serial.Serial('/dev/serial/by-path/platform-xhci-hcd.0-usb-0:2:1.0-port0', 31250,timeout=0.1)
import time



mega.bytesize = 8 #Bu, veri bitlerinin sayısını belirtir. Genellikle 8’dir.
mega.parity = 'N' #Bu, parity bitini belirtir. Genellikle ‘N’ (Yok) olarak ayarlanır.
mega.stopbits = 1 #Bu, durdurma bitlerinin sayısını belirtir. Genellikle 1’dir.ü


yaw = 0

def set_globyaw(yw):
    global yaw    # Needed to modify global copy of globvar
    yaw = round(yw,1)


def yawRead():
    global yaw  # yaw'ın global olduğunu belirtiyoruz

    try:
        if mega.in_waiting > 0:
            yaw2 = mega.readline().decode('ASCII').rstrip("\n")
            yaw = float(yaw2)  # yaw2'yi float'a dönüştürmeyi deniyoruz
            set_globyaw(-1*(yaw-180))

    except (ValueError, TypeError):
        print(TypeError)  # Eğer dönüştürme başarısız olursa (None veya geçersiz bir değer nedeniyle)
        pass  # Hata oluşursa, bir şey yapmayız ve yaw'ın bir önceki değerini koruruz.

    except KeyboardInterrupt:
        print("Kullanıcı tarafından kesildi.")

    return yaw  # Her durumda, yaw'ı döndürürüz


def main():
    yawRead()
    print(yaw)
    print("1")

    time.sleep(0.5)
    print("2")
    yawRead()
    
    while True:      

        print("2")
        yawRead()
        
        print(yaw)
        print("lastread:",yaw)


if __name__ ==  '__main__':
    main()
