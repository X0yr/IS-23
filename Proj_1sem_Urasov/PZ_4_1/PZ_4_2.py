try:
    N=int(input("Введите число >>> "))
    B=0
    while (N>0) and (B == 0):
        if ((N%10)%2 !=0):
            print('True')
            B = 1
        else:
            N//=10
    if B!=1:
        print('Folse')
except:
    print("error")