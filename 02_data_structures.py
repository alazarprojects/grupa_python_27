#Liste

list1 = [4, 5, 10, 20, 30, 100, 500, 999, 1000]
#        0  1   2   3   4    5    6    7     8
print(list1[0])
print(list1[-1])

index = len(list1) // 2
print    (  list1  [     index     ]    )


list2 = [0 , 1 , 2, 50, 100, 100, 100, 2, 2, 2, 9, 10, 99]
print(list2)


#putem schimba un element din lista folosind [] si punand indexul elementului in ele
list2[3] = 100
print(list2)

# Dictionare:

# unordered. , cheia trebuie sa fie unica, prima valoare va fi suprascrisa de a 2a valoare, de ex la inaltime
persoana = {
    "key": "valoare",
    "nume": "Alex",
    "inaltime": "1.85m",
    "varsta": 27,
    "cetatean_roman": True,
    "bolnav": False,
    "greutate": 75.7,
    "inaltime" : "2m",
}


print(persoana)
# fast lookup
print(persoana["key"])
print(persoana["varsta"])
persoana["inaltime"] = "3m"
persoana["CNP"] = "2215546734757"

# cel mai intalnit tip de date
# bool.

# string.
# cont bancar:
# IBAN: 132453464563434

#   "  h   e   l   l  o"
#    184 101 108 108 111
#   0101010111011

#seturi:
#cutie de bomboane, toate diferite.
#un set nu are index
#filtreaza, apar doar elementele unice

#curly braces
#squigly brackets
#nu te poti baza pe ordinea lor
elemset = {3, 6, 10, 9, 8, 100, 3}

print(elemset)

list2 = [0 , 1 , 2, 50, 100, 100, 100, 2, 2, 2, 9, 10, 99]

list2_no_duplicates = set(list2)
print(list2_no_duplicates)

list3 = ["gigel_99", "alina_32" "alex", "marius"]
# "adrian" -> vreau sa mi fac cont. sistemul trebuie sa verifice daca username-ul este liber si nefolosit
# complexitate n. 0(n)
#pentru un set, aceeasi actiune are 0(1)

# "gigel_99" -> 93444543
# "alina_32" -> 23423345

lista4 = list(set(list2))
print(lista4)


# tuple, like a list, but immutable.

coordinates = (0, 10)
coordinates3d = (0, 15, -5)

print(coordinates[1])

coordinates = (0, 19)

# Metode:

#catel = "Spot"
#catel.latra("cioara")
#catel.manance("peste")
#catel.miroase("adrian")
#catel.musca("adrian")

# obiect.actiune/functie/metoda (parametrii)

lista5 = [7, 8, 100, 99]
lista5.append(-50) #adauga -50 in lista
print(lista5)
lista5.pop(1) #a scos indexul 1 adica cifra 8 din lista
print(lista5)
lista5.reverse() # a inversat lista
print(lista5)
lista5.sort() # a adus lista de la mic la mare
print(lista5)
lista5.remove(100) #sterge prima aparitie a numarului din lista

set2 = {7, 6, 8, 8, 10, 90, 100}
set2.add(-5) #adauga numar
set2.remove(90) #remove sterge
print(set2)

# chei de dictionare

dict_2 = {
    "key":"value",
    1: "one",
    3.14:"PI",
    True: False,
    (2,3):"coordinates",
    "bizar" : {
        "level2": {
            "list": [0, 1, 2,3 ,100, 99, -5]
        }
    }
}

print(dict_2)

print(True == 1)
# True si 1 sunt vazute ca si aceeasi valoare, si faptul ca sunt folosite ca si cheie

print() # un spatiu gol, ca si un endline

print("End of file")