
import random
from functools import reduce
from pprint import pprint
from lib.core import even_numbers, is_even



#print(random.sample(range(0, 1000), 15))

random_numbers = [738, 382, 62, 39, 584, 225, 193, 72, 585, 149, 187, 579, 125, 936, 488]

# filter(), map(), reduce(), zip()

#lambda functions:

def mult_2(param1):
    return param1 * 2


print(mult_2(10))

#efemera
#one shot - se foloseste o singura data
square = lambda x: x * 2
print(square(10))

# filtrati toate numerele multiplu de 7 din random_numbers

rezultat = list(filter(lambda x: x % 3 == 0, random_numbers))
print(rezultat)

#prima data am definit conditia cu lambda, adica sa fie multiplu de 3, si apoi locatia adica din lista de random_numbers

rezultat2 = list(filter(is_even, random_numbers))
print(rezultat2)

# map(), reduce(), zip()

print("=========Map function: =========")
random_numbers = [738, 382, 62, 39, 584, 225, 193, 72, 585, 149, 187, 579, 125, 936, 488]


# "map"  primeste 2 parametrii, o functie si o lista
# var 1
ひらが = list(map(lambda x: x // 2, random_numbers))
print(ひらが)

var2 = list(map(lambda x: x ** 3, random_numbers))
print(var2)

print("======== Reduce function: ======")

var3 = reduce(lambda a, b: a +b, random_numbers, 10000)
print(var3)

var4 = reduce(lambda a, b: a * b, random_numbers)
print(var4)

print(len(str(var4)))
#ideea reduce-ului e ca trece printr o lista si aduna toate nr/elementele impreuna, sau le imparte, pe scurt face un calcul.

#random_letters = ['b', 'z', 'f', 'h', 'l', 'u', 'o']

random_letters = []


def generate_random_chars(count = 10, min_char = 97, max_char = 122):

    # for i in range(count):
    # random_letters.append(chr(random.randint(min_char, max_char)))
    #
    # print(random_letters)

    step1 = random.sample(range(min_char, max_char + 1), count)
    step2 = list(map(lambda x: chr(x), step1))
    random_letters = step2
    return random_letters

random_letters = generate_random_chars()
print(random_letters)


print("======= Zip Function: =========")

zip()
#ideea zipp-ului e ca primesti mai multe liste si le combini in tupluri (perechi de date)

names = ["John", "James", "Turk", "Maria", "Oprah"]
ages = [18, 20, 35, 50, 10]

combined = dict(zip(names, ages))
print(combined)

print("======= Key Values =======")

score = [6, 8, 4, 10, 9]


zipped_people = list(zip(names, ages, score))
print(zipped_people)

people = []

for elem in zipped_people:
    #elem = ('John', 18, 6)
    people.append({
        "name": elem[0],
        "age": elem[1],
        "score": elem[2]
    })

pprint(people, sort_dicts=False)

#lista de dictionare e cea mai intalnita forma de date

sorted_list = sorted(people, key = lambda a: a["name"], reverse = False)
print(sorted_list)

