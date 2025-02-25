phonebook = {
    "Alice":"703-493-1834",
    "Bob":"857-384-1234",
}

name = input("Enter your name: ")
print(phonebook.get(name,"Not found"))