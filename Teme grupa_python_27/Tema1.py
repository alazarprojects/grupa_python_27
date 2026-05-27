print()
varl1 = ["ERR-Value Error-ER:10","INF-Program launch Info-CD:5","WRN-Low memory-WR:11"]
varl2 = ["INF-Program exit-CD:14","WRN-Low disk space-WR:99","WRN-Bandwith reached-WR:87"]

print(varl1)
print(varl2)

ambeleliste = varl1 + varl2  # adaugam intr-o singura lista
print(ambeleliste)
print()


for elem in ambeleliste:
    parti = elem.split("-") #am impartit textul in 3 parti dupa fiecare "-"

    tip = parti[0] #extragem tip ul msg cu index 0 adica: ERR, INF sau WRN
    mesaj = parti[1] #extragem mesajul propriu-zis cu index 1: Value error, Low memory etc

    # extragem codul
    coduri = parti[2].split(":") #separa codului tip numar, ex-> ER:10, ramane 10
    cod = coduri[1] #apoi salvam numarul codului 10, 5, 11  etc

    # alegem ce cuvant afisam în functie de tipul mesajului
    if tip == "ERR":
        afisare_mesaj = "ERROR"

    if tip == "INF":
        afisare_mesaj = "INFO"

    if tip == "WRN":
        afisare_mesaj = "WARNING"

    print(f"[{afisare_mesaj}]")
    print(f"Mesaj: {mesaj}")
    print(f"Cod: {cod}\n")
