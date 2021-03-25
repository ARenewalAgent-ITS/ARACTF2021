# Secure Password Manager v2
---
## Deskripsi
Untuk lebih mengamankan akun freefire ku aku menggunakan aplikasi secure password manager yang terbaru dengan algoritma enkripsi yang katanya lebih aman dibanding yang v1. Namun pada v2 key tersimpan secara jelas pada file stored.passwd dan aku takut seseorang dapat mengetahui passwordku berdasarkan key yang ada di sana , jadi aku menyembunyikan key1 untuk password akun freefireku di flashdisk. Sialnya aku flashdisk itu hilang dan tentunya aku tidak mengingat angka panjang itu hmm dan sekarang aku lupa passwordku juga. Apakah ada yang bisa membantuku mendapatkan passwordku kembali? tentunya agar aku bisa bermain freefire lagi!
## Solusi
Diberikan sebuah file ELF yang dibuat menggunakan bahasa pemrograman GO. 
Kita dapat mengetahui fungsi main dari program tersebut dengan cara melakukan penelusuran struktur fungsi main pada program golang yaitu main_main


Selanjutnya kita tinggal melakukan analisis terhadap fungsi enkripsi yang ada dan ternyata algoritma yang diterapkan adalah RSA. Yang mana nilai q adalah komplemen dari p*2020. Selanjutnya kita tinggal mencari cara untuk mendapatkan private key dari RSA. Ternyata kita bisa mendapatkan nilai p dan q dengan melakukan akar kuadrat terhadap nilai yang telah ditemukan berdasarkan ke valid an nilai masknya ( kuadrat atau bukan ).

Selanjutnya kita asumsikan misal panjang dari flag adalah 3 ( enc )
val=2**21
bigInteger=0
(bigInteger*val)+enc[i])*val+enc[i+1])*val+enc[i+2]==right
(bigInteger*val)+enc[i])*val+enc[i+1])*val+enc[i+2]-enc[i+2]==right-enc[i+2]
(bigInteger*val)+enc[i])*val+enc[i+1])*val==right-enc[i+2]
karena kita tahu value dari val , kita bisa melakukan gcd
(bigInteger*val)+enc[i])*val+enc[i+1])*val with val , Jika hasilnya adalah val maka tebakan kita benar

Berikut solver yang digunakan
```
import binascii
import math
import gmpy2
import codecs
import base64

n = 0x17175c829b1b8d10e5d02f0fe1b258fae6ccb9abc7932ecaecd1f55120ba333c32b63abeed70c3e1b723484217a8e0927fbc3feef2c049d78816337323e79bb167fa9feba7d53b10790961364abe916d8e77d4e913b99cfe6a4fe6f3008d8842ed84a4b2ddf9c1ee6e76c6d6294f41e6def39f107e9648bdeac7d4057ec4bb99bba6268c07b6c490712b89170f3f02f750510db1798076543d57db3e055c1f07aad168dafe93cf5d014b35ddc499cae4e6ee3c0bb82f1d77d9bc74c63b1e5d82cae714b044c13f12eee733011e5b374bdf197549548fd3d2ed897bfa0669b173f68836fd55e9c7f75dc3d6b754bb4aeeaafa9b14d6f8511918d1aa138d7fd430027
e = 65537
c = 0x119266650a5e56985692f73c8cb792bdf0a6fb1e7bb265a565511cecd60819a67e420300882d4d5e2bcc2f819bc4bb801349bbe75af93297a52951e654594d850a1508ddcd42f25323dbbc9b75e74b669faa3baeff551b35efed7d36c6b68e29acd465e0a0f3267441bf6c6ff4d61ae0833269c5b4004f56c751dfd46efc7cb8ea9fcf9416ec6d13df4c5bdb5a754391a4de612706985a22df5d977d245d2122a39fb37a7e73fdb633ad8ec3792f7846c2e9046b63e20b6d59aedf9a4ec940d28f4c43dcff94109cdf7aea0e43ffbb60542f204b7e981340ee76d541744ab6dfd6249c38aea10d331cf8c6a92a48c844c08b42bcf4d3808fb429dfa10de94f1381f

ss = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dd = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(20):
    ss[i] = (2 ** (i + 1020)) - 1
    dd[i] = ss[i] ** 2 - 4 * n * 2020
    if dd[i].is_square():
        sum = ss[i]
        product = n*2020
        break

x = var('x')
p,q = solve(x^2 -sum*x + product == 0, x)
p,q = int(str(p)[5:]), int(str(q)[5:])
if p % 2 == 0:
    p /= 2020
else:
    q /= 2020

target = int(pow(c, inverse_mod(e, (p - 1) * (q - 1)), n))

list_char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/={}?_"
val=2**21
res=""
while target!=0:
    for i in list_char:
        tmp=gmpy2.gcd((target-ord(i)*1337),val)
        if(tmp==val):
            res+=i
            break
    target-=ord(res[-1])*1337
    target>>=21
print(res[::-1])
```

#### ara2021{d0_w3_h4v3_a_r3l4t10nSh1p?}
