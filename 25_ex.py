## find numbers which are divisible by 7 and multiples of 5 between 1500 and 2700 (both included)

# n = []
# for i in range(1500,2701):
#     if i % 7 == 0 and i % 5 == 0:
#         n.append(str(i))
# print(n)


##liczby podzielne przez 3 i 5 z przedziału 0-49

# for i in range(50):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif i % 3 == 0:
#         print("fizz")
#         continue
#     elif i % 5 == 0:
#         print("buzz")
#         continue
#     print(i)


## zgadywanie liczby z przedziału 1 - 10

# import random

# count = 0
# n, x = random.randint(0,10), 0

# while n != x:
#     x = int(input("Guess a number between 1 and 10: "))
#     count = count + 1
# print("well guessed, you guessed", count, "times")


## odwracanie słów
# x = input("enter a word:")
# y = (x[::-1])

# print(y)

##liczby parzyste i nieparzyste

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# count_odd = 0
# count_even = 0

# for i in numbers:
#     if i %2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1

# print("number of even numbers:", count_even)
# print("number of odd numbers:", count_odd)

## przeliczanie wieku psa (przez pierwsze dwa lata pies ma 10.5 roku człowieka, przez kolejne każdy rok * 4)
# x = int(input("enter a dog's age in human years:"))

# if x < 2:
#     y = x * 10.5
# else:
#     y = 21 + (x - 2) * 4

# print("the dog's age is", y)

## write a program to create the multiplication table (from 1 to 10) of a number

# n = int(input("enter a number:"))

# for i in range (1,11):
#     x = n * i
#     print(n, "*", i, "=", x)

## pół choinki z cyferek
# for i in range(10):
#     print(str(i) * i)

## parzyste i nieparzyste
# x = [23, 4, -6, -9, 21, 9, 23, -9, -8]

# pos = []
# neg = []

# for i in range(len(x)):
#     if x[i] > 0:
#         pos.append(x[i])
#     else:
#         neg.append(x[i])

# print("positive:", pos)
# print("negative:", neg)

# n = "aeiou"
# x = str(input("Enter a sentence:"))

# count = 0
# for n in x:
#     count = count + 1
# print(count)

# y = len(x)
# print(y)