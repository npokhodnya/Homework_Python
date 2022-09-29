# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# 6782 -> 23
# 0,56 -> 11

def sum_of_digits(num: str):
    sum_ = 0
    for i in range(len(num)):
        if num[i].isdigit():
            sum_ += int(num[i])
    return sum_


n = input()
print(sum_of_digits(n))
