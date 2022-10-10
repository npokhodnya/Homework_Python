# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# *Пример*
#
# - при N=236     ->        [2, 2, 59]

def prime_fctors(num):
    i = 2
    res = []
    while num > 1:
        if num % i == 0:
            num /= i
            res.append(i)
        else:
            i += 1
    return res


n = int(input("N: "))
print(prime_fctors(n))
