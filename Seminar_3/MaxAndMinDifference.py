# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
#
#     Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def max_min_reminder(origin_list: list):
    max_ = origin_list[0] % 1
    min_ = origin_list[0] % 1
    for i in range(len(origin_list)):
        current = origin_list[i] % 1
        if current != 0:
            if current > max_:
                max_ = current
            elif current < min_:
                min_ = current
    return max_, min_


def diff(_max, _min):
    return _max - _min


test = [1.1, 1.2, 3.1, 5, 10.01]
result = max_min_reminder(test)
print(round(diff(result[0], result[1]), 2))
