# Вычислить число π c заданной точностью d
#
# *Пример:*
#
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤ 10^{-10}

import math


def current_num(n, multiply):
    return multiply * 4 / n


def is_number(d):
    try:
        float(d)
        return True
    except ValueError:
        return False


def pi_num(d, n=1):
    len_d = len(d)
    d = float(d)
    res = 0
    mult = 1
    current = current_num(n, mult)
    while abs(current) > d / 10:
        res += current
        n += 2
        mult *= -1
        current = current_num(n, mult)
    return float(str(res)[:len_d])


def solution(d):
    if is_number(d):
        pi_num(d)
    else:
        return "d is not a number!"


d_param = input("d: ")
print(f"result: {pi_num(d_param)}")
print(f"pi: {math.pi}")
