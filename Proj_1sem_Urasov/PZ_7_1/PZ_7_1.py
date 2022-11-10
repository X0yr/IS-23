import unittest

# s=str(input("Введдите что-то >>>  "))
# s1=str(input("Введите ещё что-нибудь >>>  "))
# print(s.count(s1))



def colstr(s, s1):
    a=len(s)
    c=len(s1)
    v=0
    x=0
    p=0
    while v<=a:
        if s[x:c] == s1:
           p+=1
        x+=1
        c+=1
        v+=1
    print(p)

s=str(input("Введдите что-то >>>  "))
s1=str(input("Введите ещё что-нибудь >>>  "))
colstr(s, s1)