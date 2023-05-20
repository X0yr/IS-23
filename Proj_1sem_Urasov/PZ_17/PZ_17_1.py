# Создайте класс «Книга», который имеет атрибуты название, автор и количество
# страниц. Добавьте методы для чтения и записи книги.

class Kniga:
    def __init__(self, nazv, avtor, kol_vo_st):
        self.nazv = nazv
        self.avtor = avtor
        self.kol_vo_st = kol_vo_st

    def Record(self):
        self.nazv = str(input())
        self.avtor = str(input())
        self.kol_vo_st = int(input())

    def Reading(self):
        return  self.nazv, self.avtor, self.kol_vo_st


r = Kniga(0, 0, 0)
print(r.Record())
print(r.Reading())