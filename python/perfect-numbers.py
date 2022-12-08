# def classify(number):
#     if number < 1:
#         raise ValueError("Classification is only possible for positive integers.")
#     total = 0
#     fator = 1
#     while fator < number:
#         if number % fator == 0:
#             total += fator
#         fator += 1
#     if total == number:
#         return "Perfect"
#     if total > number:
#         return "Abundant"
#     if total < number:
#         return "Deficient"

# x = classify(28)
# print(x)

#---------------- more velocity

import math


def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    fator = set()
    for item in range(1, int(math.sqrt(number)) + 1): #Mentored by nikoferraz
        if number % item != 0:
            continue
        fator.add(item)
        fator.add(number // item)
    fator.remove(number)
    total = sum(fator)
    if total == number:
        return "perfect"
    if total > number:
        return "abundant"
    if total < number:
        return "deficient"
