#!/usr/bin/python3

import random
from PIL import Image
import math
from Crypto.Cipher import AES
import binascii

def encrypt(im):
    width , height = im.size
    bitz=[]
    for i in bin(random.getrandbits(width*height))[2:].zfill(width*height):
        bitz.append(int(i))
    key = Image.new("L", (2*width, 2*height))
    pix_key=key.load()
    widthh , heightt = key.size
    text=[]
    image_data = im.getdata()
    password=""
    for i in range(8):
        password+=hex(image_data[i][0]^100)[2:]
    
    pix = im.load()
    plaintextstr = ""
    counter=0
    for y in range(0,height):
        for x in range(0,width):
            if(bitz[counter]):
                val_1=0
            else:
                val_1=255
            if(bitz[counter]):
                val_2=255
            else:
                val_2=0
            if(pix[x,y]==(255,255,255)):
                pix_key[2*x, 2*y]= val_1
                pix_key[2*x, 2*y+1]= val_1
                pix_key[2*x+1, 2*y]= val_2
                pix_key[2*x+1, 2*y+1]= val_2
            else:
                pix_key[2*x+1, 2*y]= val_1
                pix_key[2*x+1, 2*y+1]= val_1
                pix_key[2*x, 2*y]= val_2
                pix_key[2*x, 2*y+1]= val_2
            counter+=1
    
    key=key.convert('RGB')
    pix_key=key.load()
    for y in range(0,heightt):
        for x in range(0,widthh):
            text.append(pix_key[x,y])
    length = len(text)
    
    for i in range(0,len(text)):
        for j in range(0,3):
            plaintextstr += str(hex(int(text[i][j])^100)[2:])
    plaintextstr += "h" + str(heightt) + "h" + "w" + str(widthh) + "w"
    
    while (len(plaintextstr) % 16 != 0):
        plaintextstr = plaintextstr + "n"
    obj = AES.new(password.encode(), AES.MODE_CBC, b'_ara2021ara2021_')
    ciphertext = obj.encrypt(plaintextstr.encode())
    
    step = 3
    encone=[ciphertext[i:i+step] for i in range(0, len(ciphertext), step)]
    
    if len(encone[-1]) % 3 != 0:
        while (len(encone[-1]) % 3 != 0):
            encone[-1]+=b"1"
    enctwo=[]
    for i in range(len(encone)):
        tmp=(encone[i][0],encone[i][1],encone[i][2])
        enctwo.append(tmp)
    
    zzx=int(math.ceil(math.sqrt(len(enctwo))))
    zzy=zzx
    
    while len(enctwo)!=zzx*zzy:
        enctwo.append((0,0,0))
    encres = Image.new("RGB", (zzx,zzy))
    encres.putdata(enctwo)
    encres.save("enc.png")


def main():
    img = Image.open('flag.png').convert('RGB')
    encrypt(img)

if __name__ == '__main__':
    main()
