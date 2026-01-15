# f = open('test.txt', 'r')
# text = f.read()
# print(text)
# f.close

# f = open('text.txt', 'w')
# i = 0
# for i in range (0, 6):
#     f.write(f"Hello {i}")
# f.close()

# f = open('text.txt', 'a')
# i = 0
# for i in range (0, 6):
#     f.write(f"Hello {i}")
# f.close()

# with open('text.txt', 'r') as f:
#     text = f.read()
#     print (text)

# f = open('text.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         print("Completed")
#         break
#     print(line)

# f = open('text.txt', 'w')
# lines = ['A\n', 'B\n', 'C\n']
# f.writelines(lines)
# f.close()

# f = open('text.txt', 'a')
# lines = ['A\n', 'B\n', 'C\n']
# f.writelines(lines)
# f.close()

# f = open('text.txt', 'w')
# lines = ['A', 'B', 'C']
# for line in lines:
#     f.write('\n' + line + '\n')
# f.close()


# f = open('text1.txt', 'w')
# lines = ['1234567890Neeraj']
# for line in lines:
#     f.write(line)
# f.close()

# with open('text1.txt', 'r') as f:
#     f.seek(10)
#     data = f.read(6)
#     print(data)

# with open('text1.txt', 'r') as f:
#     data = f.read(10)
#     current_position = f.tell()
#     f.seek(current_position)
#     print(current_position)
#     print(data)

# with open('text1.txt', 'w') as f:
#     f.write("Hello World")
#     f.truncate(5)

# with open('text1.txt', 'r') as f:
#     print(f.read())