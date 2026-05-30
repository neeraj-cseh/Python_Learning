class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"{self.x}X + {self.y}Y + {self.z}Z"
    def __add__(self, a):
        return vector(self.x + a.x, self.y + a.y, self.z + a.z)

v1 = vector(1, 2, 3)
print(v1)
v2 = vector(4, 5, 6)
print(v2)
v3 = v1 + v2
print(v3, type(v3))