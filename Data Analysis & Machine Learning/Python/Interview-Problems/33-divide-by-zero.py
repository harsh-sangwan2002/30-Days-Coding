try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    res = num1/num2
    print(res)
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
else:
    print("Result: ",res)