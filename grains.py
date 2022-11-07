def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")


    return 1 * 2**(number - 1)
        
def total():

    return (1 * 2**64) - 1

n = square(int(input()))
print(n)
print(total())