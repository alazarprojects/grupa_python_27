#variabile prin referinta.
lista1 = [10,30, 5, 7, 100, -5]
lista2 = lista1
#lista2 = este un numar express, si cand facem o modificare ca de exemplu attend, isi face mirror la adresa memorie a listei 1

print(lista1)


# modificam lista2.
lista2.append(88)
print(lista1)

#variabile prin valoare:
var1 = 100
var2 = var1

var2 = 77
print(var1) #variabila nu s-a schimbat dn 100 in 77, deoarece python are varibile care sunt strucutri de date primitive:
#int, float, bool, string

#structura de date complexa: lista, dictionarul, set, tuplu,

lista3 = [9, 10, 100, 5, 50, 4]
#         0   1    2  3   4  5
# slicing, splicing
# syntax:   list[start:stop:step]  #start, stop.. sunt indexii

# print(lista3[0:4:3])
# print(lista3[::-7]) , daca pui un numar de index mai mare decat lista ta, iti arata primul numnar

lista4 = lista3[:]
lista4.append(88)
#slice ul de la lista3 "[:]" creeaza o adresa noua de memorie, si nu o sa se reflecte schimbarea
#nu se modifica lista3 , fiindca lista4 este o clona, nu este aceeasi lista cu lista 3.
print(lista3)

lista5 = [7,10]
lista5.append(99)
lista5.extend([100, 101, 102])
lista5 += [103, 104, 105]
lista5.remove(101) #sterge doar primul numar 101 intalnit in lista. daca sunt2, doar primul este sters.
print(lista5.index(100))

lista5.sort()
print(lista5)

lista6=sorted(lista5)
print(lista6)

#matrici
#Matrix, Keanu Reaves

matrice1 = [
    [3, 4, 10], #index 0
    [7, 8, 11], #index 1
    [0, 3, 99]  #index 2
]
#ind 0, 1,  2
print(matrice1[0][1]) #s a printat prima linie, a 2a coloana

print(matrice1[2][0]) #se printeaza linia 3, prima coloana

# list comprehension.
lista7 = [3, 4, 10]
lista8 = [x ** 3 for x in lista7]

print(lista8)

lista9 = [x ** 3 for x in lista7 if x % 2 == 0]

print(lista9)

# Strings.
# un str se comporta ca o lista imutabila
alfabet = "ABCdefghijklmn"

print(alfabet[::-1])

print(alfabet.lower())
print(alfabet.upper())

#eroare:
#alfabet[0] = "P"

print(alfabet.strip())
print(alfabet.replace("A", "00"))

prop1 = "     Gabi a inceput sa invete python. El, un student, urmeaza acest curs, cursul de python.     "
rezultat1 = (prop1.strip().lower().split("."))
rezultat1.remove('')
#rezultat.pop()
print(rezultat1)

#strip elimina spatiile, (in cazul nostru)de la inceput si sfarsit
#lower transforma in litere mici
#split imparte propozitiile de la "."
#metodele se fac de la stanga la dreapta, deoarece in stanga e variabila



# prop2 = "."
# print(prop2.split("."))

var3 = ['a', 'b', 'c', 'detrical 03 100000IU']
rezultat2 = "-".join(var3)

print(rezultat2)

if "D3" in rezultat2:
    print("avem vitamina d")

print(99 in lista5)

ex1 = "AVG-JRD-IOR:RED-GRN-BLU:QWE-RTY-UIO"
#luati acest string si creati o matrice 3x3, in care sa pastrati doar literele.
#primul element e "AVG", urmatorul de pe randul 1 e "JRD" etc.

part1= ex1.split(":")
print(part1)
#print(part1.split("-"))

rezultat3 = []
for elem in part1:
    print(elem)
    elem.split("-")
    rezultat3.append(elem.split("-"))

print(rezultat3[1][0])

#while

listaw = [4, 10, 20, 50, 100]

while len(listaw) > 0:
    print(listaw.pop())

#while fata de for are un altfel de folos, while exploreaza un spatiu necunoscut(de ex: o lista care primeste sau se sterg elem din ea)
#un while il poti folosi pentru un binary tree, cand nu stii cate elemente ai si e un spatiu necunoscut

nr_imens = 1000000
while nr_imens > 0:
    nr_imens = nr_imens - 10000
    print(nr_imens)

# while il folosim cand nu stim nr de pasi sau cand spatiul de explorare este necunoscut, dar avem o conditie clara de sfarsit.
# for il folosim cand parcurgem o lista deseori, sau un dictionar, etc. cand stim clar cum arata o structura de date. daca lista se modifica intre timp, for-ul nu este potrivit pentru a parcurge lista.

lista13 = [10, 20, 300, 1000]

while True :
    if len(lista13) <= 0 :
        break
    print(lista13.pop())

#formatare e atunci cand intr-un sir de caractere, introduci alt sir de caractere
name = "Alex"
age = 25
profession = "Sailor"

#f-string
print(f"Hello! My name is {name}, I'm {age} years old, and I'm a {profession} .")

# forma()
print("Hello! My name is {}, I'm {} years old, and I'm a {}".format(name, age, profession))

#acelasi lucru, 2 metode diferite, unul mai modern, si cel clasic

#basic concatenation
print("Hello! My name is " + name +", I'm "+ str(age) + " years old, and I'm a " + str(profession))

#newline special character
msg = "Line 1 \nLine 2"
print(msg)


# multi-line string
msg2 = """
Line 1
Line 2 
etc etc
"""
print(msg2)