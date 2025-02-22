# Strings are immutable sequences of characters. They are enclosed in single or double quotes.
my_first_string = "Hello World!"
print(my_first_string)

# Convert string to upper-case
print(my_first_string.upper())

# Convert string to lower-case
print(my_first_string.lower())

# Convert string to title-case
print(my_first_string.title())

message = "Hey! how are you doing?"
print(message[3])

# Split in the string
res = my_first_string.split(" ")
print(res)

# Join
res = " ".join(res)
print(res)

# Replace in the string
message = message.replace("Hey","Hello")
print(message)

algorithm = "Neural Networks"
print(algorithm.count("r"))

string1 = "Hello"
string2 = "World"
res = string1 + " " + string2
print(res)

# Find a sub-string
print(res.find("World"))

res = string1*3
print(res)