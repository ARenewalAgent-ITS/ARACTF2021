# Lihat Sebelah Barat
---
## Deskripsi
~Sekilas Info!! Tahukah kamu? Sebagai salah satu kontraktor penambangan batubara terbesar di dunia, PT Pama Persada memiliki kompetensi yang luas & pemahaman mendalam dalam hal pengembangan & operasi tambang batubara yang meliputi : Eksplorasi, perencanaan, persiapan infrastruktur, operasi penambangan, reklamasi dan re-vegetasi di area bekas tambang ~
## Solusi
Diberikan sebuah gambar. Jika gambar tersebut dicek metadatanya akan menghasilkan gambar sebagai berikut
![image](https://user-images.githubusercontent.com/50267676/112207555-da6cd980-8c49-11eb-85ff-d4d21ee3c53d.png)

Jika dilihat, ada tag yang menarik bernama copyright dengan isi 4u90nAg9n8Q19pmfJ9zzPuWBdd3 dimana kode ini saya enkripsi dalam base62. Setelah dilakukan deskripsi akan menghasilkan kode "ara2021" is the key. Password identik digunakan jika kita ingin mencari atau melihat apakah ada data tersembunyi didalam gambar tersebut. setelah itu bisa dilakukan ekstrak data dari gambarnya dengan password “ara2021” dan akan mengekstrak dump.txt yang berisi 

“f1atblne0a11820f1atblnetheAlpgj<<!!>>,,theAlpgj<<!!>>,01111011XY32.X.Yl//lmml.63mm2*l6.+7lml622336*26/X3YXYXXY./YY.2Y32C7CBi*66iC6C2BBB3i6B36i>AQJ>Q7[\C;|Q[M]\C;|Q[M]|G]B>S.201111101 “

Setelah itu, untuk mengartikan kode tersebut kita bisa melihat dari gambar dan judul dimana disebutkan LSB(least significant bit).  Berikutnya, setiap karakter dalam kode tersebut diubah kedalam biner dan diambil digit paling belakangnya. Setelah diambil setiap digit paling belakang dari setiap karakter, maka semua digit tersebut disatukan lalu di translate ke bentuk char. Kode yang digunakan sebagai berikut

with open('dump.txt', 'rb') as f:\
    data = f.read().strip()\
terakhir = [b & 1 for b in data]\
print("Proses Pengambilan digit terakhir")\
print(terakhir)\
gabung = "".join(str(b) for b in terakhir)\
print("Proses menggabungkan semua digit")\
print(gabung)\
kelompok = [gabung[i:i+8] for i in range(0, len(gabung), 8)]\
print("Mengkelompokkan setiap 8 bit")\
print(kelompok)\
huruf = [chr(int(b, 2)) for b in kelompok]\
print("mengubah dari biner ke char")\
flag = "".join(huruf)\
print(flag)\

#### ara2021{alphaisthegood}
