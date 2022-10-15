# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# 6782 -> 23
# 0,56 -> 11


# Было:
def sum_of_digits(num: str):
    sum_ = 0
    for i in range(len(num)):
        if num[i].isdigit():
            sum_ += int(num[i])
    return sum_


n = input()
print(sum_of_digits(n))


# Стало:
def sum_of_digits_new(num: str):
    return sum([int(num[i]) for i in range(len(num)) if num[i].isdigit()])


print(sum_of_digits_new(n))
