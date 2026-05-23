class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"{self.name} is {self.age} years old.")
    
class Child(Parent):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang

    def speak(self):
        print(f"{self.name} can speak {self.lang}.")

p1 = Parent("Neeraj", 25)
p1.info()

c1 = Child("Srinivas", 15, "Telugu")
c1.info()
c1.speak()