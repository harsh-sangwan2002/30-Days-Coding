try:
    with open("file3.txt","r") as file:
        content = file.read()
except:
    print("File not found!")