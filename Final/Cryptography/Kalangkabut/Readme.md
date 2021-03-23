# Kalangkabut
---
## Deskripsi
Maaf kalo acak-acakan :'(

*flag.png berisi qr code
## Solusi

Script tersebut mengenkripsi sebuah file image yang merupakan qrcode , file image tersebut diawal diubah nilai pixelnya secara random lalu dixor dengan suatu value dan terakhir dienkripsi dengan aes kemudian nilai enkripsinya direwrite ke gambar. Jadi untuk mengembalikan gambar tersebut kita perlu melakukan decrypt aes ( passwordnya 8byte pixel pertama dari qrcode ) lalu xor value dan crack randomnya. Berikut script yang digunakan untuk melakukan decrypt terhadap enc.png 

```
import qrcode  # https://github.com/lincolnloop/python-qrcode
from PIL import Image
from randcrack import RandCrack # https://github.com/tna0y/Python-random-module-cracker
from textwrap import wrap
from Crypto.Cipher import AES
import binascii

def decrypt(im):
	pix = im.load()
	width , height = im.size
	text=[]
	for y in range(0,height):
    	for x in range(0,width):
        	text.append(pix[x,y])
	for i in range(len(text)-1,-1,-1):
    	if(text[i]==(0, 0, 0)):
        	text.pop()
    	else:
        	break
    
	password=b"9b9b9b9b9b9b9b9b"
	ciphertext=b''.join(map(bytes,text))
	ciphertext=ciphertext[:-1*(len(ciphertext)%16)]
    
	obj2 = AES.new(password, AES.MODE_CBC,b'_ara2021ara2021_')
	decrypted = obj2.decrypt(ciphertext).decode()
	newwidth = decrypted.split("w")[1]
	newheight = decrypted.split("h")[1]
    
	heightr = "h" + str(newheight) + "h"
	widthr = "w" + str(newwidth) + "w"
	decrypted = decrypted.replace(heightr,"")
	decrypted = decrypted.replace(widthr,"")
	decrypted = decrypted.replace("n","")
	decrypted = binascii.unhexlify(decrypted)
    
	step = 3
	plaintext=[]
	for i in range(0,len(decrypted),3):
    	plaintext.append(decrypted[i]^100)
   	 
	newim = Image.new("L", (int(newwidth), int(newheight)))
    
	newim.putdata(plaintext)
	return newim

def main():    
	qr = qrcode.QRCode(
    	version=1,
    	error_correction=qrcode.constants.ERROR_CORRECT_L,
    	box_size=12,
    	border=4,
	)
	qr.add_data("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white")
	m, n = img.size

	im = Image.open('enc.png')
	share2=decrypt(im)

	bitstream = []
	for idx in range(48 * 444):
    	i, j = idx//n + 444 - 48, idx % n
    	if share2.getpixel((2*j, 2*i)):
        	bitstream.append(0)
    	else:
        	bitstream.append(1)
	bitstream = "".join([str(x) for x in bitstream])

	rc = RandCrack()

	splitstream = wrap((bitstream), 32)
	splitstream.reverse()

	for i in range(624):
    	val = int(splitstream[i],2)
    	rc.submit(val)

	newlist = bin(rc.predict_getrandbits(444 * 444))[2:].zfill(444 * 444)

	splitstream2 = newlist[-(444*444 - (32 * 624)):] + bitstream[-(32 * 624):]
 
	original = []
	for k in range(444 * 444):
    	i, j = k//n, k % n
    	if share2.getpixel((2*j, 2*i)):
        	if int(splitstream2[k]):
            	original.append(0)
        	else:
            	original.append(255)
    	else:
        	if int(splitstream2[k]):
            	original.append(255)
        	else:
            	original.append(0)

	# Save the resulting data back into an image
	res = Image.new("L", img.size, 255)
	res.putdata(original)
	res.save('fix_flag.png')

if __name__ == '__main__':
	main()

```

#### ara2021{h0w_did_y0u_s0lv3_r4nd0m_4nd_tr1cky_435?}
