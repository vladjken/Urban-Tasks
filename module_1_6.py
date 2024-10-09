my_dict = { 'One': 101010101, 'Two': 202020202, 'Three': 303030303}
print(my_dict)
print(my_dict['One'])
print(my_dict.get('Four', 'Нет такого'))
my_dict.update({'Four': 40404040404, 'Five': 50505050505})
a = my_dict.pop('Two')
print(a)
print(my_dict)


my_set = { 1, 2, 2, 3, 3, 3, 'Four', 'Four', 'Four', 'Four', True, False, False}
print(my_set)
my_set.add(9)
my_set.add(7)
my_set.discard('Four')

print(my_set)