# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Изначально:
def delete_words(origin_string: str, del_factor: str):
    return " ".join(list(filter(lambda el: del_factor not in el, origin_string.lower().split())))


test_string = "аБВ -влвы- сао б вба оабв абвввв"
res = delete_words(test_string, "абв")
print(res)
