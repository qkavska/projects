# #napis odwrotnie, kązda litera w oddzielnej linijce
# fruit= "banan"
# # 1.
# for i in reversed(fruit):
#     print(i)

# # 2.
# for i in fruit[::-1]:
#     print(i)

##zmiana w napisie
# greeting = "Witaj świecie"
# new_greeting = "V" + greeting[1:]
# print(new_greeting)

## zliczanie ilości znaków w wyrazie
# word = "banan"
# count = 0
# for i in word:
#     count = count + 1
# print(count)

## lub

# word = "banan"
# x = len(word)
# print(x)

## wielkie litery
# word = "banan"
# x = word.upper()
# print(x)

## szukanie pozycji znaku

# word = "banan"
# x = word.find("b")
# print(x)

##parsowanie napisów

# text = "X-DSPAM-Confidence: 0.8475 bbb-13-78"
# a = text.find(":")
# b = text.find("b", a)
# c = text[a+1:b]
# print(c)


## operator formatowania (%d, %g, %s)

# camels = 42
# "%d" % camels
# print(camels)

# text = "przez %d lata widziałem %g %s" % (3, 0.9, "wielbłąda")
# print(text)

## zamiana wyrazów
# text = "banan"
# text1 = "dupa"
# c = text.replace(text,text1)
# print(c)

## liczenie ilości wyrazów
# text = "Merry christmas"
# c = len(text.split())
# print(c)