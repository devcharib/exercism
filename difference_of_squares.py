def square_of_sum(number):
    #(1 + 2 + ... + 10)² = 55² = 3025.
    soma1 = sum(list(range(1,number+1)))**2
    return soma1
def sum_of_squares(number):
    #1² + 2² + ... + 10² = 385.
    soma2 = 0
    for n in list(range(1,number+1)):
        soma2 += n**2
    return soma2
def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
#x = square_of_sum(int(input()))
y = difference_of_squares(int(input()))
print(y)
# 2
def square_of_sum(number):
    #(1 + 2 + ... + 10)² = 55² = 3025.
    soma1 = sum(range(1,number+1))**2 #mentor BNAndras
    return soma1
def sum_of_squares(number):
    #1² + 2² + ... + 10² = 385.
    soma2 = 0
    for n in range(1,number+1): #mentor BNAndras
        soma2 += n**2
    return soma2

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
#x = square_of_sum(int(input()))
y = difference_of_squares(int(input()))
print(y)
#3
def square_of_sum(number):
    #(1 + 2 + ... + 10)² = 55² = 3025.
    soma1 = sum(range(1,number+1))**2 #mentor BNAndras
    return soma1

def sum_of_squares(number):
    #1² + 2² + ... + 10² = 385.
    generator = sum(num ** 2 for num in range(1, number+1))
    return generator

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

y = difference_of_squares(int(input()))
print(y)