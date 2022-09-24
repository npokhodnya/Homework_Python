# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка

def check_plane(x, y):
    if x > 0 < y:
        return 1
    elif x < 0 < y:
        return 2
    elif x < 0 > y:
        return 3
    elif x > 0 > y:
        return 4


x_cor = int(input("Введите x: "))
y_cor = int(input("Введите y: "))
print(check_plane(x_cor, y_cor))
