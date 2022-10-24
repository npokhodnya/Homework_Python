import csv


def create_db(filename: str = "database"):
    try:
        name = f"databases/{filename}.csv"
        with open(name, "x") as file:
            fieldnames = ["Surname", "Name", "Phone", "Description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
    except:
        pass


def add_note_csv(params: dict, filename: str = "database"):
    name = f"databases/{filename}.csv"
    with open(name, "a") as file:
        fieldnames = ["Surname", "Name", "Phone", "Description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(params)


def view_notes_csv(filename: str = "database"):
    name = f"databases/{filename}.csv"
    with open(name, "r") as file:
        reader = csv.reader(file)
        return list(reader)
