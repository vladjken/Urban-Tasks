immutable_var = 1, 3.14, 'Hi', True, [4, 5]
print(immutable_var)

# immutable_var [0] = 5
# попытаясь заменить переменную в кортеже получаем ошибку так как кортеж неизменяемой коллекцией
# но кортеж может нести в себе изменяемые элементы (список например)
immutable_var [4] [1] = 10
print(immutable_var)


mutable_list = [1, 3,14, 'Bye', False]
print(mutable_list)
mutable_list [0] = 5
print(mutable_list)