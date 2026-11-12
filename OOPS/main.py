# class cash:
#     def __init__(self,name,age,amount):
#         self.name = name
#         self.age = age
#         self.amount = amount
#         self.option()

#     def cash(self):
#         print("Cash amount:",self.amount)
#         self.message()

#     def card(self):
#         print("Card amount:",self.amount + 50)
#         self.message()

#     def debit(self):
#         print("Debited amount:",self.amount + 100)
#         self.message()

#     def credit(self):
#         print("Credited amount:",self.amount + 150)
#         self.message()

#     def acc_details(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         self.message()

#     def bal(self):
#         print("Balance:",self.amount)
#         self.message()

#     def message(self):
#         print("Thank you!!!...")

#     def option(self):
#         while True:
#             print("\n1.cash")
#             print("2.card")
#             print("3.debit")
#             print("4.credit")
#             print("5.acc_details")
#             print("6.balance")
#             print("7.exit")

#             m = int(input("Enter your choice:"))

#             match(m):
#                 case 1:
#                     self.cash()
#                 case 2:
#                     self.card()
#                 case 3:
#                     self.debit()
#                 case 4:
#                     self.credit()
#                 case 5:
#                     self.acc_details()
#                 case 6:
#                     self.bal()
#                 case 7:
#                     print("Thank you!!!...")
#                     break
#                 case _:
#                     print("Invalid Number")


# c = cash("sri",21,1000)

# class stack:
#     def __init__(self):
#         self.a = ""
#         self.option()

#     def push(self):
#         n = input("Enter number:")
#         self.a += n
#         self.message()

#     def pop(self):
#         n = input("Enter number:")
#         if n in self.a:
#             self.a = self.a.replace(n, "", 1)
#         else:
#             print("Number not found")
#         self.message()

#     def display(self):
#         print("Stack:", self.a)
#         self.message()

#     def message(self):
#         print("Thank you!!!...")

#     def option(self):
#         while True:
#             print("\n1.Push")
#             print("2.Pop")
#             print("3.Display")
#             print("4.Exit")

#             m = int(input("Enter choice:"))

#             match(m):
#                 case 1: self.push()
#                 case 2: self.pop()
#                 case 3: self.display()
#                 case 4: break
#                 case _:
#                     print("Invalid Number")

# s = stack()


# class Vehicle:
#     def __init__(self,r1,r2,f):
#         self.distance = r2-r1
#         self.fuel = f

# class Activa(Vehicle):
#     def mileage(self):
#         print("Activa -",int(self.distance/(self.fuel*6)),"MPG")

# class Dio(Vehicle):
#     def mileage(self):
#         print("Dio -",int(self.distance/(self.fuel*3)),"MPG")

# class Pulzar(Vehicle):
#     def mileage(self):
#         print("Pulzar -",int(self.distance/self.fuel),"MPG")


# r1 = int(input())
# r2 = int(input())
# f = int(input())

# a = Activa(r1,r2,f)
# d = Dio(r1,r2,f)
# p = Pulzar(r1,r2,f)

# a.mileage()
# d.mileage()
# p.mileage()




















    

















