# client.py
import serial
import socket

mega = serial.Serial('/dev/serial/by-path/platform-xhci-hcd.1-usb-0:2:1.0-port0', 9600)
data_to_send = "1,0,0,100,1,1\n"


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.125.2.24', 8080))

    mega.write(data_to_send.encode('ASCII'))

    while True:
        print('while')
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            print("abc")
            print(data)
            data_to_send_two = "1,0,0,0,1,1\n"
            mega.write(data_to_send_two.encode('ASCII')) 
        else:
            break

    client_socket.close()

if __name__ == "__main__":
    main()
