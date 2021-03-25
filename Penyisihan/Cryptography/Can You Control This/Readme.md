# Can You Control This
---
## Deskripsi
Seseorang berkata kepada saya mengenai kontrol dan cek , namun saya tidak paham apa yang dimaksud orang itu hmmm.
NB : Flag terbagi menjadi 2 bagian
## Solusi
Pada soal ini terdapat 2 buah celah yang dapat digunakan untuk mendapatkan 2 buah flag. Flag pertama dapat diperoleh dengan memanfaatkan celah pada AES CTR dengan known partial text dan menggunakan fungsi zlib compress ( dengan asumsi compress akan 
menghasilkan panjang paling pendek jika string yang sama diulang beberapa kali ). Flag kedua dapat diperoleh dengan memanfaatkan celah bit flip attack pada token yang disediakan melalui fungsi import key. 
Berikut solver yang kami gunakan
```
from Crypto.Util.number import long_to_bytes 
from pwn import * 
import json 
import string 
#r=process(["python3","main.py"]) 
r=remote(server,port) 
r.recvuntil("Payload : ") 
r.sendline('{"action":"import_key","key":"2121202120212021202120212021202120212021 202120212021202120212021"}') 
token=json.loads(r.recvline().strip()) 
token=bytes.fromhex(token["token"]) 
enc=token[:-16] 
iv=list(token[-16:]) 
iv[0]=iv[0]^0x21^0x20 
iv=bytes(iv) 
payload=bytes.hex(enc+iv) 
r.recvuntil("Payload : ") 
r.sendline('{"action":"getSecondFlag","token":"'+payload+'"}') 
flag=json.loads(r.recvline().strip()) 
flag2=long_to_bytes(flag["flag2"]).decode() 
s = string.printable 
flag1 = 'ara202' 
cnt=1 
while cnt<11: 
 min_len = 10000
 req_char = '' 
 for i in s: 
  next_char = i 
  plain_text = flag1 + i 
  if len(plain_text) > 9: 
   plain_text = plain_text*2 
  else: 
   plain_text = plain_text*5 
  plain_text = plain_text.encode().hex() 
  r.recvuntil("Payload : ") 
  r.sendline('{"action":"encrypt","plaintext":"'+plain_text+'","token":"'+payload+'"}') data = json.loads(r.recvline().strip()) 
  l = len(bytes.fromhex(data["ciphertext"])) 
  if l < min_len: 
   req_char = i 
  min_len = l 
  flag1 += req_char 
  cnt+=1 
print(flag1+flag2)
```
#### ara2021{CnTr7_Th3_b1Tss}
