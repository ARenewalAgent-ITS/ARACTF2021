# Big Dict
---
## Deskripsi
Ndak bisa bahasa enggres?.

XWZYYXWXYZXWZYYXYXYZXYXYWXYXYZXYXYYXWXXXXWXYXXYXYXXWXYXXWXWYXWZYYXWZXYXWYZXXWZWWXYXYXXWZZZXWZWXXWZYYXWZZZXWYZXXWZXXXWZYZXWZYZXWZXYXWXZY
## Solusi
Dari source code tersebut sebenarnya passkey tidak terlalu dibutuhkan karena digunakan sekali. Dari Situ kita dapat mengubah source code tersebut menjadi seperti ini
```
passkey = '******'
wut = {'10':'X', '01':'W', '00':'Y', '11':'Z'}

def encode(words,num):
	cipher = ''
	for word in words:
    	char = bin(ord(word)^num)[2:]
    	for c in range(0,len(char),2):
        	for k,v in wut.items():
            	if ''.join(char[c:c+2]) in k:
                	cipher+=v
	return cipher

```
Kita tahu bahwa word akan di xor dengan sum() dari ord() passkey. passkey akan di lower() dan kemungkinan jumlahnya 6. Kita asumsikan aja jika passwordnya ord(a)*6= 582. Setelah kitu kita masukkan encode maka akan menghasilkan 5 huruf. Kita dapat berasumsi bahwa tiap encode akan menghasilkan 5 huruf
```
>>> encode('a',582)
'XYXWZ'
>>>
```
Kita juga mendapatkan sebuah kumpulan huruf yang bisa kita tebak itu adalah flagnya. 

```
XWZYYXWXYZXWZYYXYXYZXYXYWXYXYZXYXYYXWXXXXWXYXXYXYXXWXYXXWXWYXWZYYXWZXYXWYZXXWZWWXYXYXXWZZZXWZWXXWZYYXWZZZXWYZXXWZXXXWZYZXWZYZXWZXYXWXZY
```
format flag dari ara yaitu ara2021{}. kita bisa asumsikan XWZYY adalah huruf a. Sekarang tingaal kita ubah aja ke binary 1001110000
```
>>> int('1001110000',2)
624
>>>
```
Dengan kita xor dengan word a maka akan didapatkan sum() dari passkeynya yaitu 529
```
>>> 624^97
529

```
Dengan begini kita dapat membuat dictionary sendiri dengan cara
```
>>> d = {encode(chr(s),529):chr(s) for s in range(128)}
>>> d
{'XYWYW': '\x00', 'XYWYY': '\x01', 'XYWYZ': '\x02', 'XYWYX': '\x03', 'XYWWW': '\x04', 'XYWWY': '\x05', 'XYWWZ': '\x06', 'XYWWX': '\x07', 'XYWXW': '\x08', 'XYWXY': '\t', 'XYWXZ': '\n', 'XYWXX': '\x0b', 'XYWZW': '\x0c', 'XYWZY': '\r', 'XYWZZ': '\x0e', 'XYWZX': '\x0f', 'XYYYW': '\x10', 'XYYYY': '\x11', 'XYYYZ': '\x12', 'XYYYX': '\x13', 'XYYWW': '\x14', 'XYYWY': '\x15', 'XYYWZ': '\x16', 'XYYWX': '\x17', 'XYYXW': '\x18', 'XYYXY': '\x19', 'XYYXZ': '\x1a', 'XYYXX': '\x1b', 'XYYZW': '\x1c', 'XYYZY': '\x1d', 'XYYZZ': '\x1e', 'XYYZX': '\x1f', 'XYZYW': ' ', 'XYZYY': '!', 'XYZYZ': '"', 'XYZYX': '#', 'XYZWW': '$', 'XYZWY': '%', 'XYZWZ': '&', 'XYZWX': "'", 'XYZXW': '(', 'XYZXY': ')', 'XYZXZ': '*', 'XYZXX': '+', 'XYZZW': ',', 'XYZZY': '-', 'XYZZZ': '.', 'XYZZX': '/', 'XYXYW': '0', 'XYXYY': '1', 'XYXYZ': '2', 'XYXYX': '3', 'XYXWW': '4', 'XYXWY': '5', 'XYXWZ': '6', 'XYXWX': '7', 'XYXXW': '8', 'XYXXY': '9', 'XYXXZ': ':', 'XYXXX': ';', 'XYXZW': '<', 'XYXZY': '=', 'XYXZZ': '>', 'XYXZX': '?', 'XWWYW': '@', 'XWWYY': 'A', 'XWWYZ': 'B', 'XWWYX': 'C', 'XWWWW': 'D', 'XWWWY': 'E', 'XWWWZ': 'F', 'XWWWX': 'G', 'XWWXW': 'H', 'XWWXY': 'I', 'XWWXZ': 'J', 'XWWXX': 'K', 'XWWZW': 'L', 'XWWZY': 'M', 'XWWZZ': 'N', 'XWWZX': 'O', 'XWYYW': 'P', 'XWYYY': 'Q', 'XWYYZ': 'R', 'XWYYX': 'S', 'XWYWW': 'T', 'XWYWY': 'U', 'XWYWZ': 'V', 'XWYWX': 'W', 'XWYXW': 'X', 'XWYXY': 'Y', 'XWYXZ': 'Z', 'XWYXX': '[', 'XWYZW': '\\', 'XWYZY': ']', 'XWYZZ': '^', 'XWYZX': '_', 'XWZYW': '`', 'XWZYY': 'a', 'XWZYZ': 'b', 'XWZYX': 'c', 'XWZWW': 'd', 'XWZWY': 'e', 'XWZWZ': 'f', 'XWZWX': 'g', 'XWZXW': 'h', 'XWZXY': 'i', 'XWZXZ': 'j', 'XWZXX': 'k', 'XWZZW': 'l', 'XWZZY': 'm', 'XWZZZ': 'n', 'XWZZX': 'o', 'XWXYW': 'p', 'XWXYY': 'q', 'XWXYZ': 'r', 'XWXYX': 's', 'XWXWW': 't', 'XWXWY': 'u', 'XWXWZ': 'v', 'XWXWX': 'w', 'XWXXW': 'x', 'XWXXY': 'y', 'XWXXZ': 'z', 'XWXXX': '{', 'XWXZW': '|', 'XWXZY': '}', 'XWXZZ': '~', 'XWXZX': '\x7f'}

```
Tinggal kita cocokkan kumpulan huruf yang diberikan dengan kamus kita, dengan cara
```
>>> flag = "XWZYYXWXYZXWZYYXYXYZXYXYWXYXYZXYXYYXWXXXXWXYXXYXYXXWXYXXWXWYXWZYYXWZXYXWYZXXWZWWXYXYXXWZZZXWZWXXWZYYXWZZZXWYZXXWZXXXWZYZXWZYZXWZXYXWXZY"
>>> for i in range(0,135,5):
... 	print(d[flag[i:i+5]],end="")
...
ara2021{s3suai_d3ngan_kbbi}

```
#### ara2021{s3suai_d3ngan_kbbi}