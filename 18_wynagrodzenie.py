
def wynagrodzenie(x, y):
    try:  
        if y > 160:
            z = (y - 160) * (1.5 * x)
            a = float((x * y) + z)
            brut = a * 1.23
            print("Twoje wynagrodzenie + nadgodziny wynosi:", round(a, 2), "pln netto, a brutto:", round(brut, 2), "pln")
        elif y > 200:
            h = (y - 160) * (2 * x)
            b = float((x * y) + h)
            brut2 = b * 1.23
            print("Twoje wynagrodzenie + nadgodziny wynosi:", round(b, 2), "pln netto, a brutto:", round(brut2, 2), "pln")
        else:
            k = x * y
            print("Twoje wynagrodzenie wynosi:", k, "pln")
    except:
            print("Musisz wprowadzić wartość liczbową!")

x = float(input("Podaj stawkę za godzinę: "))
y = int(input("Podaj liczbę godzin: "))

wynagrodzenie(x, y)

