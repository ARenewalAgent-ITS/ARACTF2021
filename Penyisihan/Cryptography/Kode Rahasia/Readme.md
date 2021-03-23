# Kode Rahasia
---
## Deskripsi
Kamu adalah seseorang yang bekerja di PT Pama Persada.  Ditengah-tengah pekerjaan mu, seseorang teman datang dan berkata bahwa dia menemukan harta karun di salah satu lokasi penambangan. Tetapi dia tidak bisa memberitahukan lokasinya secara langsung, lalu berkata

"There is geometry in the humming of the strings, there is music in the spacing of the spheres. and at the end, you will find hamming is very useful"

dan memberikan sebuah lokasi titik koordinat

1001111001000111100100011000001110111101101100000011000111100101011000001110101

carilah lokasi dari harta karun tersebut


## Solusi

Clue : "You will find hamming is very useful"
Act : soal ini hanya perlu diselesaikan menggunakan kode hamming saya
Berikut adalah kode solver yang dapat digunakan

```
from math import ceil, log

s = "1001111001000111100100011000001110111101101100010011000111100101011000001110111"

LENS = len(s)

MAXP = ceil(log(LENS)/log(2))


print(">>> Pengecekan Error...")

flipbit = -1

for p in range(MAXP):
    
    skip = 2*p
    
    start = skip - 1
    
    ones = 0
    
    for i in range(start, LENS, 2skip):
    
      ones += s[i:i+skip].count("1")
    
    if ones % 2 == 1:
        
        flipbit = max(flipbit, 0) + skip

if flipbit != -1:
    
    msg = ">>> Error pada bit ke  {0}".format(flipbit)
    
    print(msg)
    
    s = s[:flipbit-1] + ('1' if s[flipbit-1] == '0' else '0') + s[flipbit:]
    
    print(s)

else:
    
    print(">>> Tidak ada error")


print(">>> hapus kode deteksi ")

t = ""

for i, c in enumerate(s):
    
    if i+1 not in [1, 2, 4, 8, 16, 32, 64, 128]:
        
        t += c

print(t)

print(">>> Convert ke char")

sol = "".join(chr(int(t[i:i+8], 2)) for i in range(0, len(t), 8))

print(sol)
```
#### ara2021{tr0olLy0u}
