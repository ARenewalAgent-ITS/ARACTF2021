# Gordon
---
## Deskripsi
"Omong-omong soal mentah, gue lagi ngotak-atik SD Card yang tadi jatuh di jalan, gue liat tadi RATA dong di jalan, terus nemu file ini. Gue ga bisa baca sih, tapi ya kayanya isinya menarik."
"Mas, ini warteg"

## Solusi
1. Peserta mendapat file data.dat sebesar 1440000 bytes.
2. File tersebut merupakan RGB dari suatu gambar dengan ukurannya sama dengan warteg.jpg
3. Kemudian merecover gambar tersebut 
```
from PIL import Image
import numpy as np
im = Image.open('warteg.jpg')
a = np.array(np.asarray(im))
data = open("data.dat", "rb").read()
c = 0
for i in range(500):
for j in range(960):
for k in range(3):
a[i][j][k] = data[c]
c += 1
im = Image.fromarray(a)
im.save("gordon.jpg")
```
4. file gambar dapat dilihat


#### ara2021{flatten_every_pixel_to_make_it_raw}
