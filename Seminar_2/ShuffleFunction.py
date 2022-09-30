import time


def shuffle_list(origin_list):
    shuffled_list = origin_list.copy()
    len_list = len(origin_list)
    for i in range(len_list):
        rand_index = (int(time.time()) // (i + 1)) % len_list
        shuffled_list[i], shuffled_list[rand_index] = shuffled_list[rand_index], shuffled_list[i]
    return shuffled_list


test_list = [1, "GB", 3, 4, "b^2 - 4ac"] # Можете менять значения здесь для проверки :)
print(f"{test_list} --> {shuffle_list(test_list)}")
