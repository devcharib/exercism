"""Return o number of steps of the Collatz Conjecture"""
def collatz(n):
    if n < 1:
        raise ValueError("Only positive integers are allowed")
    print(n)
    step = 0
    while n > 1:
        n = n/2 if n % 2 == 0 else 3*n+1
        step += 1
    print(step)
x = collatz(int(input()))
