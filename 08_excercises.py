# def mul_or_sum(num1, num2):

#     product = num1 * num2
#     if product <= 1000:
#         return product
#     else:
#         return num1 + num2

# result = mul_or_sum(20, 30)
# print("the result is ", result)


# n = int(input("Enter number of elements: "))
# a = []

# for i in range(0, n):
#     elem = float(input("Enter element: "))
#     a.append(elem)

# avg = sum(a) / n
# print("Average of your list is: ", round(avg, 2))

        
# n = suma dwóch poprzednich liczb

a = 0
b = 1
print(a, end=", ")
for i in range (0, 10):
    print(b, end=", ")
    b = b + a
    a = b - a

# def fib(n):
#     if (n == 0):
#       return 0
#     if (n == 1):
#       return 1
#     return fib(n-1) + fib(n-2)
# print(fib(5))

# n = int(input("wprowadź liczbę: "))

# def num():
#     if n <= 10 or n == 11:
#         n_1 = n + 1
#         print(n_1)
#     else:
#         print(n_2)
#         n_2 = n - 1
# print(num())


# n = int(input("Enter number: "))

# sum = 0
# for num in range(1, n + 1, 1):
#     sum = sum + num
# average = sum / n

# print("average of ", n, "numbers is: ", average)
