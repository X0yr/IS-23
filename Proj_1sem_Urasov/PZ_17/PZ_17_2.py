# Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год
# выпуска". От этого класса унаследуйте класс "Автомобиль" и добавьте в него
# свойство "тип кузова".


class transport:

    def __init__(self, marka, model, god_vipuska):
        self.marka = marka
        self.model = model
        self.god_vipuska = god_vipuska

    def osnov(self):
        return  self.marka, self.model, self.god_vipuska

class avto(transport):

    def __init__(self, svoistvo, tip_kuzova):
        self.svoistvo = svoistvo
        self.tiv_kuzova = tip_kuzova

    def dop(self):
        return self.svoistvo, self.tiv_kuzova


avto1 = transport("Сузуки", "Кизаши", "C 2009 по 2014")
avto2 = avto("Салон неплохо скроен и крепко сшит. В Kizashi не возникает ощущения, будто сидишь в пластиковой скорлупе.", "Седан")
print(avto1.osnov())
print(avto2.dop())
