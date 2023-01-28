# Из заданной строки отобразить только символы нижнего регистра.
# Использовать библиотеку string. Строка 'In PyCharm, you can specify third-party standalone
# applications and run them as External Tools'.

import string

st_1 = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
s = string.ascii_uppercase
print(s)
st_1 = st_1.replace(s , "")

print(st_1)