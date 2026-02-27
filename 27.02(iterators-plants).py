#Завдання: Створіть ітерований об'єкт, у разі ітерації яким повертається генератор.

class Plants:
    def __init__(self):
        self.plants = ["Лілія", "Ромашка", "Базилік", "Папороть", "Волошка"]
    def __iter__(self):
        def generator():
            for plant in self.plants:
                yield plant
        return generator()
plants = Plants()

for names in plants:
    print(names)
    