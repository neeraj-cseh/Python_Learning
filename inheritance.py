class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Details(self):
        print(f"{self.name} age is {self.age}")

class Child(Parent):
    def Language(self):
        print("Mother tongue is Telugu")

a = Parent("Neeraj", 23)
a.Details()
b = Child("Srinivas", 22)
b.Language()
