calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    string = (len(string), string.upper(), string.lower())
    count_calls()
    return string

def is_contains(str, list):
    count_calls()
    for i in list:
        list = i.upper()
    if str.upper() in list:
        return True
    else: return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)