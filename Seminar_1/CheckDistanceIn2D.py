# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


def check_distance_2d(xa, ya, xb, yb):
    return round((((xa - xb) ** 2) + ((ya - yb) ** 2)) ** 0.5, 2)


x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))
print(check_distance_2d(x1, y1, x2, y2))
