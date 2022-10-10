# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму
# многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

def decompose_poly(poly: str):
    poly = poly.replace("- ", "+ -").split()
    poly_filtered = list(filter(lambda x: x != "+" and x != "0" and x != "=", poly))
    res = [poly_filtered[i].split("*") for i in range(len(poly_filtered))]
    for element in res:
        if len(element) == 1:
            element.append("X^0")
    return res


def sum_of_polys(first_poly: list, second_poly: list):
    sum_list = first_poly + second_poly
    cash = []
    result = []
    for i in range(len(sum_list)):
        sum_ = 1
        if sum_list[i][1] not in cash:
            cash.append(sum_list[i][1])
            for j in range(i + 1, len(sum_list)):
                if sum_list[i][1] == sum_list[j][1]:
                    sum_ = int(sum_list[i][0]) + int(sum_list[j][0])
            result.append([sum_, sum_list[i][1]])
    return result


def compose_poly(poly_list: list):
    res = []
    for element in poly_list:
        if len(res) != 0:
            if int(element[0]) >= 0:
                res.append("+")
            else:
                res.append("-")
        res.append(f"{abs(int(element[0]))}*{element[1]}")
    return " ".join(res)


with open("first.txt") as file:
    first_poly = decompose_poly(file.read())
with open("second.txt") as file:
    second_poly = decompose_poly(file.read())
with open("ans.txt", "w") as file:
    file.write(compose_poly(sum_of_polys(first_poly, second_poly)) + " = 0")
