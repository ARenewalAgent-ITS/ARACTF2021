# Fire Wheel
---
## Deskripsi
"Pendekar pedang itu melompat ke belakang lawan dan berputar di udara sambil melepaskan serangan api dalam gerakan melingkar."

Kalian akan mendapatkan flag jika kalian mampu menemukan key yang tepat untuk melewati validasi!
## Solusi
Diberikan sebuah file ELF namun terdapat perubahan pada headernya sehingga berikut
hasilnya ketika dicheck menggunakan command file

Kita tidak dapat membukanya menggunakan IDA dan melakukan dynamic analysis kecuali
melakukan patching. Jadi untuk membukanya kita bisa melakukan scripting untuk mencari
entry point lalu melakukan disassembly mulai dari entry point tersebut sampai selesai.


```
from capstone import *
from ctypes import *
import io
class ELF64FileHeader(Structure):
_fields_ = [
("e_indent", c_char * 16),
("e_type", c_uint16),
("e_machine", c_uint16),
("e_version", c_uint32),
("e_entry", c_uint64),
("e_phoff", c_uint64),
("e_shoff", c_uint64),
("e_flags", c_uint32),
("e_ehsize", c_uint16),
("e_phentsize", c_uint16),
("e_phnum", c_uint16),
("e_shentsize", c_uint16),

Selanjutnya tinggal menganalisis kode assembly yang dihasilkan. ( atau bisa dengan
command berikut ( objdump -D -b binary -m i386:x86-64 -M intel checker ) )
("e_shnum", c_uint16),
("e_shstrndx", c_uint16),
]
class ELF64ProgramHeader(Structure):
_fields_ = [
("p_type", c_uint32),
("p_offset", c_uint32),
("p_vaddr", c_uint64),
("p_paddr", c_uint64),
("p_filesz", c_uint64),
("p_flags", c_uint64),
("p_memsz", c_uint64),
("p_align", c_uint64),
]
stream = io.BytesIO(open("checker", "rb").read())
header = ELF64FileHeader()
stream.readinto(header)
print("----- ELF header -----")
print(f"e_type: {header.e_type}")
print(f"e_machine: {header.e_machine} => x86_64")
print(f"e_entry: {hex(header.e_entry)}")
print(f"e_phoff: {hex(header.e_phoff)}")
print(f"e_shoff: {hex(header.e_shoff)}")
print(f"e_phnum: {hex(header.e_phnum)}")
print(f"e_shnum: {hex(header.e_shnum)}")
stream.seek(header.e_phoff)
phdr = ELF64ProgramHeader()
stream.readinto(phdr)
print("----- Program header -----")
print(f"p_type: {phdr.p_type}")
print(f"p_offset: {hex(phdr.p_offset)}")
print(f"p_vaddr: {hex(phdr.p_vaddr)}")
print(f"p_paddr: {hex(phdr.p_paddr)}")
print(f"p_memsz: {hex(phdr.p_memsz)}")
print(f"p_filesz: {hex(phdr.p_filesz)}")
stream.seek(0xa2)
code = stream.read(-1)
md = Cs(CS_ARCH_X86, CS_MODE_64)
print("----- disassemble -----")
for i in md.disasm(code, 0x4000a2):
print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
```
Selanjutnya tinggal menganalisis kode assembly yang dihasilkan. ( atau bisa dengan
command berikut ( objdump -D -b binary -m i386:x86-64 -M intel checker ) )

```
----- disassemble -----
0x4000a2: xor eax, eax
0x4000a4: sub rsp, 0x10
0x4000a8: xor eax, eax
0x4000aa: mov r8, rsp

0x4000ad: xor eax, eax
0x4000af: sub rsp, 0x10
0x4000b3: xor eax, eax
0x4000b5: mov r9, rsp
0x4000b8: xor eax, eax
0x4000ba: pxor xmm0, xmm0
0x4000be: xor eax, eax
0x4000c0: movaps xmmword ptr [rsp], xmm0
0x4000c4: xor eax, eax
0x4000c6: movaps xmmword ptr [rsp + 0x10], xmm0
0x4000cb: xor eax, eax
0x4000cd: mov esi, 0x400070
0x4000d2: xor eax, eax
0x4000d4: mov edx, 7
0x4000d9: call 0x400095
0x4000de: xor eax, eax
0x4000e0: xor edi, edi
0x4000e2: mov rsi, r8
0x4000e5: mov edx, 0x10
0x4000ea: syscall
0x4000ec: mov rax, qword ptr [r8]
0x4000ef: xor qword ptr [r9], rax
0x4000f2: mov rax, qword ptr [r8 + 8]
0x4000f6: xor qword ptr [r9 + 8], rax
0x4000fa: add rax, 5
0x4000fe: sub rax, 1
0x400102: add rax, 7
0x400106: sub rax, 0xb
0x40010a: rol qword ptr [r9], 0x39
0x40010e: ror qword ptr [r9 + 8], 0x13
0x400113: mov rax, qword ptr [0x400000]
0x40011b: xor qword ptr [r9], rax
0x40011e: add rax, 9
0x400122: sub rax, 3
0x400126: add rax, 7
0x40012a: sub rax, 0xd
0x40012e: mov rax, qword ptr [0x400008]
0x400136: xor qword ptr [r9 + 8], rax
0x40013a: mov rax, qword ptr [0x400028]
0x400142: xor rax, qword ptr [r9]
0x400145: add rax, 7
0x400149: sub rax, 6
0x40014d: add rax, 3
0x400151: sub rax, 4
0x400155: mov rdx, qword ptr [0x400030]
0x40015d: xor rdx, qword ptr [r9 + 8]
0x400161: and rax, rax
0x400164: nop
0x400165: nop
0x400166: nop
0x400167: nop
0x400168: jne 0x4001b7
0x40016a: nop
0x40016b: nop

Disini terdapat beberapa jebakan seperti menggunakan instruksi sub dan add dengan
operand register dan konstanta jadi kita bisa skip instruksi tersebut. Selain itu instruksi xor
eax,eax yang tidak penting juga dan nop dapat kita skip sehingga berikut hasil dari
pembersihan kode assembly tersebut.
0x40016c: cmp rax, rdx
0x40016f: jne 0x4001b7
0x400171: mov esi, 0x400078
0x400176: mov edx, 0x1a
0x40017b: add edx, 7
0x40017e: sub edx, 3
0x400181: add edx, 1
0x400184: sub edx, 4
0x400187: nop
0x400188: call 0x400095
0x40018d: mov rsi, r8
0x400190: mov edx, 0x10
0x400195: call 0x400095
0x40019a: mov esi, 0x400093
0x40019f: mov edx, 2
0x4001a4: add edx, 3
0x4001a7: add edx, 4
0x4001aa: sub edx, 2
0x4001ad: sub edx, 5
0x4001b0: call 0x400095
0x4001b5: jmp 0x4001c6
0x4001b7: mov esi, 0x400058
0x4001bc: mov edx, 8
0x4001c1: call 0x400095
0x4001c6: mov eax, 0x3c
0x4001cb: xor edi, edi
0x4001cd: syscall
```

Disini terdapat beberapa jebakan seperti menggunakan instruksi sub dan add dengan
operand register dan konstanta jadi kita bisa skip instruksi tersebut. Selain itu instruksi xor
eax,eax yang tidak penting juga dan nop dapat kita skip sehingga berikut hasil dari
pembersihan kode assembly tersebut.

```
----- disassemble -----
0x4000a4: sub rsp, 0x10
0x4000aa: mov r8, rsp
0x4000af: sub rsp, 0x10
0x4000b5: mov r9, rsp
0x4000ba: pxor xmm0, xmm0
0x4000c0: movaps xmmword ptr [rsp], xmm0
0x4000c6: movaps xmmword ptr [rsp + 0x10], xmm0
0x4000cd: mov esi, 0x400070
0x4000d4: mov edx, 7
0x4000d9: call 0x400095
# read(stdin, 0x10, r8)
0x4000de: xor eax, eax
0x4000e0: xor edi, edi
0x4000e2: mov rsi, r8
0x4000e5: mov edx, 0x10
0x4000ea: syscall

# r9 <= r8 (first 8 byte)
0x4000ec: mov rax, qword ptr [r8]
0x4000ef: xor qword ptr [r9], rax
# r9 + 8 <= r8 + 8 (second 8 byte)
0x4000f2: mov rax, qword ptr [r8 + 8]
0x4000f6: xor qword ptr [r9 + 8], rax
# r9 rotate left 0x39 bit
0x40010a: rol qword ptr [r9], 0x39
# r9+8 rotate right 0x13 bit
0x40010e: ror qword ptr [r9 + 8], 0x13
# r9 xor with value in 0x400000
0x400113: mov rax, qword ptr [0x400000]
0x40011b: xor qword ptr [r9], rax
# r9 xor with value in 0x400008
0x40012e: mov rax, qword ptr [0x400008]
0x400136: xor qword ptr [r9 + 8], rax
# rax = r9 xor with value in 0x400028
0x40013a: mov rax, qword ptr [0x400028]
0x400142: xor rax, qword ptr [r9]
# rdx = r9 xor with value in 0x400030
0x400155: mov rdx, qword ptr [0x400030]
0x40015d: xor rdx, qword ptr [r9 + 8]
# rax != 0 -> wrong
0x400161: and rax, rax
0x400168: jne 0x4001b7
# rax != rdx -> wrong
0x40016c: cmp rax, rdx
0x40016f: jne 0x4001b7
0x400171: mov esi, 0x400078
0x400176: mov edx, 0x1a
0x400187: nop
0x400188: call 0x400095
0x40018d: mov rsi, r8
0x400190: mov edx, 0x10
0x400195: call 0x400095
0x40019a: mov esi, 0x400093
0x40019f: mov edx, 2
0x4001b0: call 0x400095
0x4001b5: jmp 0x4001c6
0x4001b7: mov esi, 0x400058
0x4001bc: mov edx, 8
0x4001c1: call 0x400095
0x4001c6: mov eax, 0x3c
0x4001cb: xor edi, edi
0x4001cd: syscall
```
dan berikut adalah solvernya
```
import binascii
import struct
def rol(x, shift):
return ((x << shift) | (x >> (64 - shift))) & 0xffffffffffffffff
def ror(x, shift):
return ((x >> shift) | (x << (64 - shift))) & 0xffffffffffffffff
def unhex(x):
return binascii.unhexlify(hex(x)[2:])[::-1]
with open('checker', 'rb') as f:
elf = f.read()
k1, k2 = struct.unpack('QQ', elf[:0x10])
k3, k4 = struct.unpack('QQ', elf[0x28:0x38])
flag = ''
flag += unhex(ror(k1 ^ k3, 57)).decode()
flag += unhex(rol(k2 ^ k4, 0x13)).decode()
print(flag)
```

#### ara2021{r0t4t3__t1ny_x0r}
