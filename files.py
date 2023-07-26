# file = open("test.txt", "a")

# if file.writable():
#    ile = file.write(input("Wprowadź dane: ") + "\n")

# file = open("test.txt", "r")

# if file.readable():
#     print("Zawartość pliku:", ile)
#     for l in file:
#         print(l)

# file.close()

# with open("py/produkty.txt") as f:

#     for produkt in f.readlines():
#         print(produkt)

# f.close()


# file = open("produkty1.txt", "w")
# file.write("hello")

# file.close()

# import subprocess
# subprocess.Popen("C:\Program Files\\Mozilla Firefox\\firefox")

# import subprocess
# subprocess.Popen("C:\Program Files (x86)\\OpenOffice 4\\program\\scalc")


# file = open("file.txt") 

# read all contents of file
# print(file.read())

# read n number of characters
# print(file.read(3))

# read one single line 
# print(file.readline())

# read line by line
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# file.close()

# read line by line 
# for line in file.readlines():
    # print(line)

# read file line by line and write riversed lines
with open("file.txt", "r") as file:
    content = file.readlines()
    reversed(content)
    with open("file.txt", "a") as writer:
        for line in reversed(content):
            writer.write(line)