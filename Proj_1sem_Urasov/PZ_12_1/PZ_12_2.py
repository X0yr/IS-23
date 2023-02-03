# Из заданной строки отобразить только символы нижнего регистра.
# Использовать библиотеку string. Строка 'In PyCharm, you can specify third-party standalone
# applications and run them as External Tools'.

import string #заводим библиотеку string

st_1 = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
answer = list(filter(lambda x:x in string.ascii_lowercase, st_1)) #создаём лист, в который с помошью lambda фунции занесутся все символы нижнего региста строки st_1

print("Символы нижнего регистра >>>", answer)