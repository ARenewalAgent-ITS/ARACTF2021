# cocomilk
---
## Deskripsi
Qiqi adalah seorang zombie yang sering pelupa. Suatu hari ia membuat kodingan dalam bahasa C++ untuk membuat kode rahasia lokasi cocomilk. Namun beberapa saat kemudian dia lupa menulis kodingan tersebut dalam bahasa C++ dan menuliskannya dalam bahasa Python. Qiqi yang kebingungan mencoba menginputkan lokasi cocomilk tersebut dengan menjalankan kodingannya dalam bahasa C++ dan Python. Anehnya, kodingannya dapat berjalan dan menghasilkan Output 1 pada bahasa C++ dan Output 2 pada bahasa Python. Beberapa saat kemudian, Qiqi melupakan lokasi rahasia cocomilk yang barusan diinputkan. Bantu Qiqi untuk mendapatkan lokasi rahasia cocomilk miliknya!
## Solusi
kalau dipisah dapet 2 kodingan dalam bahasa cpp dan python. "jadi.cpp" akan mengambil
karakter dengan indeks genap. Lalu string yang udah jadi itu di XOR dengan indeks string baru.
lalu akan mendapat Output 1. "jadi.py" akan mengambil karakter dengan indeks genap dan
indeks ganjil. string indeks ganjil akan di XOR dengan indeks string barunya dan di XOR dengan
karakter dengan indeks yang sama pada string indeks genap. Untuk output akan diformat
dalam bentuk hex.
Untuk mendapatkan jawaban, Output 1 di XOR sesuai indeksnya. Lalu didapat string untuk
indeks genap. Output 2 di XOR sesuai indeksnya dan di XOR lagi sesuai string indeks genap.
Lalu didapat string indeks ganjil. Lalu kedua string digabungkan kembali.

#### ara2021{C0com1lk_IS_Coc0g04t_M!lK}