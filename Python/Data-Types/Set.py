empty_set = set()
print(type(empty_set))

non_empty_set = {1,6,4,'abc'}
print(non_empty_set)

my_object = {}
print(type(my_object))

set_a = {1,2,3}
set_b = {2,3,4}

# Union operator
print(set_a|set_b)

# Intersection operator
print(set_a&set_b)

# Difference operator
print(set_a-set_b)