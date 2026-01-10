def gmean (a, b):
    mean = ((a*b)/(a+b))
    print (mean)

def large (a, b):
    if (a>b):
        print ("", a, "is greater than ", b)
    else:
        print ("", b, "is greater than ", a)

a = 5
b = 6
large (a, b)
gmean (a, b)

c = 9
d = 8
large (c, d)
gmean (c, d)