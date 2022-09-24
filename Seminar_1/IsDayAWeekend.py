# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот
#    день выходным.
#
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


def is_weekend(num_of_day):
    if 0 < num_of_day < 8:
        if num_of_day == 6 or num_of_day == 7:
            return "да"
        else:
            return "нет"
    else:
        return f"Число {num_of_day} не является днём недели!"


try:
    num = int(input("Введите номер дня недели: "))
    print(is_weekend(num))
except ValueError:
    print('Введённый параметр не является числом!')
