class Person:
    name = "Neeraj"
    age = 24
    def info(self):
        print(f"{self.name} is {self.age} years old.")
p1 = Person()
p2 = Person()
p3 = Person()
p2.name = "Srinivas"
p2.age = 25
p3.name = "Mala"
p3.age = 23
p1.info()
p2.info()
p3.info()