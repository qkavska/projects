# x = 15
# y = 20

# if x > y:
#     print("yes")
# elif x < y:
#     print("no")
# else:
#     print("none")


x = int(input("Wprowadź liczbę: "))
if (x >= 10 and x <= 100) or (x >= 100 and x <= 200):
    print("Liczba jest z przedziału.")
else:
    print("Zła wartość.")