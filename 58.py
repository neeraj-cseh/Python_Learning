class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"{self.name} is {self.age} years old.")
p1 = Person("Mala", 23)
p2 = Person("Neeraj", 24)
p3 = Person("Srinivas", 25)
p1.info()
p2.info()
p3.info()