# Из предложенного текстового файла (text18-31.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить строку наименьшей длины.

a=open("text18-31.txt", "r", encoding="UTF-8")
b=a.read()
lines = 0
for line in b:
    if line.isalpha():
        lines += 1
print(a)
print(b)
print("символы >> ", lines)



c=(list(b))
v = 0
x = 0
f = 0
my_sp = []
my_sp2 = []
my_sp3 = []
line = b.replace('\n', "")
spisok2 = ['!']
while v < len(c): #цикл работающий пока переменная v меньше чем длинна строки
    if c[f] == '!': #условие выполняющееся если при переборе элементов строки
        my_sp.append(len(c[x:f]))
        my_sp2.append(c[x:f+1])
        x = f+1
    f += 1
    v += 1
my_sp3.append(c[74:f])
line2 = (list(my_sp2))
line2 = line2


a.close()
print(line)

print(min(my_sp))
print(line2)
print(line3)