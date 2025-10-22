# ---------------------- Real-Life Example ----------------------


class Person:
    def __init__(self, name, age):  # __init__ runs automatically when object is created
        self.name = name  # self.name belongs to the object
        self.age = age

    def myfunc(self):  # method using self to access object data
        print("My name is " + self.name)


p1 = Person("John", 45)  # creating an object p1
print(p1.name)  # access property
print(p1.age)
p1.myfunc()  # calling method


# ---------------------- Real-Life Example ----------------------


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def introduce(self):
        print(f"Hi, I am {self.name} and my roll number is {self.roll}.")


student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

student1.introduce()
student2.introduce()


# ---------------------- Real-Life Example ----------------------


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show_balance(self):
        print(f"{self.account_holder} has a balance of ${self.balance}.")


account1 = BankAccount("Rahim", 5000)
account2 = BankAccount("Karim", 12000)

account1.show_balance()
account2.show_balance()
