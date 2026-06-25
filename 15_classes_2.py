from enum import Enum

# Clase, liste de obiecte ale claselor, si actiuni comune ale claselor.

# CATEGORIES = ["curs", "cumparaturi", "..."]
# print(CATEGORIES[15])

class Categories(Enum):
    COURSE = "course"
    SHOPPING = "shopping"
    WORK = "work"
    PRESENTS = "presents"

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    ULTRA = 4

# print(Categories.WORK.value)
# print(Categories.WORK.name)

current_category = Categories.WORK

if current_category == Categories.WORK:
    print("I'm at work!")


class Task:
    def __init__(self, title, date, owner, category):
        self.title = title
        self.date = date
        self.owner = owner
        self.category = category

    def __str__(self):
        return f"{self.title}, {self.date}, {self.owner}, {self.category}"

    def __repr__(self):
        return f'Task("{self.title}", "{self.date}", "{self.owner}", {self.category})'


task1 = Task("Rezolvare Tema", "23.Iunie", "John", Categories.COURSE)
print(task1)

task2 = Task("Spalat Vase", "23.Iunie", "John", Categories.WORK)

task3 = Task("Buy shoes", "24.Iunie", "Olivia", Categories.SHOPPING)

# todo = [task1, task2, task3]


class Todos:
    def __init__(self):
        self.todos_list = []

    def add_task(self, add_task):
        for task in self.todos_list:
            if task.title == add_task.title:
                print("Task with this title already exists")
                return
        self.todos_list.append(add_task)

    def remove_task(self, task_to_delete):
        for task in self.todos_list:
            if task == task_to_delete:
                self.todos_list.remove(task)

    def filter_by_category(self, categ):
        results = []
        for task in self.todos_list:
            if task.category == categ:
                results.append(task)
        return results

    def filter_by_owner(self, owner):
        results = []
        for task in self.todos_list:
            if task.owner == owner:
                results.append(task)
            return results

    def count_by_category(self, categ):
        count = 0
        for task in self.todos_list:
            if task.category == categ:
                count += 1
            return count

    def __str__(self):
        return f"{self.todos_list}"


todos1 = Todos()
todos1.add_task(task1)
todos1.add_task(task2)
todos1.add_task(task3)
todos1.add_task(Task("Go to second-hand store", "25.June", "Olivia", Categories.SHOPPING))
print(todos1)

todos1.remove_task(task2)


print(todos1)
print(todos1.filter_by_category(Categories.SHOPPING))






task4 = Task("name", "24.June", "owner", Categories.SHOPPING)

# Categories.SHOPPING    ///     "shopping"

task5 = Task("Rezolvare Tema", "23.Iunie", "John", Categories.COURSE)
print(task5.category)

## scrieti o metoda in clasa Todos pentru a filtra dupa owner. acea metoda va returna toate task-urile ale unui owner, ce-l primim ca parametru al acelei metode.

print("Task 1")
print(todos1.filter_by_owner("John"))

# scrieti o metoda in clasa Todos care numara toate task-urile ale unei anumite categorii, si returneaza cate task-uri sunt pentru acea categorie. Daca sunt 3 taskuri in total pe categoria Category.COURSE de exemplu, metoda returneaza numarul 3.

print("Task 2")
print(todos1.count_by_category(Categories.COURSE))

# modificati metoda add_task, sa nu permita adaugarea unui task cu titlu duplicat. Daca exista deja un task cu acel titlu, sa printeze "Task with this title already exists!.

print("Task 3")
todos1.add_task(Task("Go to second-hand store", "25.June", "Olivia", Categories.SHOPPING))
