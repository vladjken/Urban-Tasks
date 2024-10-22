def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(3, 'число')
print_params(False, 5, 'слово')
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [1.3, False, 'Hello']
values_dict = {'a': 56, 'b':False, 'c':'Bye'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [78.1, 'Cool' ]
print_params(*values_list_2, 42)