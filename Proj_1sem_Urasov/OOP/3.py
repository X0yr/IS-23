class Person:
    def __init__(self, imya, familia, cvalifik = 1):
        self.imya = imya
        self.familia = familia
        self.cvalifik = cvalifik

    def info1(self):
        print(self.imya, self.familia, self.cvalifik)
    
    def destract(self):
        print("До свидани, мистер", self.familia, self.imya)
        info1 = [self.imya, self.familia, self.cvalifik]
        for i in info1:
            del i

PersonInf = Person("Иван", "Серов", 1)
print(PersonInf.info1())

