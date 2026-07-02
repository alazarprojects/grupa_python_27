
# fibonacci:
# 0 1 1 2 3 5 8 13 21 34 55 89 ...

# un iterator poate explora un spatiu cu un sfarsit necunoscut, unde e greu de stiut cati pasi poate explora acel spatiu
class Fibonacci:
    def __init__(self):
        self. first = 0
        self. second = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.first

        next_number = self.first + self.second
        self.first = self.second
        self.second = next_number

        return current


pas = 0
for i in Fibonacci():
    print(i)

    if i > 9999999:
        break

#    pas += 1
#    if pas >= 10:
#       break
