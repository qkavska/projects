# class Student:
#     def __init__(self, name, major, gpa, is_on_probation):
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation

#     def on_honor_roll(self):
#         if self.gpa >= 3.5:
#             return True
#         else:
#             return False
        

# student1 = Student("Jim", "Business", 3.1, False)
# student2 = Student("Mike", "HR", 3.5, True)

# print(student2.on_honor_roll())


# create Human's class and define every of them

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduceYou(self, welcome = "Hello"):
        return welcome + ", my name is " + self.name + " I am " + str(self.age)+ " years old."
    
obiect = Human("John", 28)
print(obiect.name)
print(obiect.introduceYou("Hi"))

obiect2 = Human("Adam", 19)
obiect2.name = "Adam"
print(obiect2.introduceYou())


# utwórz dwa obikety auto1 i auto2 w klasie Pojazd, o zdefiniowanych kryteriach

class Pojazd:
    def __init__(self, nazwa, color, rodzaj, wartosc):
        self.nazwa = nazwa
        self.color = color
        self.rodzaj = rodzaj
        self.wartosc = wartosc
        
    def info(self):
        return self.nazwa + " to " + self.color + " " + self.rodzaj + " warty " + str(self.wartosc) + " zl."
        
        
auto1 = Pojazd("Ferrari", "czerwony", "kabriolet", 6000)
print(auto1.info())
auto2 = Pojazd("Ikarus", "niebieski", "autobus", 10000)
print(auto2.info())



