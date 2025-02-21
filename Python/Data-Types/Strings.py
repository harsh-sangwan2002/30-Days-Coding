# Strings are immutable sequences of characters. They are enclosed in single or double quotes.
my_first_string = "Hello World!"
print(my_first_string)

message = "Hey! how are you doing?"
print(message[3])
message = message.replace("Hey","Hello")
print(message)

algorithm = "Neural Networks"
print(algorithm.count("r"))

string1 = "Hello"
string2 = "World"
res = string1 + " " + string2
print(res)

res = string1*3
print(res)