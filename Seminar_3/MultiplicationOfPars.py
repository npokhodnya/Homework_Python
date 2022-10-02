# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
#     Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiply_of_pars(origin_lst: list):
    result = list()
    repeats = len(origin_lst) // 2 if len(origin_lst) % 2 == 0 else len(origin_lst) // 2 + 1
    for i in range(repeats):
        result.append(origin_lst[i] * origin_lst[len(origin_lst) - (i + 1)])
    return result


test_1 = [2, 3, 4, 5, 6]
print(multiply_of_pars(test_1))
test_2 = [2, 3, 5, 6]
print(multiply_of_pars(test_2))
