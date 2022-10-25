import csv

from modules.change_database import add_note_csv


def move_data_to_csv(from_: str, to: str):
    fieldnames = ["Surname", "Name", "Phone", "Description"]
    try:
        with open(from_, "r") as new, open(to, "a") as old:
            reader = csv.DictReader(new)
            writer = csv.DictWriter(old, fieldnames=fieldnames)
            for par in list(reader):
                writer.writerow(par)
            print("Данные успешно импортированы!")
    except:
        print("Ошибка! Файл не существует!")


def move_data_txt_to_csv(from_: str):
    count = 0
    try:
        flag = True
        with open(from_, "r") as old:
            while flag:
                current_string = old.readline()
                if current_string == "":
                    flag = False
                surname = current_string.replace("\n", "")
                if surname != "":
                    name = old.readline().replace("\n", "")
                    phone = old.readline().replace("\n", "")
                    description = old.readline().replace("\n", "")
                    if "Surname: " in surname and "Name: " in name and "Phone: " in phone and "Description: " in description:
                        surname = surname.replace("Surname: ", "")
                        name = name.replace("Name: ", "")
                        phone = phone.replace("Phone: ", "")
                        description = description.replace("Description: ", "")
                        add_note_csv({"Surname": surname, "Name": name, "Phone": phone, "Description": description})
                        count += 1
                    else:
                        print("Файл не соответствует нужному формату, импорт невозможен!")
        print(f"Импортировано записей: {count}")
    except:
        print("Ошибка! Такого файла не существует!")
