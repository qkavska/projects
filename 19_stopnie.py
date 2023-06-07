def stopnie():

    try:
        x = int(input("Podaj temperaturę w stopniach Celsjusza: "))
        y = float((x * 9/5) - 32)
        print("To będzie", y, "stopni Fahranheita")
    
    except:
        z = int(input("Muisz wprowadzić liczbę: "))
        print(z)

stopnie()
