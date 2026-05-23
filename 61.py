class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"{self.name} is {self.age} years old.")
    
class Child(Parent):
    def lang(self):
        print(f"{self.name} can speak multiple languages.")

p1 = Parent("Neeraj", 25)
p1.info()

c1 = Child("Srinivas", 15)
c1.info()
c1.lang()