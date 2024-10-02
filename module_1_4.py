my_string = input("Напиши мне что-то: ")
print('В твоей фразе: ' , len(my_string), 'символа(ов)')

print('Вот так это в верхнем регистре: ' , my_string.upper())
print('Так в нижнем:' , my_string.lower())
print('Без пробелов:' , my_string.replace(' ', ''))
print('Первый символ:' , my_string[0])
print('Последний символ: ' , my_string[-1])