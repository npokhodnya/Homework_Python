# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.
#
# *Пример*
#
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

def unique(lst: list):
    res = []
    for element in lst:
        if element in res:
            continue
        elif lst.count(element) == 1:
            res.append(element)
    return res


test = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
print(unique(test))
