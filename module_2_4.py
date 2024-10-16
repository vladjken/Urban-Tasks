numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # дан список
primes = [] # простые чилса сюда
not_primes = []

for num in numbers :
    if num < 2:
        continue
    for del_ in range(2, int(num**0.5) + 1 ):
        if num % del_ == 0: # провека на простое число
            not_primes.append(num)
            break
    else:
        primes.append(num)

print('Primes:', primes) # вывод списка
print('Not Primes:', not_primes)


