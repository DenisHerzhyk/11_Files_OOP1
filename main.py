# 1).

import re

html = open("OOP.txt", "r", encoding="utf-8")
txt = open("OUT.txt", "w", encoding="utf-8")

for line in html.readlines():
    clean_text = re.sub('<.*?>', '', line)
    if clean_text.strip():  # проверяем, что строка не пустая после удаления HTML тегов
        txt.write(clean_text + "\n")  # добавляем перенос строки к строке, которая не пустая

html.close()
txt.close()
import fileinput

# 2).

# #lemon, price: 5
# Ivan Ivanov
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# Total: 45

class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.items = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.items[item] = cnt
        self.total += item.price * cnt

    def __str__(self):
        item_lines = []
        for item, cnt in self.items.items():
            item_lines.append(f"{item.name}: {cnt} pcs.")
        items_str = "\n".join(item_lines)
        return f"User: {self.user}\nItems:\n{items_str}\nTotal: {self.total}"

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

#3).

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name:{self.name}\nAge:{self.age}\nGender:{self.gender}"

print(Person("Alina",5,"Women"))

#4).

class Employee(Person):
    def __init__(self,salary,position):
        self.salary = salary
        self.position = position
    def __str__(self):
        return f"Salary:{self.salary}\nPosition:{self.position}"

print(Employee("Senior",500))

#5).

class BankAccount:
    def __init__(self,balance,owner):
        self.balance = balance
        self.owner = owner
    def __str__(self):
        return (f"Cash in:{self.balance} + {self.owner} = {self.balance+self.owner}\nCash out:{self.balance} - {self.owner} = {self.balance-self.owner}")

print(BankAccount(500,50))

#6.1).

class Read:
    def __init__(self,file):
        self.file = file
    def __str__(self):
        read = open(self.file, "r", encoding="utf-8")
        return read.read ()

print(Read("6.1.txt"))

#6.2).

class Write:
    def __init__(self,file):
        self.file = file
    def write (self):
        opening = open(self.file,"w",encoding="utf-8")
        opening.write("Hello")
        opening.close()


Write("6.2.2.txt")

#6.3).

class Read:
    def __init__(self,file):
        self.file = file
    def read_lines(self):
        with open(self.file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            return str(lines)

reader = Read("6.1.txt")
lines = reader.read_lines()
print(lines)