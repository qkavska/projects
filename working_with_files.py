
# file = open("mbox-short.txt")
# print(file)

## kiedy nie działa "open" -> with open + lokalizacja pliku

# with open("py/mbox-short.txt", "r") as f:
#     file = f.read()


## liczenie linii w pliku

# count = 0
# for i in file:
#     count = count + 1
# print("liczba linii:", count)

## or

# x = len(file)
# print("liczba linii:", x)


## przeszukiwanie pliku -> startsiwth

# with open("py/mbox-short.txt", "r") as file:
#     for line in file:
#         line = line.rstrip()
#         if line.startswith("From:"):
#             print(line)


## szukanie fragmentu napisu w innym napisie -> find

# with open("py/mbox-short.txt", "r") as file:
#     for line in file:
#         line = line.rstrip()
#         if line.find("@uct.ac.za") == -1:
#             continue
#         print(line)

## pisanie do pilu (dodawanie tekstu) -> write ("w" nadpisuje stary plik - tworzy nowy w starym, usuwa wszystko ze starego! "a" dodaje tekst do pliku)


## usuwanie pliku -> remove

# import os
# os.remove("py/twojastara.txt")


## zmiana nazwy pliku -> rename

# import os
# os.rename("py/text.txt", "test.txt")

# with open("py/file.txt", "w") as f:
#     f.write("dupa")
#     f.close()


## kopiowanie plikó -> shutil.copy

# import shutil
# x = r"C:\Users\kukaw\Git\py\file.txt"
# y = r"C:\Users\kukaw\Git\py\file3.txt"
# shutil.copy(x,y)
# print("Copied")

fname = input("Podaj nazwę pliku: ")

try:
    with open(fname, "r") as file:
        file.read()
except:
    print("Nie można otworzyć pliku o nazwie", fname)
    exit()

count = 0
for i in file:
    if i.startswith("file"):
        count = count + 1
        
print("Mamy", count, "linii z tematem wiadomości w pliku", fname)

