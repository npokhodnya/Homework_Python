# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#     Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



def fibo(k):
    fibo_list = [0, 1]
    for i in range(2, k+1):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    for j in range(k):
        fibo_list.insert(0, fibo_list[1] - fibo_list[0])
    return fibo_list


print(fibo(8))
