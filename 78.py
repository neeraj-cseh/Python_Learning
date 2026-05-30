class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print (f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    def make_sound(self):
        print (f"{self.name} barks.")

animal = Animal("Generic Animal", "Unknown")
dog = Dog("Buddy", "Golden Retriever")
animal.make_sound()  # Output: Generic Animal makes a sound.
dog.make_sound()     # Output: Buddy barks.