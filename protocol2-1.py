import random


h = random.randint(1, 128) #хэш-образ
dA = random.randint(1,20) #закрытый ключ отправителя А
nA = random.randint(1,20) #часть открытого ключа А
eA = random.randint(1,20) #открытый ключ А

s = (h ** dA) % nA #Цифровая подпись

print ('Цифровая подпись = {}'.format(s))

hl = 0

hl = (s ** eA) % nA #Вычисление хэш-образа
print ('=========')
print (hl)
print (h)
