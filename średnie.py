#program oblicza średnią arytmetyczną z dowolnej ilości liczb

# x = int(input("Wprowadź z ilu liczb chcesz obliczyć średnią: "))
# sum = 0
# for i in range(0,x):
#     sum += int(input("Wprowadź liczbę: "))
#     y = sum/x
# print("Średnia arytmetyczna z Twoich liczb to:", round(y, 2))


#program oblicza średnią harmoniczną (n)/(1/a1)+(1/a2)+...+(1/an) z dowolnej ilości liczb

# x = int(input("Wprowadź z ilu liczb chcesz obliczyć średnią: "))
# sum = 0
# for i in range(0,x):
#     sum += 1/int(input("Wprowadź liczbę: "))
#     y = x/sum
# print("Średnia harmoniczna z Twoich liczb to:", round(y, 2))


#program oblicza średnią geometryczną (a1*a2*...*an)**1/n z dowolnej ilości liczb (podwójna gwiazdka to pierwiastek), iloczyn nie może równać się 0!

# x = int(input("Wprowadź z ilu liczb chcesz obliczyć średnią: "))
# iloczyn = 1
# for i in range(0,x):
#     iloczyn *= int(input("Wprowadź liczbę: "))**(1/x)
# print("Średnia geometryczna z Twoich liczb to:", round(iloczyn, 2))


# program oblicza średnią kwadratową ((a1^2+a2^2+...+an^2)/n)**1/2 z dowolnej ilości liczb 

# import math

# x = int(input("Wprowadź z ilu liczb chcesz obliczyć średnią: "))
# sum = 0
# for i in range(0,x):
#     sum += (int(input("Wprowadź liczbę: ")))**2
#     y = math.sqrt(sum/x)
# print("Średnia kwadratowa z Twoich liczb to:", round(y, 2))