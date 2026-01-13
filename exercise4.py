string = input("Enter: ")
words = string.split(" ") 
coding = int(input("1 for Coding\n2 for Decoding: "))
# if coding == 1:
#     coding = True
#     print("Start Encoding")
# elif coding == 2:
#     coding = False
#     print("Start Decoding")
# else:
#     print("Invalid input")

if (coding == 1):
    print("Start Encoding")
    nwords = []
    for word in words:
        if (len(word)>=3):
            r1 = 'abc'
            r2 = 'xyz'
            nstring = r1 + word[1:] + word[0] + r2
            nwords.append(nstring)
        else:
            nwords.append(word[::-1])
    print("".join(nwords))

elif (coding == 2):
    print("Start Decoding")
    nwords = []
    for word in words:
        if (len(word)>=3):
            nstring = word[3:-3]
            nstring = nstring[-1] + nstring[:-1]
            nwords.append(nstring)
        else:
            nwords.append(word[::-1])
    print("".join(nwords))

else:
    print("Invalid input")