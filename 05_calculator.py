# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

# def add(a, b):
#     answer = a + b
#     print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

# def sub(a, b):
#     answer = a - b
#     print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

# def mul(a, b):
#     answer = a * b
#     print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

# def div(a, b):
#     answer = a / b
#     print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

# while True:
#     print("A. Addition")
#     print("B. Subtraction")
#     print("C. Multiplication")
#     print("D. Division")
#     print("E. Exit")

#     choice = input("Input your choice: ")

#     if choice == "a" or choice == "A":
#         print("Addition")
#         a = int(input("input first number: "))
#         b = int(input("input second number: "))
#         add(a, b)
#     elif choice == "b" or choice == "B":
#         print("Subtraction")
#         a = int(input("input first number: "))
#         b = int(input("input second number: "))
#         sub(a, b)
#     elif choice == "c" or choice == "C":
#         print("Multiplication")
#         a = int(input("input first number: "))
#         b = int(input("input second number: "))
#         mul(a, b)
#     elif choice == "d" or choice == "D":
#         print("Division")
#         a = int(input("input first number: "))
#         b = int(input("input second number: "))
#         div(a, b)
#     elif choice == "e" or choice == "E":
#         print("Program ended")
#         quit()

num1 = float(input("enter first number: "))
op = input("enter operator: ")
num2 = float(input("enter second number: "))

if op == "+":
    print(round(num1 + num2, 2))
elif op == "-":
    print(round(num1 - num2, 2))
elif op == "*":
    print(round(num1 * num2, 2))
elif op == "/":
    print(round(num1 / num2, 2))
else:
    print("Inwalid operator")







