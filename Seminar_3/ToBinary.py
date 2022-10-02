#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
#     Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def to_bin(num: int):
    result = [num % 2]
    while num//2 > 0:
        num //= 2
        reminder = num % 2
        result.append(reminder)
    return combine_num(result)


def combine_num(lst: list):
    result = ""
    lst.reverse()
    for element in lst:
        result += str(element)
    return int(result)


print(to_bin(45))  # --->  101101
print(to_bin(3))  # --->  11
print(to_bin(2))  # --->  10
