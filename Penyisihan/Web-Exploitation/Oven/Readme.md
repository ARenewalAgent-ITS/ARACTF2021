# Oven
---
## Deskripsi
Gunakan oven saat memanggang kue!

## Solusi
Diberikan source code sebuah web dengan sebuah cookie bake_here. Dari cookie tersebut,
kita dapat mengirimkan PHP Object dan password harus memiliki hash yang sama. Dari sini
harus melakukan type juggling. Kemnudian menemukan magic hash
sha-256 berupa “Sol7trnk00” yang memenuhi kondisi if-else untuk mendapatkan flag. Berikut
adalah PHP Serialized Object yang digunakan:
```
O:5:"Token":2:{s:8:"username";s:5:"admin";s:8:"password";s:10:"Sol7trnk00";}
```
encode payload di atas dan kirimkan request dengan cookie bake_here berisi payload
tersebut.

#### ara2021{cl4551c_typ3_ju66ling}
