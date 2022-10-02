# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
#     Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_not_even(list_nums: list):
    """Returns sum of numbers by odd indexes
    Example:
    [2, 3, 5, 9, 3] --> 12 """
    sum_ = 0
    i = 1
    while i < len(list_nums):
        sum_ += list_nums[i]
        i += 2
    return sum_


test = [2, 3, 5, 9, 3]
print(sum_not_even(test))
