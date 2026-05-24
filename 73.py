class Person:
    name = "Neeraj"

    def __len__(self):
        i = 0
        for char in self.name:
            i += 1
        return i

p = Person()
print(p.name)
print(len(p))