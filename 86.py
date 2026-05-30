# numbers = [1, 2, 3, 4, 5]
# while n := len(numbers) > 0:
#     print(numbers.pop())

name = ["Mala", "Neeraj", "Srinivas"]
if (name := input("Enter your name:") in name):
    print(f"Hello, {name}!")
else:
    print("Name not found.")