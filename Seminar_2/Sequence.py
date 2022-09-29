# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def create_sequence(number):
    result_list = []
    for i in range(1, number + 1):
        result_list.append(factorial(i))
    return result_list


n = int(input())
print(create_sequence(n))
