try:
    N=int(input('введите число >>> '))
    a=[]
    y=0
    while y<N:
        a.append(random.randint(1, 100))
        y+=1
    K=int(input('введите число от 1 до 100 >>> '))
    B=[]
    j=0
    while j < N:
        B.append(random.randint(1, 100))
        j+= 1
    h=0
    B[K]=(sum(a))/K
    print(B)
except:
    print('Error')
