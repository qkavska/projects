word = "11"
with open(r"C:\Users\kukaw\OneDrive\Dokumenty\moje\py\produkty.txt", "r") as fp:
   lines = fp.readlines()
for line in lines:
     if line.find(word) != -1:
         print("line's number:", lines.index(line))

