# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# *Пример:*
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def generate_polynomial(k=random.randint(1, 10)):
    poly = []
    for i in range(random.randint(1, 5)):
        num = random.randint(-100, 100)
        x_in = random.randint(0, 1)
        degree = random.randint(1, k)
        if num == 0:
            continue
        if len(poly) > 0:
            if num < 0:
                poly.append("-")
            else:
                poly.append("+")
        if x_in and len(poly) > 0:
            if num != 0:
                if degree == 1:
                    poly.append(f"{abs(num)}X")
                else:
                    poly.append(f"{abs(num)}X^{degree}")
            else:
                if degree == 1:
                    poly.append("X")
                else:
                    poly.append(f"X^{degree}")
        elif not x_in and len(poly) > 0:
            poly.append(f"{abs(num)}")
        else:
            if k > 1:
                poly.append(f"{abs(num)}X^{k}")
            else:
                poly.append(f"{abs(num)}X")

    poly.append("= 0")
    return poly


with open("poly_k/answer.txt", "w") as file:
    file.write(" ".join(generate_polynomial(2)))
