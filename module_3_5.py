def get_multiplied_digits(numder):
    str_number = str(numder)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first*get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)