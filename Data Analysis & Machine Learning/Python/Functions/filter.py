# filter function
# filter(function,iterable)

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda num : num%2==0,numbers))
print(even_numbers)

odd_numbers = list(filter(lambda num: num%2!=0, numbers))
print(odd_numbers)