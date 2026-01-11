# This is the KBC Game

name = input("Please Enter Your Name: ")
print ("\nLets start the game,",name)

def op(Q, A, B, C, D):
    print (Q, A, B, C, D )

op('''\nYour 1st question is - Which animal is known as the "Ship of the Desert"? ''', "\nA. Elephant", "B. Camel", "C. Horse", "D. Tiger")
ans1 = "B"
x = input("\nEnter your option: ")
if x == ans1:
    print ("You are right")
    p1 = 100
else:
    print ("You are wrong")
    p1 = 0

op('''\nYour 2nd question is - Which planet in our solar system is known as the "Red Planet"? ''', "\nA. Jupiter", "B. Venus", "C. Mars", "D. Saturn")
ans2 = "C"
x = input("\nEnter your option: ")
if x == ans2:
    print ("You are right")
    p2 = 100
else:
    print ("You are wrong")
    p2 = 0

op('''\nYour 3rd question is - In the human body, which of these is the hardest substance? ''', "\nA. Bone", "B. Skin", "C. Nail", "D. Tooth Enamel")
ans3 = "D"
x = input("\nEnter your option: ")
if x == ans3:
    print ("You are right")
    p3 = 100
else:
    print ("You are wrong")
    p3 = 0

print ("Your final score is - ", p1 + p2 + p3)