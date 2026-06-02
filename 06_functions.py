
#functii
#def -> keyword, face parte din sintaxa de definire a unei functii

#definire de functie
def greet():
    print("Hello")
    print("this is flume")

#apelare de functie

greet()

# add
# a, b -> parametrii (argumente)
#definiarea functiei face codul reutilizabil de cate ori vrem

def add(a, b):
    return a + b

print(add(5, 10))
# add (5, 10)

print(add(60, 90))
print(add(100, 333))

def mul(a, b):
    return a * b

var1 = mul(5, 15)
print(var1)
add(var1, 35)
# s-a facut inmultirea din var1, 5 ori 15 si s a adunat 35

# paramentru se numeste acel "a", Argument este valoarea ce o dam acelui "a", de exemplu 5

# creati sub, care scade a - b, div care imparte a / b si pow care ridica a ** b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def pow(a, b):
    return a ** b


#putem sa apelam o functie in alta functie
# 6-4 * 10
rezultat = sub(6, mul(4, 10))
print(rezultat)

# 5+4 * 8 ** 2

rezultat2 = add(5, mul(4, pow(8, 2)))
print(rezultat2)


# daca o functie nu are return, python pune un return implicit, None
def speak(word="woof"):
    print(word)

speak()
speak("Meow")

def drive(car_model, max_speed=130):
    print(f"{car_model} is running at a max speed of {max_speed}")

drive("Audi")
drive("Mazda", "red")

# typed function
def modulo (a: int, b: int) -> int:
    """
    Returns the remdinder of the division between two numbers
    :param a: the number is divided by
    :param b: the number that does the division
    :return: remainder
    """
    return a % b

# RST / Sphinx style docs ^
print(modulo(13, True))

nr = [10, 11, 21, 5, -1, 20, 3]

def even_numbers(list1):
    #iteram prin lista. folosim modulo
    res = []
    for n in list1:
        if n % 2 == 0:
            print(f"am gasit numar par: {n}") #daca impartim nr la 2 si restul este 0 atunci e par
            res.append(n)
    return res


result = even_numbers(nr)
print(result)

nr2 = [7, 22, 4, 5, -2, 8, 10]
restult2 = even_numbers(nr2)
print(restult2)

# Tema:


print("Tema procesare stringuri")
#ERR-Value Error-ER:10"

#"INF-Program launch Info-CD:5"

#"WRN-Low memory-WR:11

var2 = ["ERR-Value Error-ER:10","INF-Program launch Info-CD:5", "WRN-Low memory-WR:11"]

#refractorizare:
#mutat codul intr-o functie, si in loc de print, folositi return, sa returnam un string care este mesajul formatat

def format_logs(param1):
    chunks = []
    for s in param1:
        if s.split("-")[0] == "ERR":
           chunks.append("[ERROR]")
        elif s.split("-")[0] == "WRN":
            chunks.append("[WARNING]")
        elif s.split("-")[0] == "INF":
            chunks.append("[INFO]")
        else:
            chunks.append(s.split("-")[0])

        chunks.append(f"Mesaj: {s.split("-")[1]}")
        # s -> string :::: .split("-") -> list :::: [2] -> elem din lista dupa index :::: elem este string, deci s.split("-")[2] -> string :::: .split(":") -> list :::: acea_lista[1] -> al doilea element, care este numarul de cod ce ne intereseaza.
        chunks.append(f"Cod: {s.split("-")[2].split(":")[1]}\n")

    str_result = "\n".join(chunks)
    return str_result

result = format_logs(var2)
print(result)

# [ERROR] - folositi if
# Mesaf: Value Error
# Cod: 10

# [ERROR]
# Mesaj: Value Error
# Cod: 10
# [INO]
# Mesaj: Program launch Info
# Cod: 5
# [WARNING]
# Mesaj: Low memory
# Cod: 11

