# Online Notes Storage
---
## Deskripsi
Waduh rekan kerjaku ngoding langsung di production server, hmm aku takut ada yang salah di kodingannya :3 . Dan ya tentu aku cuman punya file kodinganku saja tidak dengan tambahan dari rekanku

NB : Flag terbagi menjadi 2 bagian
## Solusi
Diberikan sebuah website dengan backend Flask. kemudian
melakukan SSTI. JWT dapat di-craft sendiri sehingga roles bernilai “member” karena
verify=False.
Pada endpoint protected, kita dapat mengupload sebuah file dan nama file tidak di-sanitize
sehingga dapat keluar dari path ./static/uploads. Kami pun mencoba mengupload file untuk
meng-overwrite sebuah template yang berisi payload SSTI dan berhasil.
Kemudaian akan mendapatkan 
-list of file 
-setelah itu Dapat key di app.py, yaitu 648b8f4e7cf9e805fa68e2f9d4bab173
- kemudian Dapat encrypted flag part di database dump, yaitu
856A06F12ACC7EDC6FFC90656EB8F3C11A5472F10D9AFD1C18
-Dapat script encryption.py
-Dapat flag part di flag.txt, yaitu 1n_4ct10n_8f7a23b1}
Untuk mendapatkan flag part 1, gunakan key, encrypted flag, dan encryption script yang
didapatkan .
Setelah kedua potongan flag disatukan, didapat flag utuh berikut.

#### ara2021{d0ubl3_1n73ct1on_1n_4ct10n_8f7a23b1}
