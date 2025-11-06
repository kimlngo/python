#Dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict['key1'])

price_lookup = {'apple': 2.99, 'orange': 1.99, 'milk': 3.7}
print(f'price of apple: {price_lookup['apple']}')

#multiple data type
my_dict = {'k1': 123, 'k2': [1,2,3], 'k3': {'innerkey': 100}}
print(f"my_dict['k2'] = {my_dict['k2']}")
print(f"inner value: {my_dict['k3']['innerkey']}")

#add a new key-value pair
my_dict['k4'] = 'nice!'
print(my_dict)

#modify existing key
my_dict['k1'] = 456
print(my_dict)

#get keys
#dict_keys(['k1', 'k2', 'k3'])
my_dict = {'k1': 123, 'k2': [1,2,3], 'k3': {'innerkey': 100}}
print(f'keys: {my_dict.keys()}')
#dict_values([123, [1, 2, 3], {'innerkey': 100}])
print(f'values: {my_dict.values()}')

#items, print out tupples
#dict_items([('k1', 123), ('k2', [1, 2, 3]), ('k3', {'innerkey': 100})])
print(f'all tupples: {my_dict.items()}')