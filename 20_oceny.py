
def oceny(a):
        try:
            for i in range(0,1):   
                if a >= 0.9:
                    i = 5.0
                    print("Ocena", str(i))
                elif a >= 0.8:
                    i = 4.5
                    print("Ocena", str(i))
                elif a >= 0.7:
                    i = 4.0
                    print("Ocena", str(i))
                elif a >= 0.6:
                    i = 3.5
                    print("Ocena", str(i))
                elif a >= 0.5:
                    i = 3.0
                    print("Ocena", str(i))
                elif a < 0.5:
                    i = 2.0
                    print("Ocena", str(i))       
                else:
                    print("Błąd, wartość poza zakresem.")
        except:
                print("Niepoprawna wartość.")
a = float(input("Wprowadź wartość: "))
oceny(a)