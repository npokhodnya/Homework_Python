import Seminar_7.telephone_directory.modules.checker as checker

from Seminar_7.telephone_directory.modules.change_database import add_note_csv, view_notes_csv, create_db
from Seminar_7.telephone_directory.modules.export import move_data_csv, move_data_csv_to_txt
from Seminar_7.telephone_directory.modules.import_data import move_data_to_csv, move_data_txt_to_csv


def import_csv_menu():
    name = input("Введите абсолютный путь файла, из которого хотите импортировать данные: ")
    move_data_to_csv(f"{name}", "databases/database.csv")


def import_txt_menu():
    name = input("Введите абсолютный путь файла, из которого хотите импортировать данные: ")
    move_data_txt_to_csv(f"{name}")


def import_menu():
    while True:
        format_file = input("Введите формат файла для импорта (1 - csv / 2 - txt): ")
        format_ = checker.check_format(format_file)
        if not format_:
            print("Введены некорректные данные!\n")
            continue
        if format_ == 1:
            import_csv_menu()
            break
        elif format_ == 2:
            import_txt_menu()
            break


def export_csv_menu():
    while True:
        name = input("Введите имя файла, в который хотите экспортировать данные "
                     "(Если файл с таким названием существует, то он будет перезаписан): ")
        check = checker.check_name_of_file(name)
        if check == False:
            print("Имя нового файла не может быть таким же, как имя корневой базы (database)!")
            continue
        elif check is None:
            print("Имя нового файла должно cодержать только буквы!")
            continue
        move_data_csv("databases/database.csv", f"databases/{name}.csv")
        print("Данные успешно экспортированы!")
        break


def export_txt_menu():
    while True:
        name = input("Введите имя файла, в который хотите экспортировать данные "
                     "(Если файл с таким названием существует, то он будет перезаписан): ")
        check = checker.check_name_of_file(name)
        if check == False:
            print("Имя нового файла не может быть таким же, как имя корневой базы (database)!")
            continue
        elif check is None:
            print("Имя нового файла должно модержать только буквы!")
            continue
        move_data_csv_to_txt("databases/database.csv", f"databases/{name}.txt")
        print("Данные успешно экспортированы!")
        break


def export_menu():
    while True:
        format_file = input("Введите формат файла для экспорта (1 - csv / 2 - txt): ")
        format_ = checker.check_format(format_file)
        if not format_:
            print("Введены некорректные данные!\n")
            continue
        if format_ == 1:
            export_csv_menu()
            break
        elif format_ == 2:
            export_txt_menu()
            break


def show_notes(notes: list):
    for i in range(1, len(notes)):
        print(f"{i}. {' ; '.join([element for element in notes[i]])}")


def show_params(params: dict):
    print("~" * 15)
    for k, v in params.items():
        print(f"{k}: {v}")
    print("~" * 15)


def add():
    res = dict()
    family = input("Введите фамилию: ")
    res['Surname'] = family
    name = input("Введите имя: ")
    res['Name'] = name
    tel = input("Введите телефон: ")
    res['Phone'] = tel
    description = input("Введите описание: ")
    res['Description'] = description
    show_params(res)
    print(res)
    correct = input("Введенные данные верны? (Да/Нет): ")
    if correct.lower() == "да":
        add_note_csv(res)
    else:
        exit_or_not = input("Данные не будут записаны. Повторить ввод? (Да/Нет): ")
        if exit_or_not.lower() == "да":
            add()


def interface():
    create_db()
    while True:
        print("\nМЕНЮ:\n"
              "1 - Посмотреть записи\n"
              "2 - Добавить запись\n"
              "3 - Импорт записей из другого файла\n"
              "4 - Экспорт записей в другие файлы\n"
              "9 - выйти\n")
        choice = input("Выберите режим работы: ")
        mode = checker.check_mode(choice)
        if not mode:
            continue
        if mode == 1:
            res = view_notes_csv()
            show_notes(res)
        elif mode == 2:
            add()
        elif mode == 3:
            import_menu()
        elif mode == 4:
            export_menu()
        elif mode == 9:
            break
