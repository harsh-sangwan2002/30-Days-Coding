def fun(firstName,lastName):
    print("Hello ",firstName," ",lastName)
    
fun("Harsh","Sangwan")

# Arbitraty arguments
def fun(*name):
    print(name)

fun("Harsh","Sangwan")

# Key:value arguments
def fun(child3,child2,child1):
    print(child1,child2,child3)

fun(child1="John",child2="Mark",child3="Big")

# Arbitrary key:value arguments
def fun(**children):
    print(children)

fun(child1="John",child2="Mark",child3="Big")

# Passing list as an argument
def fun(list):
    print(list)
    
list = [1,2,3,4,5]
fun(list)

# Returning from the function
def add(a,b):
    return a+b

res = add(10,20)
print(res)

# Using pass keyword
def fun():
    pass