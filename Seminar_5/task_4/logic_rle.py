# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(string: str):
    res = []
    len_ = len(list(string))
    count = 1
    for i in range(len_):
        if i < len_ - 1:
            if string[i] == string[i+1] and count < 9:
                count += 1
                continue
            else:
                res.append(f"{count}{string[i]}")
                count = 1
                continue
        else:
            res.append(f"{count}{string[i]}")
            break
    return "".join(res)


def decode(string: str):
    res = []
    l = len(string)
    for i in range(1, l, 2):
        res.append(string[i] * int(string[i - 1]))
    return "".join(res)
