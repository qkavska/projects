# x = int(input("enter your price: "))
# if x >= 500:
#     elem = x - (x * 0.25)
#     elem2 = x * 0.25
#     print("your price discounted is: ", round(elem, 2))
#     print("discount is: ", elem2)
# else:
#     print("your price is not discounted")

# y = float(input("define your price: "))

# if y <= 200:
#     price = y - (y * 0.2)
#     disc = y * 0.2
#     print("your price discounted is: ", round(price, 2))
#     print("your discount is: ", disc)
# elif y >= 200:
#     price = y - (y * 0.3)
#     disc = y * 0.3
#     print("your discount is: ", round(price, 2))
#     print("your discount is: ", disc)


#media expert
# n = int(input("define number of products: "))
# a = []
# x = float(input("define price of this product: "))
# if n == 1:
#     price = x - (x * 0.1)
# elif n == 2:
#     price = x - (x * 0.2)
# elif n == 3:
#     price = x - (x * 0.5)
# elif n == 4:
#     price = x - (x * 0.75)
# elif n == 5:
#     price = x - (x * 0.99)
# print("your discounted price is: ", round(price, 2))

# is_male = False
# is_tall = False

# if is_male and is_tall:
#     print("you're a tall male")
# elif is_male and not is_tall:
#     print("you aren't a tall male")
# elif is_tall and not is_male:
#     print("you're a tall female")
# else:
#     print("you aren't male neither tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3,40,5))