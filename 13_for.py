
# for index in range(5):
#     if index == 0:
#         print("first iteration")
#     else:
#         print("not first")

# def raise_to_power(base_num, pow_num):
#     result = 2
#     for index in range(pow_num):
#         result = result * base_num
#     return result


# print(raise_to_power(2, 2))

# s = 0
# n = int(input("Enter number: "))
# for i in range(1, n + 1, 1):
#     s += i
# print("\n")
# print("sum is: ", s)

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# n = 5
# for i in range(1, n + 1, 1):
#     for j in range(1, i + 1, 1):
#         print(j, end="")
#     print("")

# n = int(input("Enter range: "))
# while n != 0:
#     print(n, end=" ")
#     n -= 1

# display first 7 multiples of 7
# count = 0
# for i in range(100):
#     if i%7 == 0:
#         print(i, end=" ")
#         count = count + 1
#         if count == 8:
#             break

# kwadrat liczb z listy
# x = [2,3,4,5,6,7,8]
# z = []
# for i in range(len(x)):
#     z.append(x[i]**2)
#     print(z, end="")

# liczby ujemne i dodatnie
# x = [23, 4, -6, 23, -9, 21, 3, -45]
# pos = []
# neg = []
# for i in range(len(x)):
#     if x[i] < 0:
#         neg.append(x[i])
#     else:
#         pos.append(x[i])
# print("positive numbers are: ", pos)
# print("negative numbers are: ", neg)

# typy
# x = [23, "Python", 23.98]
# y = []
# for i in range(len(x)):
#     y.append(type(x[i]))
# print(x)
# print(y)

# liczby parzyste i nieparzyste 
# x = [10, 23, 24, 35, 65, 78, 90]
# odd = []
# even = []
# for i in range(len(x)):
#     if x[i] % 2 == 0:
#         even.append(x[i])
#     else:
#         odd.append(x[i])
# print("odd numbers are:", odd)
# print("even numbers are: ", even)

# count = 0
# for lista in [9, 10, 18, 99, 102, 456]:
#     count = count + 1
# print("tyle elementów:", count)

# x = None
# y = [1, 2, 3, 10, -8, 49, 156, -92]
# for i in y:
#     if x is None or i < x:
#         x = i
# print("najmniejsza liczba: ", i)

# x = None
# y = [1, 2, 3, 10, -8, 49, 156, -92]
# for i in y:
#     if x is None or i > x:
#         x = i
# print("największa liczba: ", x)


# count = 0
# total = 0.0


# while True:
#     num = input("Wprowadź liczbę:")

#     if num == "gotowe":
#         break
#     print(num)
#     try:
#         sum = float(num) 
#     except:
#         print("Musisz podać liczbę.")
#         continue

#     count = count + 1
#     total = total + sum

# print("Gotowe!", "Tyle razy zgadywałeś:", count, "suma liczb:", total, "średnia:", round(total/count, 2))


# x = None
# y = [3, 5, 6, 90, -2]

# for i in y:
#     if x is None or i < x:
#         x = i
# print("Najmniejsza", x)


# y = [3, 5, 6, 90, -2]
# x = min(y)
# print(x)

# z = max(y)
# print(z)

# sum = 0
# iloczyn = 1
# for i in range(5,1000,5):
#     sum += i
#     iloczyn *= i
# print(sum)
# print(iloczyn)


#tabliczka mnożenia

# for i in range(1,11):
#     for y in range(1,11):
#         print("{:3}".format(y*i), end=" ")
#     print("")

#formatowanie
# wycentrowany = 2
# do_prawej = 5
# do_lewej = 3

# print(f"|{wycentrowany:^3}|{do_prawej:>3}|{do_lewej:<3}|")
# print(f" {i*y:>3} ", end="|") #formatowanie (3 bo 3 mejsca są potrzebne, zeby wyszło równo, bo ostatnia liczba to 100)



