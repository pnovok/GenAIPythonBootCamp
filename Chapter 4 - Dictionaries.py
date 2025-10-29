# # DICTIONARY Basics
# model_config = {'model_name': 'GPT-4', 'layers':48}
# print(type(model_config))
#
# #Keys should be immutable, not lists, but we can use tuples
#
# test_dict = dict()
# test_dict['key1'] = 'value1'
# test_dict['key2'] = 'value2'
#
# print(test_dict)
# print("The first value is: "+test_dict['key1'])
# print("The second value is: "+test_dict['key2'])
#
#
# #Removing keys from the dict
# data = {'name':'Alice','age':30,'city':'New York'}
# age = data.pop('age')
# print(age,data)
# print(data)
#
# # Let's return the last item as a tuple
# data = {'name':'Alice','age':30,'city':'New York'}
# last_item = data.popitem()
# print(last_item,data)
#
# # Let's delete the key
# data = {'name':'Alice','age':30,'city':'New York'}
# del data['city']
# print(data)
#
# # Let's compare keys between 2 dicts
# config_a = {'model_name': 'GPT-4', 'layers':48, 'param':34}
# config_b = {'model_name': 'GPT-4', 'layers':45}
#
# common_keys = config_a.keys() & config_b.keys()
# print(common_keys)
#
# # Iterating over key/values in dicts
# for key in config_a.keys():
#     print(f"The key is {key}")
#
# for value in config_b.values():
#     print(f"The value is {value}")
#
# for key,value in config_a.items():
#     print(f"The key is {key} for the value is {value}")

    # DICTIONARY COMPREHENSIONS

# Original dictionary
hyperparams = {'layers': 3, 'units': 256, 'dropout': 0.2}

# Create a new dictionary where all values are doubled
adjusted_params = {k: v * 2 for k, v in hyperparams.items()}
print(adjusted_params)
# {'layers': 6, 'units': 512, 'dropout': 0.4}

# Create a set of keys (in uppercase) where values are greater than 0.2
updated_params = {k.upper() for k, v in hyperparams.items() if v > 0.2}
print(updated_params)
# {'LAYERS', 'UNITS'}


for i in range(3):
    if i == 1:
        pass
    print(i)

for letter in 'pythoooon!!!':
   print(letter, end='')
   if letter == 'o':
       continue









