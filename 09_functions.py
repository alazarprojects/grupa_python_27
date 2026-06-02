
import random
from lib.core import even_numbers, is_even


#print(random.sample(range(0, 1000), 15))

random_numbers = [738, 382, 62, 39, 584, 225, 193, 72, 585, 149, 187, 579, 125, 936, 488]

# filter(), map(), reduce(), zip()

#lambda functions:

def mult_2(param1):
    return param1 * 2


print(mult_2(10))

#efemera
square = lambda x: x * 2
print(square(10))

# filtrati toate numerele multiplu de 7 din random_numbers

rezultat = list(filter(lambda x: x % 3 == 0, random_numbers))
print(rezultat)

#prima data am definit conditia cu lambda, adica sa fie multiplu de 3, si apoi locatia adica din lista de random_numbers

rezultat2 = list(filter(is_even, random_numbers))
print(rezultat2)