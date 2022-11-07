def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 1 << (number - 1)
#operadores de deslocamento bit a bit
# primeiro operando << segundo operando
# 1 << 5 --> (1-2-4-8-16) ele anda pra esquerda nasce um bit na direita com o valor dobrado do ultimo bit
#deslocar um bit para a esquerda dobra o seu valor

# a << n == a * 2^n

def total():
    return (1 << 64) - 1

n = square(int(input()))
print(n)

print(total())