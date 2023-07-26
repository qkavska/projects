# lucky_numbers = [42, 8, 15, 18, 29, 33, 67]
# lists = ["Kevin", "Karen", "Jim", "Toby", "Alan"]
# # lists [1] = "Mike"
# # lists.extend(lucky_numbers)
# # lists.append("Creed")
# # lists.insert(1, "Kelly")
# # lists.remove("Jim")
# # lists.clear()
# # lists.pop()
# # lists.index("Jim")
# # lists.count("Karen")
# # lucky_numbers.sort()
# # lucky_numbers.reverse()
# lists2 = lists.copy()
# print(lists2)


#grid

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]

# # print(number_grid[2][2])

# for row in number_grid:
#     for col in row:
#         print(col)


# list - rozbijanie słowa na litery w liście
# count = 0
# word = 'spam'
# for letter in word:
#     t = list(word)
#     count += 1
# print(t, count)


# split - rozbijanie napisu na pojedyncze słowa w liście

# x = 'Twoja stara pierze w rzece'
# y = x.split()
# z = len(y)
    
# print(y, z)


# join - łączenie pojedynczych słów w liście w napis
# a = ['Twoja', 'stara', 'pierze', 'w', 'rzece']
# x = ' '
# print(x.join(a))

# fhand = open('mbox-short.txt')
# for line in fhand:
#     word = line.split()
#     if len(word) == 0: continue
#     if word[0] != 'From': continue
#     print(word[2])

fhand = open('mbox-short.txt')
# count = 0
# x = []


# pobieranie wartości od użytkownika, liczenie sumy i średniej z listy
# x = []
# liczba = int(input("Wprowadź liczbę: "))

# while liczba > 0:
#     x.append(liczba)
#     liczba = int(input("Wprowadź kolejną liczbę: "))

# for i in x:
#     z = sum(x)
#     k = len(x)
#     j = z/k
# print(x, "Suma wartości z listy to:", z, "a średnia to:", j)


## tworzenie listy, które przechowuje słowa z pliku

# with open('romeo.txt', "r") as fhand:

#     x = fhand.read() # czytanie programu linia po linii
#     y = x.split() # rozdzielenie linii na listę słów
#     z = [] # tworzenie nowej listy do przechowania słów

# for i in y: # przechodzenie przez wszystkie słowa w linijkach pliku 
#     if i not in z: #sprawdzenie czy elementów nie ma na liście, jeśli nie ma to
#         z.append(i) #dodanie elementów do listy

# z.sort() # sortowanie listy w kolejności alfabetycznej
# print(z)


## ćwiczenie z listą

# numlist = []
# while True:
#     inp = input("Wprowadź liczbę: ")
#     if inp == "done": 
#         break
#     value = float(inp)
#     numlist.append(value)

# x = min(numlist)
# y = max(numlist)
# print("największa wartość z Twojej listy to:", y, "najmniejsza wartość z Twojej listy to:", x)

