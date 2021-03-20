# 0zip
---
## Deskripsi
PT Pama Persada sedang melakukan pengeboran untuk mendapatkan mineral di lokasi penemuan mineral terbaru mereka. seorang engginer nya lalu berkata : We need to go deeper...
## Solusi
bisa menggunakan ```strings 0.zip | grep ara2021```.
Didapat file bernama 0.zip, didalamnya terdapat file bernama 1.zip, dan seterusnya. Soal seperti ini lumayan marak di ajang CTF. File nested zip tersebut saya ekstrak dengan bash menggunakan perintah berikut:

```for i in {0..100}; do unzip "$i" -d "${i%%.zip}"; unzip "$i"; done```

Perintah tersebut akan mengekstrak suatu file zip bernama 0 sampai 100 sebanyak 2 kali, pada folder baru sesuai namanya dan pada folder tempat zipnya berada. Pada zip ke-100, file FLAG muncul dan berisi:

Sepertinya file tersebut merupakan flag palsu, karena setelah ditelusuri lebih lanjut file berskema XML ini merupakan file kontak di windows yang biasanya berekstensi ".contact" yang isinya terdapat flag:

    ara2021{ini bukan flag}

Setelah menelusuri kembali hasil ekstrak keseluruhan menggunakan perintah ```tree```
101 directories, 205 files

Pada hasil tersebut terdapat suatu keanehan pada ke-44 yang mana terdapat 2 file didalamnya sedangkan di folder lain hanya terdapat satu file. File yang dicurigai bernama 46.zip dan ketika dicoba dibuka menggunakan 7zip tidak bisa. Mencoba menampilkan isinya menggunakan 'cat' didapatkan flag:


#### ara2021{1N53r7-1Nc3P710N-M3m3-H3R3-3TuxG6}