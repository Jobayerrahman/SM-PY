class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def myfunc(self):
        print("My name is " + self.name)
p1 = Person("John",45)

print(p1.name)
print(p1.age)
p1.myfunc()