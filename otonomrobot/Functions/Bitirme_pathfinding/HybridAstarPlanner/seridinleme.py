import serial

# Seri port bağlantısını açın (port adını ve baud rate'i ayarlayın)
ser = serial.Serial('COM11', 9600, timeout=1)

def seridinleme():
    try:
        with open("veri.txt", "w") as dosya:
            for _ in range(360):
                veri = ser.readline().decode().strip()
                if veri:
                    print(f"Okunan veri: {veri}")
                    dosya.write(veri + "\n")
    except KeyboardInterrupt:
        print("Kullanıcı tarafından kesildi.")
    finally:
        # Seri port bağlantısını kapatın
        ser.close()
        print("Veri veri.txt dosyasına 360 satırla kaydedildi.")
