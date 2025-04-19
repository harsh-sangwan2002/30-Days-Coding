with open("file.txt", "r") as file:
    content = file.read()
    
with open("file-copy.txt", "w") as file:
    file.write(content)