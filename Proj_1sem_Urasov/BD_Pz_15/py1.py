#От таблицы Состав отказались, согласованно с преподавателем
#От таблицы Состав отказались, согласованно с преподавателем


import sqlite3 as sq


print("Задание SELECT №1. Вывести список всех товаров и их описания:")
with sq.connect('Opt. base') as con:
    cur = con.cursor()
    cur.execute("SELECT name_tov, opis FROM goods")
    result = cur.fetchall()
print(result)

# print("Задание SELECT №2. Вывести список всех магазинов и их адресов:")
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("SELECT nazv_mag, address FROM shop") 
#     result = cur.fetchall()
# print(result)

# print("Задание SELECT №3. Вывести список всех заявок магазинов и даты, на которые они были поданы:")
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("SELECT id_mag, date_zayav FROM store_statements") 
#     result = cur.fetchall()
# print(result)

# print("Задание SELECT №4. Вывести список товаров и количество их наличия на складе:")
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("SELECT id_kol_tov, kol_vo FROM number_of_goods_in_stock") 
#     result = cur.fetchall()
# print(result)

# print("Задание SELECT №5. Вывести список товаров и количество их наличия на складе в порядке убывания количества:")
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("SELECT id_kol_tov, kol_vo FROM number_of_goods_in_stock ORDER BY kol_vo DESC") 
#     result = cur.fetchall()
# print(result)

# print("Задание SELECT №6. Вывести список всех заявок магазинов и товаров, которые были в них заказаны:")
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("SELECT id_zayav, id_tov FROM compound") 
#     result = cur.fetchall()
# print(result)

# print("Задание SELECT №7. Вывести список всех товаров, у которых на складе количество меньше минимально допустимого:")
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("SELECT id_kol_tov FROM number_of_goods_in_stock WHERE kol_vo < 1000") 
#     result = cur.fetchall()
# print(result)


# print("Задание SELECT №8. Вывести список всех заявок магазинов, которые были сделаны в определенный период времени:")
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("SELECT id_mag FROM store_statements WHERE date_zayav BETWEEN '2022-08-015' AND '2022-11-30' ") 
#     result = cur.fetchall()
# print(result)

# print("Задание SELECT №9. Вывести список всех магазинов, у которых суммарное количество товаров на складе меньше заданного значения:")
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("SELECT id_mag FROM number_of_goods_in_stock WHERE kol_vo < 7000") 
#     result = cur.fetchall()
# print(result)

# # Задание UPDATE №1. 
# # Обновить количество товара на складе для конкретного товара
# with sq.connect('Opt. base') as con: 
#    cur = con.cursor()
#    cur.execute("UPDATE number_of_goods_in_stock SET kol_vo=4999 WHERE id_kol_tov = 21")
    
# # Задания 2 и 3 преподаватель разрешил не делать.

# #Задание UPDATE №4. 
# #Обновить адрес магазина, который подал заявку
# with sq.connect('Opt. base') as con: 
#    cur = con.cursor()
#    cur.execute("UPDATE shop SET address='ул. Победная' WHERE id_mag=(SELECT id_mag FROM store_statements WHERE id_zayav=34)")
    
# # Задание UPDATE №5. 
# # Обновить дату заявки для конкретного магазина
# with sq.connect('Opt. base') as con: 
#    cur = con.cursor()
#    cur.execute("UPDATE store_statements SET date_zayav='2022-09-25' WHERE id_mag = 12")

# # Задание UPDATE №6. 
# # Обновить количество товара на складе для нескольких товаров
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("UPDATE number_of_goods_in_stock SET kol_vo=2000 WHERE (id_kol_tov = 24) or (id_kol_tov = 27)")

# # Задание UPDATE №7.
# # Обновить описание товара и количество на складе для конкретного товара
# with sq.connect('Opt. base') as con: 
#    cur = con.cursor()
#    cur.execute("UPDATE goods SET opis='Домашнее' WHERE id_tov = 10")
#    cur.execute("UPDATE number_of_goods_in_stock SET kol_vo=950 WHERE id_kol_tov = 30")

# # Задание UPDATE №8. 
# # Обновление количества товаров на складе, учитывая выполненную заявку магазина
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("UPDATE number_of_goods_in_stock SET kol_vo=((SELECT kol_vo FROM number_of_goods_in_stock WHERE id_kol_tov=(SELECT id_tov FROM compound WHERE id_zayav=31)) - (SELECT SUM(kol_vo) FROM compound WHERE id_tov=(SELECT id_tov FROM compound WHERE id_zayav=31))) WHERE id_tov=(SELECT id_tov FROM compound WHERE id_zayav=31)")    

# # Задание UPDATE №9. 
# # Обновление количества товаров на складе, учитывая выполненную заявку магазина с учетом конкретного товара
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("UPDATE number_of_goods_in_stock SET kol_vo=((SELECT kol_vo FROM number_of_goods_in_stock WHERE id_kol_tov=22) - (SELECT SUM(kol_vo) FROM compound WHERE id_tov=3)) WHERE id_tov=3")

# # Задание UPDATE №10. 
# # Обновить название магазина, который подал заявку, и адрес магазина для конкретной заявки.
# with sq.connect('Opt. base') as con: 
#    cur = con.cursor()
#    cur.execute("UPDATE shop SET nazv_mag='Любовь', address='ул. Космонавтова' WHERE id_mag=(SELECT id_mag FROM store_statements WHERE id_zayav = 32)")
    
# # Отказались от 11 задания

# # Задание UPDATE №12. 
# # Обновить адрес магазина и количество товара в заявке для конкретного товара
# with sq.connect('Opt. base') as con: 
#    cur = con.cursor()
#    cur.execute("UPDATE shop SET address='ул. Чикайловская' WHERE id_mag= (SELECT id_mag FROM store_statements WHERE id_zayav=(SELECT id_zayav FROM compound WHERE id_tov=10))")
#    cur.execute("UPDATE compound SET kol_vo=896 WHERE id_tov=10")

# # Задание UPDATE №13. 
# # Обновить описание товара и количество на складе для нескольких товаров
# with sq.connect('Opt. base') as con: 
#    cur = con.cursor()
#    cur.execute("UPDATE goods SET opis='Фрукты\Овощи' WHERE (id_tov = 2) or (id_tov=7)")
#    cur.execute("UPDATE number_of_goods_in_stock SET kol_vo=7000 WHERE (id_tov = 2) or (id_tov=7)")

# # Задание DELETE №1. 
# # Удаление заявки магазина и соответствующих записей в таблице состава
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("DELETE FROM store_statements WHERE id_zayav=39")
#     cur.execute("DELETE FROM compound WHERE id_zayav=39")

# # Задание DELETE №2.
# # Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, не имеющим заявок в таблице "Состав"
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("DELETE FROM number_of_goods_in_stock WHERE id_tov=5")
    
# # Задание DELETE №3. 
# # Удалить из таблицы "Заявки магазинов" все заявки магазинов, адрес которых начинается на "ул. Ленина"
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("DELETE FROM store_statements WHERE id_mag IN (SELECT id_mag FROM shop WHERE address LIKE 'ул. Ленина')")
    
# # Задание DELETE №4.
# # Удалить из таблицы "Состав" записи, соответствующие товарам, которых нет на складе (количество = 0)
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("DELETE FROM compound WHERE id_tov IN (SELECT id_tov FROM number_of_goods_in_stock WHERE kol_vo=0)")

# # Задание DELETE №5. 
# # Удалить из таблицы "Магазины" магазины, в которых не было заявок в течение последнего месяца
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("DELETE FROM shop WHERE id_mag NOT IN (SELECT id_mag FROM store_statements WHERE date_zayav BETWEEN '2022-11-30' AND '2023-01-29')")

# Задание DELETE №6. 
# Удалить из таблицы "Товары" товары, которые не были заказаны ни разу
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("DELETE FROM goods WHERE id_tov NOT IN (SELECT id_tov FROM compound)")
    
# # Задание DELETE №7. 
# # Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, которые не были заказаны ни разу
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("DELETE FROM number_of_goods_in_stock WHERE id_kol_tov NOT IN (SELECT id_tov FROM compound)")
    
# # Задание DELETE №8. 
# # Удалить из таблицы "Состав" записи, соответствующие заявкам, которые были поданы более месяца назад
# with sq.connect('Opt. base') as con: 
#     cur = con.cursor()
#     cur.execute("DELETE FROM compound WHERE id_zayav IN (SELECT id_zayav FROM store_statements WHERE date_zayav BETWEEN '2022-11-30' AND '2023-01-29')")