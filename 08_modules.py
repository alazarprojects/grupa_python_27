
import os

#operating system interaction

print(os.listdir())

if os.path.exists("manage.py"):
    print("Avem fisierul manage.py in acest folder")
    print(os.path.getsize("manage.py"))
else:
    print("File not found")

# os.path.listdir() returneaza o lista de nume de foldere si fisiere
# os.path.isfile(fisier) returneaza True daca "fisier" este fisier
# os.path.getsize(fisier) returneaza marimea fisierului

# ex: creati o functie care trece prin fisierele din folderul curent si returneaza marimea totala a fisierelor


def total_files_size():
    """"
    Function that returns total file size for all files in root level directory.
    :return: total file size, in KB
    """
    files = os.listdir()
    total = 0
    for f in files:
        if os.path.isfile(f):
            print(f)
            marime = os.path.getsize(f)
            total = total + marime
    return total / 1024

#baza 2, nu baza 10
#1 bit -> 0.1
#1 byte -> 8 biti
#1 kbyte -> 2 ^ 8
# 2 4 8 16 32 64 128 256 512 1024 2048....

# cati kb
print(total_files_size())