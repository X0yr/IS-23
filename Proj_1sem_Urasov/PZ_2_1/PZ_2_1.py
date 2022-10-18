try:
    a=int(input('введите число от 1 до 365 '))
    print('Error')
if a % 7 == 1:
    print('Вторник')
if a % 7 == 2:
    print('Среда')
if a % 7 == 3:
    print('Четверг')
if a % 7 == 4:
    print('Пятница')
if a % 7 == 5:
    print('Суббота')
if a % 7 == 6:
    print('Воскресенье')
if a % 7 == 0:
    print('Понедельник')
except:
    print('error')