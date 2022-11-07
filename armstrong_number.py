
def is_armstrong_number(number):
    """
    this function is_armstrong_number returns True or False for the number whether is an
    Armstrong number
    """
    digits = list(str(number))
    number_of_digits = len(digits)
    sum = 0
    for dig in digits:
        sum += int(dig)**number_of_digits
    return True if sum == int(number) else False

x = is_armstrong_number(input())
print(x)

# depois do mentor
def is_armstrong_number(number):
    """
    this function is_armstrong_number returns True or False for the number whether is an
    Armstrong number
    """
    digits = list(str(number))
    number_of_digits = len(digits)
    items = []
    for dig in digits:
        items.append(int(dig)**number_of_digits)
    return sum(items) == number #return without if | without int()

x = is_armstrong_number(int(input()))
print(x)