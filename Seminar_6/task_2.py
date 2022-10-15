# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.


# Было:
def create_sequence(n):
    result = []
    for i in range(-n, n + 1):
        result.append(i)
    return result


def multiplication(a, b, origin_list):
    return origin_list[a - 1] * origin_list[b - 1]


n = int(input("N: "))
a = int(input("a: "))
b = int(input("b: "))
res_list = create_sequence(n)
print(f"a * b = {res_list[a - 1]} * {res_list[b - 1]} = {multiplication(a, b, res_list)}")


# Стало:
def multiplication(a, b, n):
    lst = [i for i in range(-n, n + 1)]
    return lst[a - 1] * lst[b - 1]


print(f"a * b = {multiplication(a, b, n)}")
