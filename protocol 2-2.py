import random
import time
import hashlib

p = random.randint(509,512)
q = random.randint(254,256)

i = 0

while i == 0:
    a = random.randint(1,20)
    if (a ** 13) % p == 1:
        i += 1
    time.sleep(0.5)

x = random.randint(1,20)

y = (a ** x) % p

print ('простое число p = {}'.format(p))
print ('закрытый ключ х = {}'.format(x))
print ('открытый ключ у = {}'.format(y))

h = hashlib.md5(b'KOM') #хэш-образ
print (h)
i = 0
while i == 0:
    k = random.randint(1, 30)
    w = (a ** k) % p
    wl = w % q
    if wl != 0:
        s = ((x * wl) + (k * h)) % q
        if s != 0:
            i += 1
    time.sleep(0.5)

print (s)

v = (h ** (q-2)) % q

z1 = (s * v) % q
z2 = ((q-wl) % p) % q

u = (((a ** z1)*(y ** z2)) % p) % q

print (u)