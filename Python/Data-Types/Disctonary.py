marvel_dict = {
    'Name':'Thor',
    'Place':'Asgard',
    'Powers':['Super Strength','Flight','Weather Control']
}

print(marvel_dict['Powers'])
print(marvel_dict.keys())
print(marvel_dict.values())

customer = {
    'id':1234,
    'name':'John Smith',
    'email':'john@example.com',
}

customer['email'] = 'john2@example.com'
customer['phone'] = 9998887776
print(customer)

print(list(marvel_dict.keys()))