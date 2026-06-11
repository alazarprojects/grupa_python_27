def afiseaza_meniu():
    print("1 – Afisare lista de cumparaturi")
    print("2 – Adaugare element")
    print("3 – Stergere element")
    print("4 – Sterere lista de cumparaturi")
    print("5 - Cautare in lista de cumparaturi")


produse_disponibile = [

    {
       "nume": "Deodorant",
       "pret": 45
    },
    {
        "nume": "Cafea",
        "pret": 12
    },
    {
        "nume": "Rosii",
        "pret": 25
    },
    {
        "nume": "Lipici",
        "pret": 9
    },
    {
        "nume": "Cascaval",
        "pret": 50
        }
]

lista_cumparaturi = []
def afiseaza_produse_valabile():
    print(produse_disponibile)
def afiseaza_produse_cos():
    print(lista_cumparaturi)
def adauga_produs():
    print(produse_disponibile)
    produs_selectat = input("Va rugam selectati un produs")
    for produs in produse_disponibile:
        if produs_selectat in produs["nume"]:
            lista_cumparaturi.append(produs)
def elimina_produs():
    afiseaza_produse_cos()
    produs_selectat = input("Va rugam selectati un produs")
    for produs in lista_cumparaturi:
        if produs_selectat in produs["nume"]:
            lista_cumparaturi.remove(produs)
def stergere_lista():
    lista_cumparaturi.clear()
    print("Lista a fost stearsa.")
def cautare_produse():
    produse_valide=[]
    pret_cautat = input("Introduceti un pret")
    for produs in lista_cumparaturi:
       if int(pret_cautat) >= produs["pret"]:
           produse_valide.append(produs)
    print(produse_valide)

def exit_program():
    print("Va mulumim pentru cumparaturi!")

def interactiune_meniu():
    afiseaza_meniu()
    input_client = input("Va rugam alegeti un numar")
    while input_client != "0":
        if input_client == "1":
            afiseaza_produse_cos()
        elif input_client == "2":
            adauga_produs()
        elif input_client == "3":
            elimina_produs()
        elif input_client == "4":
            stergere_lista()
        elif input_client == "5":
            cautare_produse()

        afiseaza_meniu()
        input_client = input("Va rugam alegeti un numar")
    exit_program()


interactiune_meniu()

