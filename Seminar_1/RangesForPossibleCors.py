# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой
# четверти (x и y).


import random as rand


def check_cors_for_plane(plane_num):
    if plane_num == 1:
        return rand.randint(1, 10), rand.randint(1, 10)
    elif plane_num == 2:
        return rand.randint(-10, 0), rand.randint(1, 10)
    elif plane_num == 3:
        return rand.randint(-10, 0), rand.randint(-10, 0)
    elif plane_num == 4:
        return rand.randint(1, 10), rand.randint(-10, 0)


plane_n = int(input("Введите номер четверти: "))
print(check_cors_for_plane(plane_n))
