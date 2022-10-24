import csv


def move_data_csv(from_: str, to: str, fieldnames: list = None):
    if fieldnames is None:
        fieldnames = ["Surname", "Name", "Phone", "Description"]
    with open(to, "w") as new, open(from_, "r") as old:
        reader = csv.DictReader(old)
        writer = csv.DictWriter(new, fieldnames=fieldnames)
        writer.writeheader()
        for par in list(reader):
            writer.writerow(par)


def move_data_csv_to_txt(from_: str, to: str):
    with open(to, "w") as new, open(from_, "r") as old:
        txt = ""
        reader = csv.DictReader(old)
        for row in reader:
            txt += f"Surname: {row['Surname']}\n"
            txt += f"Name: {row['Name']}\n"
            txt += f"Phone: {row['Phone']}\n"
            txt += f"Description: {row['Description']}\n\n"
        new.write(txt)
