marvel_dict = {
    'Name':'Thor',
    'Place':'Asgard',
    'Powers':['Super Strength','Flight','Weather Control']
}

print(marvel_dict['Powers'])
print(marvel_dict.keys())
print(marvel_dict.values())
print(marvel_dict.items())

customer = {
    'id':1234,
    'name':'John Smith',
    'email':'john@example.com',
}

# Update the dictionary
customer['email'] = 'john2@example.com'
customer['phone'] = 9998887776
print(customer)

print(list(marvel_dict.keys()))

new_dict = customer.copy()
print(new_dict)
customer.clear()
print(customer)

# Get in a dictionary
print(marvel_dict.get("Name"))