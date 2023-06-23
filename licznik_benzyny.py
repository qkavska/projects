# km - liczba km
# cena - cena l benzyny
# ile - ilość spalanych litrów na 100 km


# def przelicznik():
#     km = float(input("wprowadź liczbę km: ")) 
#     ile = int(input("wprowadź ile litrów spala Twój samochód na 100 km: "))
#     cena = float(input("wprowadź cenę benzyny za l: ")) 

#     a = float(ile) * cena
#     b = (a * km)/ 100.0

#     print("przejazd", km, "km wyniesie Cię", round(b, 2), " zł")
# przelicznik()


# porównanie ceny diesla i ceny benzyny
def przejazd():
    km = float(input("wprowadź liczbę km: ")) 
    ile = int(input("wprowadź ile litrów spala Twój samochód na 100 km: "))
    cena1 = float(input("wprowadź cenę benzyny za l: ")) 
    cena2 = float(input("wprowadź cenę diesla za l: ")) 

    a1 = float(ile) * cena1
    b1 = (a1 * km)/ 100.0

    a2 = float(ile) * cena2
    b2 = (a2 * km)/ 100.0

    różnica1 = b1 - b2
    różnica2 = b2 - b1

    if b1 > b2:
        print("przejazd benzyną", km, "km wyniesie", b1, "zł, a przejazd dieslem -", b2, "zł, więc będzie droższy od diesla o", round(różnica1, 2), "zł")
    elif b2 > b1:
        print("przejazd dieslem", km, "km wyniesie", b2, "zł, a przejazd bęzyną -", b1, "zł, więc będzie droższy od benzyny o", round(różnica2, 2), "zł")
    else:
        print("ceny obu przejazdów są porównywalne")
przejazd()
