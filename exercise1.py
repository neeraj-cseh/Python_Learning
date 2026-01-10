a = int(input("\nEnter the first value: "))
b = int(input("\nEnter the second value: "))
print ("\nAvailable Operations: \n1.Addition \n2.Subtraction \n3.Multiplication")
op = int(input("\nEnter the required operation: "))

match op:
    case _ if op == 1:
        print("The output is: ", a+b)

    case _ if op == 2:
        print("The output is: ", a-b)

    case _ if op == 3:
        print("The output is: ", a*b)

    case _:
        print("Sorry there is some error...!")