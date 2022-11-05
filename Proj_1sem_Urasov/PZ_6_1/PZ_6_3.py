import random
try:
    a=[]
    j=int(input('Введите число >>> '))
    u=1
    while u<j:
        a.append(random.randint(1, 100))
        u+=1
    a.sort()
    a.append(random.randint(1, 100))
    a.sort()
    print(a)
except:
    print('Error')