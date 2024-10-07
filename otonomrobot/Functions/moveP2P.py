import firstfonks
import serial
import time
import math
import numpy as np
import sys
import DepthAnythingV2.getLength as bettercallsaul

# unoi port ayarları
mega = serial.Serial('/dev/serial/by-path/platform-xhci-hcd.0-usb-0:2:1.0-port0', 31250, timeout=0.1)

mega.bytesize = 8 #Bu, veri bitlerinin sayısını belirtir. Genellikle 8’dir.
mega.parity = 'N' #Bu, parity bitini belirtir. Genellikle ‘N’ (Yok) olarak ayarlanır.
mega.stopbits = 1 #Bu, durdurma bitlerinin sayısını belirtir. Genellikle 1’dir.ü
o=1
yaw = 0
i =0
j=0
def set_globyaw(yw):
    global yaw    # Needed to modify global copy of globvar
    yaw = round(yw, 1)

def set_globdenem(p):
    global j    # Needed to modify global copy of globvar
    j=p

def set_globkurtarici(k):
    global i    # Needed to modify global copy of globvar
    i=k
def yawRead():
    global yaw  # yaw'ın global olduğunu belirtiyoruz

    try:
        if mega.in_waiting > 0:
            yaw2 = mega.readline().decode('ASCII').rstrip("\n")
            yaw = float(yaw2)  # yaw2'yi float'a dönüştürmeyi deniyoruz
            set_globyaw(-1 * (yaw - 180))

    except (ValueError, TypeError):
        print(TypeError)  # Eğer dönüştürme başarısız olursa (None veya geçersiz bir değer nedeniyle)
        pass  # Hata oluşursa, bir şey yapmayız ve yaw'ın bir önceki değerini koruruz.

    except KeyboardInterrupt:
        print("Kullanıcı tarafından kesildi.")
    
    return yaw  # Her durumda, yaw'ı döndürürüz

yawRead()

def sendMove(data):
    try:
        #data = "1,14.64,20,150,1,2\n"
        mega.write(data.encode('ASCII')) 
        
    except KeyboardInterrupt:
        print("Kullanıcı tarafından kesildi.")

def calculate_infos(cx, cy, cyaw, gx, gy, gyaw,newx,newy):
    mp = []
    infos = firstfonks.pathplanner(cx, cy, cyaw, gx, gy, gyaw,newx,newy)
    print(infos)
    for miniinfo in infos:
        first_yaw = miniinfo[0]
        last_yaw = miniinfo[1]
        radius = miniinfo[2]
        rotation = miniinfo[3]
        c_x = miniinfo[4]
        c_y = miniinfo[5]
        if radius <= 0.1:
            radius = 1

        theta = 0
        if rotation != 0:
            theta = ((math.atan((16) / radius)) * 180) / math.pi
            theta = round(theta, 2)  
            alpha = (math.atan(16 / (radius + 12.25)) * 180) / math.pi
            alpha2 = (math.atan(16 / (radius - 12.25)) * 180) / math.pi
        match rotation:
            case 0: # düz
                moveParams = "1,0,0,0,200,1,2\n"  
            case -1: # sağ
                moveParams = "1," + str(theta) + "," + str(2*alpha) + "," +str(2*alpha2)+ ",70,1,1\n"
            case 1: # sol
                moveParams = "1," + str(theta) + "," + str(2*alpha) +"," +str(2*alpha2)+ ",70,1,-1\n"
            case _:
                moveParams = "1,0,0,0,0,0,0\n"
            
        mp.append([moveParams, first_yaw, last_yaw, radius, rotation, c_x, c_y])
    return mp

# Hedeflenen yaw değerini belirle

# Gerçek yaw değerini güncelle ve PID kontrolcüsünün çıktısını al
# Bu çıktı, servo motorları kontrol etmek için kullanılabilir
def arabasur(cx, cy, cyaw, gx, gy, gyaw,newx,newy):
    with open('output_log.txt', 'w') as log_file:
        def print_and_log(*args, **kwargs):
            print(*args, **kwargs)
            log_file.write(' '.join(map(str, args)) + '\n')

        counter = 1
        adim = 7
        cmd_s = 100.0
        moveParams = "1,0,0,0,0,0,0\n"
        sendMove(moveParams)
        time.sleep(5)
        
        print_and_log(yaw)
        print_and_log("1")
        
        time.sleep(2)
        print_and_log("2")
        yawRead()
        yawx = yaw
        print_and_log(yaw)
        print_and_log("lastread:", yaw)
        mp = calculate_infos(cx, cy, cyaw, gx, gy, gyaw,newx,newy)
        print_and_log(mp)
        time.sleep(2)
        l=1
        for inf in mp:
            if o==5:
                moveParams = "1,0,0,0,0,0,0\n"
                sendMove(moveParams)
                break
            if((inf[4]) == 0):
                set_globdenem(l)
                if j ==3:
                    break
                l=l+1
                print_and_log(inf[0])
                moveParams = inf[0]
                sendMove(moveParams)
                yawRead()
                Kp = 0.8
                ref = yaw
                error = 0
                t1 = time.time()
                
                print("inf",inf[3])
                t_s = float(inf[3] / cmd_s)
                print_and_log("ts",t_s)
                time.sleep(3)
                moveParams = "1,0,0,0,0,1,2\n"
                sendMove(moveParams)
                break
                while True:
                    yawRead()
                    
                    error = round(ref - yaw, 1)
                    if abs(error) > 180:
                        error = round(ref - yaw + 360, 1)
                    kontrol_signal = Kp * error
                    t2 = time.time()
                    print_and_log("burda")
                    if i==0:
                        
                    if (bettercallsaul.obje_yes_no() > 0):
                        set_globkurtarici(1)
                        print_and_log("surda")
                        moveParams = "1,0,0,0,0,1,2\n"      
                        sendMove(moveParams)
                        yesyaw = yawRead()
                        print(yesyaw)
                        gecensure = t2 - t1
                        kalansure = t_s - gecensure
                        kalanyol = (inf[3] * kalansure) / t_s
                        gidilenyol = (inf[3] * gecensure) / t_s

                        c_x = inf[5]
                        c_y = inf[6]
                        objeuzaklik,o_x1,o_x2 = bettercallsaul.kamera_to_uzaklik()
                        nesne_x =  int(c_x + int(np.float64(objeuzaklik/2) * np.cos(np.radians(float(90)))))
                        nesne_y =  int(c_y + int(np.float64(objeuzaklik/2) * np.sin(np.radians(float(90)))) )
                        print_and_log("nesnex",nesne_x)
                        print_and_log("nesney",nesne_y)
                        arabasur(c_x, c_y, yesyaw, gx, gy, gyaw,180,250)
                        
                        break
                    
                    print('else')
                    print_and_log("error:", error)
                    '''if abs(error) > 1:
                        servoangle = (-1 * kontrol_signal)
                        print_and_log("servoangle:", servoangle)
                        if servoangle < 0:  
                            moveParams = "1," + str(round(error, 1)) + "," + str(round(error, 1)) + ","+ str(abs(round(servoangle))) + ",200,1,-1\n"
                            #moveParams = "1," + str(round(error, 1)) + "," + "30" + ",128,1,-1\n"
                            
                            print_and_log(moveParams)
                        
                        elif servoangle > 0:
                            moveParams = "1," + str(round(error, 1)) + "," + str(round(error, 1)) + ","+ str(abs(round(servoangle))) + ",200,1,1\n"
                            #moveParams = "1," + str(round(error, 1)) + ",30" + ",128,1,1\n"
                            print_and_log(moveParams)
                        td = time.time()
                        if(time.time() - td > 0.25):
                            sendMove(moveParams)
                            td = time.time()'''
                        
                    if ((t2 - t1) > t_s):
                        print('surda')
                        moveParams = "1,0,0,0,0,0,0\n"
                        sendMove(moveParams)
                        break
                    
            elif((inf[4]) == -1 or (inf[4]) == 1):
                yawRead()
                inf[2] = 180.0 + round((inf[2]), 1)
                moveParams = inf[0]
                sendMove(moveParams)
                while abs(inf[2] - round(yaw, 1)) > 0.5:
                    yawRead()
                    
                    print_and_log("yawfirst:", yaw)
                    print_and_log("inffirst:", round(inf[2], 1))
                    yawRead()
                    """moveParams = "1,0,0,0,1,2\n"      
                    sendMove(moveParams)
                    time.sleep(1)""" #kamera yaz buraya <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        moveParams = "1,0,0,0,0,1,2\n"      
        sendMove(moveParams)

if __name__ == '__main__':
    arabasur(40,40,90,40,350,90,0,0)
