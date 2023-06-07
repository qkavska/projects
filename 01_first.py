
# str
#name = "Kamil"
#name = 'Kamil'
#name = """Kamil""" - oddaje w różnych linijkach
#print (name)

# int, float, complex
# a = 5 int
# b = 3.0 float - liczba zmiennoprzecinkowa

# operatory matematyczne
# print (a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print (a%b) - reszta z dzielenia
# print(a ** b) #- potęgowanie

# a = a + 1 - można dodać liczbę
# print(a)

# a += 2 - dodawanie o 2
# a -= 2 
# a *= 2 
# a /= 2
# print(a)

# bool true/false
#is_sky_blue = True
#is_sun_blue = False

#print(is_sky_blue)
#print(is_sun_blue)

#print(type(name))
#print(type(a))
#print(type(is_sky_blue))

# first = 2
# second = "3"

# print(first + int(second))
# print(str(first)+second)

# operatory porównania - zwracają wartość typu bool

# a = 50000
# b = 50000

# print(a == 5) - czy jest równe - equality operator
# print(a != 5) - czy nie jest równe
# print (a > 5)
# print (a < 5)
# print (a >= 5)
# print (a <= 5)
# print (a == b)
# print (a is b) - identity operator

# operatory logiczne
# a = 5
# print(a > 2 and a > 10)
# print(a > 2 or a > 10)

# string

# name="Kamil"
# print(len(name)) - zwraca ilość znaków w wyrazie
# print(name.capitalize()) - zmienia pierwszą literę na wielką
# print(name.upper()) - zwiększa litery
# print(name.lower()) - zmniejsza litery
# print(name[0]) - zwraca 1 literę
# print(name[0:3]) - zwraca 3 pierwsze litery

# channel = "jak nauczyć się programowania"
# print(channel.split(" ")) - rozdzielenie

# join_string = "-"
# print(join_string.join(['jak', 'nauczyć', 'się'])) - połączenie

# first_name = "Kamil"
# last_name = "Nowak"
# # print(first_name + " " + last_name)
# join_string = " "
# print(join_string.join([first_name, last_name]))

# james_bond = 7
# print(str(james_bond).zfill(3))

# instrukcje warunkowe

# light = input ("What's the light? (red, green, yellow) ")
# if light == "red":
#     print("wait!")
# elif light == "yellow":
#     print("let's...")
# elif light == "green":
#     print("go!")
# else:
#     print("no value")

# number = 1

# while number < 6:
#     print(number)
#     number += 2

# for number in range(0,10):
#     if number == 5:
#         continue 
#         break
#     print(number)

# struktury danych
# lista

# names_list = [] - nawias kwadratowy
# names_list.append("Kamil") - dodawanie elementów do listy
# names_list.append("Mariusz")
# print(names_list)

# names_list = ["Kamil", "Mariusz"]
# print(names_list)

# names_list = ["Kamil", "Mariusz", "Adam", "Kamil"]

# # names_list.reverse() - odwrócenie kolejności
# names_list.sort() 
# print(names_list)

# for name in names_list:
#     print(name)
#     print(names_list[2])

# print(names_list.count("Kamil")) - ile razy występuje dana zmienna
# print(len(names_list))

# print(names_list)
# print()
# print(names_list.pop(1)) - zwraca konkretny element na liście, usuwa z        następnych list
# print()
# print(names_list)

# names_list.remove("Kamil") - usuwa pierwsze wystąpienie danego elementu
# print(names_list)

# names_list.clear() - usuwa całą listę
# print(names_list)

# names_list2 = ["Dominik", "Anna"]
# names_list3 = names_list + names_list2 - łączenie list
# print(names_list3)

# krotka 
# person = ("Kamil", "Nowak") - nawias zwykły
# print(len(person))

# set (zbiór) - nie można duplikować danych

# set_name = {"Kamil", "Mariusz", "Kamil"}
# print(set_name)

# set_name = set()
# set_name.add("Kamil")
# set_name.add("Mariusz")
# # set_name.remove("Kamil")
# set_name.discard("Mariusz")
# print(set_name)

# set_name = set()
# set_name.add("Kamil")
# set_name.add("Mariusz")
# set_name2 = {"Dominik", "Anna"}
# set_name3 = set_name.union(set_name2)
# for name in set_name3:
#     print(name)

# set_name3 = set_name.difference(set_name2)
# set_name.clear()
# for name in set_name:
#     print(name)

# names_list.extend(set_name2) - łączenie listy i setu
# print(names_list)

# dictionary

# countries_and_capitals = {"Poland":"Warsaw","Germany":"Berlin"}
# countries_and_capitals["Hungary"] = "Budapest"
# # print(countries_and_capitals)

# for country in countries_and_capitals.keys():
#     # print(country)

# for capital in countries_and_capitals.values():
#     print(capital)

# for capital, country in countries_and_capitals.items():
#     print(country + "-" + capital)

# print(countries_and_capitals["Poland"])
# print(countries_and_capitals.get("Poland"))

# print(countries_and_capitals["USA"]) 
# print(countries_and_capitals.get("USA")) - pokazuje, że nie ma 

# print(countries_and_capitals.setdefault("USA", "Washington DC"))
# print(countries_and_capitals)

# if "USA" in countries_and_capitals:
#     print("Yes")
# else:
#     print("No")

# countries_and_capitals.clear()
# print(countries_and_capitals

# countries_information = {}
# countries_information["Poland"] = ("Warsaw", 38.9)
# countries_information["Hungary"] = ("Budapest", 5.47)
# countries_information["Hungary"] = ("Budapest", 5.47)
# countries_information["Hungary"] = ("Budapest", 5.47)

# # for country in countries_information.keys():
# #     print(country)

# #     country = input("o jakim kraju?")

#     country_information = countries_information.get(country)
#     print()
#     print(country)
#     print("-----")
#     print("Stolica:" + country_information[0])
#     print("Liczba mieszkańców:" + " " + str(country_information[1]))


# funkcje

# countries_information = {}
# countries_information["Poland"] = ("Warsaw", 38.9)
# countries_information["Hungary"] = ("Budapest", 5.47)


# def show_country_info(country):

#     country_information = countries_information.get(country)
#     print()
#     print(country)
#     print("-----")
#     print("Stolica:" + country_information[0])
#     print("Liczba mieszkańców:" + " " + str(country_information[1]))

# for country in countries_information.keys():
#     print(country)

#     country = input("o jakim kraju?")
#     show_country_info(country)

# pliki do odczytu

# file = open("file.txt", "w+")
# countries_and_capitals = {"Poland":"Warsaw","Germany":"Berlin",                     "Hungary":"Budapest"}

# for country, capital in countries_and_capitals.items():
#     file.write(country + "-" + capital + "\n")

# file.close()

# file = open("file.txt")
# for line in file.readlines():
#     print(line.strip())

#     file.close()
