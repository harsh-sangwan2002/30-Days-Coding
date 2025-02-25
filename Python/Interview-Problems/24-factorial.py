num = int(input("Enter a number: "))

def find_factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*find_factorial(num-1)

print(find_factorial(num))