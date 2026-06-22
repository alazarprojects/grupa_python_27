import json
from pathlib import Path
from datetime import datetime

from pprint import pprint
def write_list_data(file_name, items):
    with open(file_name, 'w', encoding='utf-8') as f:
        for item in items:
            f.write(f"{item}\n")

def read_list_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return [line.strip().strip("{}'") for line in f]

def write_json_data(file_name, data):
    path = Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)

    # write data to file
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        print("Data saved successfully!")


def read_json_data(file_name):
    path = Path(file_name)

    if not path.exists() or path.stat().st_size == 0:
        return []   # return empty list if file doesn't exist or is empty

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def adaugare_categorii():
    print("=== Introducere categorii ===")
    categorii = read_list_data("categorii.txt")
    while True:
        categorie = input("Categorie (sau 'stop'): ")

        if categorie.lower() == "stop":
            break

        if categorie in categorii:
            print("Categoria există deja! Nu a fost adăugată.")
            continue

        categorii.append(categorie)

    write_list_data("categorii.txt", categorii)

    print("Categorii salvate!\n")


def adaugare_task():
    print("\n=== Adăugare task ===")
    taskuri = read_json_data("taskuri.json")
    categorii = read_list_data("categorii.txt")
    nume = input("Introduceți task-ul: ")
    data_limita = input("Introduceți data limită (DD.MM.YYYY HH:MM): ")
    responsabil = input("Introduceți persoana responsabilă: ")
    categorie = input("Introduceți categoria task-ului: ")

    # verificare categorie
    if categorie not in categorii:
        print("Eroare! Categoria nu există, alegeti alta varianta!.\n")
        return

    task = {
        "nume": nume,
        "data_limita": data_limita,
        "responsabil": responsabil,
        "categorie": categorie
    }

    taskuri.append(task)
    write_json_data("taskuri.json", taskuri)
    print("Task adăugat cu succes!\n")

def afisare_taskuri_pe_categorii():
    categorii = read_list_data("categorii.txt")
    taskuri = read_json_data("taskuri.json")

    for categorie in categorii:
        categorie = categorie.strip().strip("{}'")
        print(f"Categoria {categorie} ")
        are_taskuri = 0
        for task in taskuri:
            if task["categorie"] == categorie:
                print(f"""
                Nume: {task['nume']}
                Data limită: {task['data_limita']}
                Responsabil: {task['responsabil']}
                """)
                are_taskuri+=1
        if are_taskuri == 0:
            print ("Nu sunt task-uri in categorie")


def afisare_taskuri_cu_index():
    print("\n=== Lista taskuri ===")
    taskuri = read_json_data("taskuri.json")
    if len(taskuri) == 0:
        print("Nu există taskuri.\n")
        return

    for i, task in enumerate(taskuri, start=1):
        print(f"""
Task #{i}
Nume: {task['nume']}
Data limită: {task['data_limita']}
Responsabil: {task['responsabil']}
Categorie: {task['categorie']}
""")

def editare_taskuri():
    afisare_taskuri_cu_index()
    taskuri = read_json_data("taskuri.json")
    categorii = read_list_data("categorii.txt")
    index = int(input("Alege taskul pentru editat: "))
    if index < 0 or index > len(taskuri):
        print("Indexul nu exista")
    else:
        nume = input("Introduceți task-ul: ")
        data_limita = input("Introduceți data limită (DD.MM.YYYY HH:MM): ")
        responsabil = input("Introduceți persoana responsabilă: ")
        categorie = input("Introduceți categoria task-ului: ")

        # verificare categorie
        if categorie not in categorii:
            print("Eroare! Categoria nu există, alegeti alta varianta!.\n")
            return

        task = {
            "nume": nume,
            "data_limita": data_limita,
            "responsabil": responsabil,
            "categorie": categorie
        }

        taskuri[index-1] = task
        write_json_data("taskuri.json", taskuri)


def cautare_dupa_responsabil():
    nume = input("Introduceți numele persoanei: ")

    gasit = False
    taskuri = read_json_data("taskuri.json")
    for task in taskuri:
        if task["responsabil"].lower() == nume.lower():
            print(task)
            gasit = True

    if not gasit:
        print("Nu există taskuri pentru această persoană.\n")


def cautare_dupa_categorie():
    categorie = input("Introduceți categoria: ")

    gasit = False

    taskuri = read_json_data("taskuri.json")
    for task in taskuri:
        if task["categorie"].lower() == categorie.lower():
            print(task)
            gasit = True

    if not gasit:
        print("Nu există taskuri în această categorie.\n")

def cautare_dupa_nume_task():
    nume_task = input("Introduceți nume task: ")

    gasit = False

    taskuri = read_json_data("taskuri.json")
    for task in taskuri:
        if nume_task in task["nume"]:
            print(task)
            gasit = True

    if not gasit:
        print("Nu există taskuri cu acest nume task.\n")

def cautare_dupa_data():
    data = input("Introduceți data (DD.MM.YYYY): ")

    gasit = False

    taskuri = read_json_data("taskuri.json")
    for task in taskuri:
        if data.strip() in task["data_limita"] :
            print(task)
            gasit = True

    if not gasit:
        print("Nu există taskuri în această data.\n")
def sterge_task():
    afisare_taskuri_cu_index()
    taskuri = read_json_data("taskuri.json")
    index = int(input("Alege taskul pentru stergere: "))
    if index < 0 or index > len(taskuri):
        print("Indexul nu exista")
    else:
        taskuri.remove(taskuri[index-1])
        write_json_data("taskuri.json", taskuri)
        print("Task-ul a fost sters cu success")
def sorteaza_taskuri_cronologic(taskuri):
    return sorted(
        taskuri,
        key=lambda task: datetime.strptime(task["data_limita"], "%d.%m.%Y %H:%M")
    )

def afisare_sortare_ordine_cronologica():
    taskuri = read_json_data("taskuri.json")
    taskuri_sortate_cronologic = sorteaza_taskuri_cronologic(taskuri)

    for i, task in enumerate(taskuri_sortate_cronologic, start=1):
        print(f"""
    Task #{i}
    Nume: {task['nume']}
    Data limită: {task['data_limita']}
    Responsabil: {task['responsabil']}
    Categorie: {task['categorie']}
    """)

def meniu():
    adaugare_categorii()

    while True:
        print("""
===== MENIU =====
1. Adăugare task
2. Afișare taskuri per categorii
3. Editare task
4. Sterge task
5. Căutare după responsabil
6. Căutare după categorie
7. Cautare dupa data
8. Cautare dupa nume task
9. Afiseaza taskuri in ordine cronologica
0. Ieșire
""")

        optiune = input("Alegeți opțiunea: ")

        if optiune == "1":
            adaugare_task()

        elif optiune == "2":
            afisare_taskuri_pe_categorii()

        elif optiune == "3":
            editare_taskuri()

        elif optiune == "4":
            sterge_task()

        elif optiune == "5":
            cautare_dupa_responsabil()

        elif optiune == "6":
            cautare_dupa_categorie()

        elif optiune == "7":
            cautare_dupa_data()

        elif optiune == "8":
            cautare_dupa_nume_task()

        elif optiune == "9":
            afisare_sortare_ordine_cronologica()

        elif optiune == "0":
            print("La revedere!")
            break


        else:
            print("Opțiune invalidă!\n")


meniu()