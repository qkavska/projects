class Chef:
    def make_chicken(self):
        print("The chef makes chicken")
    def make_salad(self):
        print("The chef makes a salad")
    def make_special_dish(self):
        print("The chef makes bbq ribs")

# chef = Chef()
# chef.make_special_dish()

class ChineseChef(Chef):
    def make_chicken(self):
        print("The chef makes chicken")
    def make_salad(self):
        print("The chef makes a salad")
    def make_special_dish(self):
        print("The chef makes special dish")
    def make_fried_rice(self):
        print("The chef fried rice")

    ChineseChef = ChineseChef()
    ChineseChef.make_special_dish()