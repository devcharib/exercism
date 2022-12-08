# OUTERSIDE    = 0
# OUTERCIRCLE  = 1
# MIDDLECIRCLE = 5
# INNERCIRCLE  = 10

# POSITIVE = lambda a: a*-1 if a < 0 else a
# FATOR = lambda x : (x - x*0.3)* 2 + 0.1

# def score(x, y):
#     x = POSITIVE(x)
#     y = POSITIVE(y)
#     maior = max(x, y)

#     if maior < 1.1:
#         if maior < 0.8 or x+y < 1.1: 
#             return INNERCIRCLE
    
#     if maior < 5.1:
#         if maior < 3.6 or x+y < 5.1:
#             return MIDDLECIRCLE
      
#     if maior < 10.1:
#         if maior < 7.1 or x+y < 10.1:
#             return OUTERCIRCLE
   
#     return OUTERSIDE
#     """
# If the dart lands outside the target, player earns no points 0 points.

# If the dart lands in the outer circle of the target, player earns 1 point.

# If the dart lands in the middle circle of the target, player earns 5 points.

# If the dart lands in the inner circle of the target, player earns 10 points.
#     """
# print(score(0,-1))

# import math
# """ Amounts points."""
# OUTERSIDE    = 0
# OUTERCIRCLE  = 1
# MIDDLECIRCLE = 5
# INNERCIRCLE  = 10


# def score(x, y): # Mentored by IsaacG
#     x = abs(x)
#     y = abs(y)
#     hypotenuse = math.sqrt(x**2 + y**2) # Pythagorean theorem 
#     if hypotenuse <= 1:
#         return INNERCIRCLE
#     if hypotenuse <= 5:
#         return MIDDLECIRCLE
#     if hypotenuse <= 10:
#         return OUTERCIRCLE
#     return OUTERSIDE

# import math

# OUTERSIDE    = 0
# OUTERCIRCLE  = 1
# MIDDLECIRCLE = 5
# INNERCIRCLE  = 10
# POINTS = {1:INNERCIRCLE, 5:MIDDLECIRCLE, 10:OUTERCIRCLE}


# def score(x, y): # Mentored by IsaacG

#     hypotenuse = math.sqrt(x**2 + y**2) # Pythagorean theorem 
    
#     for key, value in POINTS.items():
#         if hypotenuse <= key:
#             return value
#     return OUTERSIDE

# print(score(0.1,-0.1))


# import math

# OUTERSIDE = 0
# OUTERCIRCLE = 1
# MIDDLECIRCLE = 5
# INNERCIRCLE = 10
# POINTS = {1: INNERCIRCLE, 5: MIDDLECIRCLE, 10: OUTERCIRCLE}


# def score(x, y): #Mentored by IsaacG
#     hypotenuse = math.sqrt(x**2 + y**2) #Pythagorean theorem 
#     for distance, point in POINTS.items():
#         if hypotenuse <= distance:
#             return point
#     return OUTERSIDE

import math

OUTERSIDE = 0
OUTERCIRCLE = 1
MIDDLECIRCLE = 5
INNERCIRCLE = 10
POINTS = {1: INNERCIRCLE, 5: MIDDLECIRCLE, 10: OUTERCIRCLE}


def score(x: int, y: int) -> int:  # Mentored by IsaacG
    """Return the points """
    hypotenuse = math.sqrt(x**2 + y**2)  # Pythagorean theorem
    result = next((point for distance, point in POINTS.items()
                   if hypotenuse <= distance), OUTERSIDE)
    return result


print(score(-9, 9))

