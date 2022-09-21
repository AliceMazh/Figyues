import math

class figures():
    def __init__(self):
        pass
    def triangle(self, a, b, c):
        p = (a + b + c) / 2
        return math.sqrt((p*(p-a)*(p-b)*(p-c)))
    def rectandle(self, a, b):
        return a*b
    def circle(self, a):
        a = float(a)
        return math.ceil(math.pi*(a**2))

def main():
    tip = str(input("Введите название фигуры ="))
    f=figures()
    if tip =="треугольник":
        a=float(input("Введите сторону a ="))
        b=float(input("Введите сторону b ="))
        c=float(input("Введите сторону c ="))
        return f.triangle(a, b, c)
    elif tip =="прямоугольник":
        a=float(input("Введите сторону a ="))
        b=float(input("Введите сторону b ="))
        return f.rectandle(a, b)
    elif tip == "круг":
        a=float(input("Введите радиус a ="))
        return f.circle(a)

#print(main())