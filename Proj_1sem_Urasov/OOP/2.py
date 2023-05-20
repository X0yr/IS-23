class rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_pr(self):
        return 2*(self.h + self.w)

class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a
class traingle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = a
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c

r1 = rectangle(1, 2)
r2 = rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = traingle(3, 2, 1)
t2 = traingle(4, 3, 2)
# print(r1.get_rect_pr(), r2.get_rect_pr())
# print(s1.get_sq_pr(), s2.get_sq_pr())

geon = [rectangle(1, 2), rectangle(3, 4),
        Square(10), Square(20),
        traingle(3, 2, 1), traingle(4, 3, 2)]

for g in geon:
    print(g.get_pr())
