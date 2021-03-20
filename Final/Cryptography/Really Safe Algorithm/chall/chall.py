from gmpy2 import *
from Crypto.Util.number import *
import random

bits = 2048

def generateConst():
    f = open("/dev/urandom","rb")
    const = bytes_to_long(f.read(32))
    f.close()
    
    prime = getStrongPrime(bits//4)
    
    count = 10
    shift = 360
    
    xxx = []
    aaa = []
    yyy = []
    bbb = []
    zzz = []
    for i in range(count):
        xxx.append(random.randint(2, prime-1))
    for i in xxx:
        aaa.append(i * const)
    for i in aaa:
        yyy.append(i % prime)
    for i in yyy:
        bbb.append(i >> shift)
    for i in bbb:
        zzz.append(i << shift)

    return const,prime,xxx,zzz

def GenerateFactor():
    p = getStrongPrime(bits)
    q = getStrongPrime(bits)

    return p, q

def CalculateKeys(p, q, const):
    e = 65537
    n = p * q
    phi = (p-1)*(q-1)
    d = inverse(e, phi)
    f = d*(p-const)

    return e, n, f

def Encrypt(flag,const):

    p, q = GenerateFactor()
    e, n, f = CalculateKeys(p, q, const)

    for i in range(bits//8):
        flag += b"!"
    flag = bytes_to_long(flag)

    c = pow(flag, e, n)
    
    return c,n,f

if __name__ == '__main__':
    flag = b"ara2021{flag}"
    const,prime,xxx,zzz = generateConst()
    c,n,f = Encrypt(flag,const)
    print("[*] c : %d\n" % c)
    print("[*] n : %d\n" % n)
    print("[*] f : %d\n" % f)
    print("[*] prime: ",prime,"\n")
    print("[*] xxx :",xxx,"\n")
    print("[*] zzz :",zzz,"\n")

