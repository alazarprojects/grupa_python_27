# terminalul are multiple stream-uri de text pe care le primeste si le afiseaza

# STDERR este stream-ul de erori.

print("========== Inceput de curs exceptii =======")
lista1 = [9, 10, 11, 33]

print(lista1)
print(lista1[3])


try:
    vari = int(input("De care index esti curios?"))
    print(lista1[vari])
    # exception that is throw from the int() conversion is caught as a ValueError. exception that is thrown when accessing a non-existing index is caught, IndexError.
except IndexError:
    print("we went too far captain!")
except ValueError:
    print("You have to write an integer number!")
except BaseException:
    print("You shall not pass!")
except BaseException:
    # Don't do this!!!
    pass
# exception bubble-up.

var2 = 10

if var2 > 5:
    raise Exception("My  variable is too high!")

print("========== Sfarsit de curs exceptii =======")

