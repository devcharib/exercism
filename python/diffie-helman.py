
import random


def private_key(p):
    return random.randint(1,p-1)
    #random a > 1 and a < p


def public_key(p, g, private):
    return g**private % p
    #A = g^a mod p
    #B = g^b mod p

def secret(p, public, private):
    return public**private % p
    #s = B^a mod p
    #s = A^a mod p

x = private_key(5)
print(x)
y = public_key(23,5,15)
print(y)
z = secret(23,19,6)
print(z)
#random([5,7,11,13,17,19,23,29,31,37])