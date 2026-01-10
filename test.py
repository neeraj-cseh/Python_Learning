x = 4
match x:
    case 0:
        print("X == 0")
    
    case 4 if x % 2 == 0:
        print ("x % 2 == 0 and x is 4")

    case _ if x < 10:
        print ("x<10")

    case _:
        print (x)