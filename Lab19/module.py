from math import pi

class Square:

    def rectangle(a, b):
        print('Площадь прямоугольника-', a * b)

    def triangle(a, h):
        print('Площадь треугольника-', 1/2*(a * h))

    def circle(r):
        print('Площадь круга-', round(pi * r**2, 4) )
