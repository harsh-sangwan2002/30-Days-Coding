my_list = [1,2,3,4]
print(my_list)

list2 = ["A string",23,100,'o',True]
print(list2)

# Append in the list
my_list[0] = 10
print(my_list)
print(sum(my_list))
my_list.append(list2)
print(my_list)

# Concatenating list
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1+list2)
print(list1*3)

# Retrieving length of the list
print(len(my_list))

# Find element index
index = my_list.index(2)
print(index)

# Count the element
print(list1.count(2))

# Sorting the list
my_list = [3,1,4,5,2,6,9,8]
res = sorted(my_list)
print(res)

# Extending the list
my_list2 = [10,11,22,21]
my_list.extend(my_list2)
print(my_list)

# Insert in the list
my_list.insert(0,6)
print(my_list)