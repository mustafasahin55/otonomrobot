# client.py
import socket
import cv2
import torch
import numpy as np
import os

from DepthAnythingV2.depth_anything_v2.dpt import DepthAnythingV2

model_configs = {
    'vits': {'encoder': 'vits', 'features': 64, 'out_channels': [48, 96, 192, 384]},
    'vitb': {'encoder': 'vitb', 'features': 128, 'out_channels': [96, 192, 384, 768]},
    'vitl': {'encoder': 'vitl', 'features': 256, 'out_channels': [256, 512, 1024, 1024]},
    'vitg': {'encoder': 'vitg', 'features': 384, 'out_channels': [1536, 1536, 1536, 1536]}
}

model = DepthAnythingV2(**model_configs['vits'])
model.load_state_dict(torch.load(f'/home/melih/Desktop/MyDir/Functions/DepthAnythingV2/checkpoints/depth_anything_v2_vits.pth', map_location='cpu'))
model.eval()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.135', 8080))
def obje_yes_no():
    data = client_socket.recv(1024).decode('utf-8')
    if data:
        return 1
def kamera_to_uzaklik():
    kontrol=1

    while (1):
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            kontrol=0
            parcalanmis_veri = data.split("(")[1].split(")")[0]
            koordinatlar = parcalanmis_veri.split(", ")
            x1 = int(koordinatlar[0].split("=")[1])
            y1 = int(koordinatlar[1].split("=")[1])
            x2 = int(koordinatlar[2].split("=")[1])
            y2 = int(koordinatlar[3].split("=")[1])

            raw_img = cv2.imread('/home/melih/Desktop/MyDir/output.png')
            depth = model.infer_image(raw_img) # HxW raw depth map in numpy

            if(0>x1 ): 
                x1=1
            elif (x1 >depth.shape[0]):
                x1 = depth.shape[0]-1

            if(0>x2 ): 
                x2=1
            elif(x2 >depth.shape[0]):
                x2 = depth.shape[0]-1

            if(0>y1):
                y1 = 1
            elif(y1 >depth.shape[0]):
                y1 = depth.shape[1]-1

            if(0>y2): 
                y2 = 1
            elif(y2 >depth.shape[0]):
                y1 = depth.shape[1]-1

            #print(x1,x2,y1,y2)

            #depth[y1,x1]=0
            #depth[y2,x2]=0

            
            depth = (depth - depth.min()) / (depth.max() - depth.min()) * 255.0
            
            matris = depth[y1:y2, x1:x2]
            ortalamagri = np.mean(matris)
            #uzaklik = 1298.58 - 112.515 * np.log(431.248 * ortalamagri + 2600.38)
            #uzaklik = 9689.45 - (9179.33*(ortalamagri**0.00965939))
            uzaklik = 836.457 - 72.2733 * np.log(356.831 * ortalamagri - 3979.18)
            print (uzaklik)
            cv2.imwrite(os.path.join('./vis_depth', '/home/melih/Desktop/MyDir/output2.png'), depth)
            return uzaklik,x1,y1,x2,y2
            """rpiadaptor=depth[ 240:308,56:118]
            kamerakutu=depth[ 220:250,360:400]
            invision=depth[ 123:231,190:240]
            print(ortalamagri)
            print(np.mean(invision))
            print(np.mean(rpiadaptor))
            print(np.mean(kamerakutu))
            print("depth ortalamagri:",np.mean(depth))"""
            

            print(np.mean(airpods))
            print(np.mean(mouse))
            print(np.mean(anakart))
            print(np.mean(kamerakutu))

            """cv2.rectangle(depth, (56,240),(118,308), 0, 2)  # 255: Beyaz renk, 2: Kalınlık
            cv2.rectangle(depth, (x1,y1),(x2,y2), 255, 2)
            cv2.rectangle(depth, (360,220),(400,250), 0, 2)
            cv2.rectangle(depth, (190,123),(230,231), 0, 2)"""
            
            depth = depth.astype(np.uint8)
            depth = np.repeat(depth[..., np.newaxis], 3, axis=-1)
            """matris = matris.astype(np.uint8)
            matris = np.repeat(matris[..., np.newaxis], 3, axis=-1)
            invision = invision.astype(np.uint8)
            invision = np.repeat(invision[..., np.newaxis], 3, axis=-1)
            rpiadaptor = rpiadaptor.astype(np.uint8)
            rpiadaptor = np.repeat(rpiadaptor[..., np.newaxis], 3, axis=-1)
            kamerakutu = kamerakutu.astype(np.uint8)
            kamerakutu = np.repeat(kamerakutu[..., np.newaxis], 3, axis=-1)"""
            
            """cv2.imwrite(os.path.join('./vis_depth', '/home/melih/Desktop/MyDir/output2.png'), depth)
            cv2.imwrite(os.path.join('./vis_depth', '/home/melih/Desktop/MyDir/mouse.png'), mouse)
            cv2.imwrite(os.path.join('./vis_depth', '/home/melih/Desktop/MyDir/airpods.png'), airpods)
            cv2.imwrite(os.path.join('./vis_depth', '/home/melih/Desktop/MyDir/kamerakutu.png'), kamerakutu)"""
            
            
            
            
        else:
            return -1,-1,-1,-1,-1

    #client_socket.close()


def main():
    print(kamera_to_uzaklik())
    
if __name__ == '__main__':
    main()