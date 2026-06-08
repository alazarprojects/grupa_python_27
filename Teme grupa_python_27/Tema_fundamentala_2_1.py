cetateni = [
    {
        "CNP": 19904843895738,
        "Nume": "Lucian Zamfir",
        "Varsta": 32,
        "Adresa": ", Jud. Brasov",
        "Greutate": 75
    },
    {
        "CNP": 193048438345345,
        "Nume": "Matei Rosu",
        "Varsta": 30,
        "Adresa": "Cluj-Napoca, Jud. Cluj",
        "Greutate": 59
    },
    {
        "CNP": 19876543211234,
        "Nume": "Andrei Popescu",
        "Varsta": 25,
        "Adresa": "Bucuresti, jud.Ilfov",
        "Greutate": 80
    },
    {
        "CNP": 28765432109876,
        "Nume": "Elena Gheorghe",
        "Varsta": 28,
        "Adresa": "Iasi, Jud. Iasi",
        "Greutate": 62
    },
    {
        "CNP": 17654321098765,
        "Nume": "Cristian Piedone",
        "Varsta": 45,
        "Adresa": "Constanta, Jud. Constanta",
        "Greutate": 90
    },
    {
        "CNP": 29543210987654,
        "Nume": "Sandra Izbasa",
        "Varsta": 35,
        "Adresa": "Timisoara, Jud. Timis",
        "Greutate": 58
    }
]

def filter_age_weight (varsta, greutate):
    cetateni_valizi = []
    for cetatean in cetateni:
        if cetatean["Varsta"] > varsta and cetatean["Greutate"] > greutate:
            cetateni_valizi.append(cetatean)
    return cetateni_valizi

#Printam toti cetatenii din lista
print("Toti cetatenii")
print(cetateni)
print()

#Printam toti cetatenii care au peste 25 de ani si 60 kg
print("Cetatenii care au peste 25 de ani ssi 60 kg")
print(filter_age_weight(25,60))
print()

#Printam toti cetatenii care au peste 40 de ani si 50 kg, ca sa demonstram ca poate fi refolosita
print("Cetatenii care au peste 40 de ani si 50 kg")
print(filter_age_weight(40,50))
print()
