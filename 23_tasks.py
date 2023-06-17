## selling products, which costs 5.0 for one and why buy more than one the discount for all of them is 10 % and tax is 7 % for each one

# price = 5
# discount = 0.1
# tax = 1.07

# a = int(input("enter number of products: "))

# if a > 1:
#     x = (price * tax) * a 
#     y = x - (x * discount)
#     print("your price is: ", y)
# else:
#     b = round((price * tax),2)
#     print("your price is: ", b)


## adding a name to the list by input

# queue = ['John', 'Amy', 'Bob', 'Adam']
# x = str(input("Enter name:"))
# queue.append(x)
# print(queue)


## select min and max item by list of items (outliers: smallest and largest) and remove them and then sum up remaining items 

# data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 
#     8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 
#     9, 100, 444, 78]

# x = min(data)
# y = max(data)
# data.remove(x)
# data.remove(y)
# z = sum(data)
# print(z)


## Imagine you are a scientist looking at a new type of cell under the microscope. This type of cell divides itself into 2 daughter cells every 24 hours, meaning that the cell population duplicates every day.


## Complete the code to take the initial cell population and the number of days you are observing the cells to calculate the cell population at the end of each day in the following format

# cells = int(input("Enter number of cells:"))
# days = int(input("Enter number of days:"))

# counter = 1
# while counter < days + 1:
#   cells = cells * 2
#   print("Day " + str(counter) + ": " +str(cells))
#   counter = counter + 1

## Define the run() function that will take the given list of games and the N number as arguments and output the corresponding game with the N index from the list. If the user enters an invalid number that is out of the list range, the program should output "Unknown".

# games = ["Alien Shooter", "Tic Tac Toe", "Snake", "Puzzle", "Football"]

# choice = int(input())

# def run(games, choice):
#     if choice >= 0 and choice <= 4:
#         print(games[choice])
#     else:
#        print("Unknown")

# run(games, choice)


# def sum(x):

#     res = 0
#     for i in range(x):
#         res+=i
#     return res

# print(sum(4))

##hint: 0 + 1 = 0, 1 + 1 = 1, 2 + 1 = 2, 3 + 1 = 3

