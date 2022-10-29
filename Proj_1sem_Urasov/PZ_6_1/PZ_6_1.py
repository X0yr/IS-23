import random
def bbb(v):
    a = []
    for m in v:
        if m % 2 == 1:
            a.append(m)
    return a
try:
    N=int(input('введите число >>> '))
    a=[]
    y=0
    while y<N:
        a.append(random.randint(1, 1000))
       y+=1
    s=bbb(a)
    j=len(s)
    p=0
    if s != []:
       for p in range(j):
           s[p]+s[-1]
           p+=1
       print(s)
    else:
       print(a)
except:
    print('Error')
