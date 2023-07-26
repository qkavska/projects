
try:
    with open('file.txt', "r") as reader:
        reader.read()
except:
    print("failure")
finally:
    print("cleaning up resources")