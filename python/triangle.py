"""Return if sides form a triangle inequality"""
def isTriangle(sides):
    for n in sides:
        if n <= 0:
            return False
    a,b,c = sides
    return (a +b) >= c and (b + c) >= a and (a + c) >= b

"""Return if sides form a triangle equialateral"""
def equilateral(sides):
    if not isTriangle(sides):
        return False

    a,b,c = sides
    return a is b is c

"""Return is sides form a triangle isosceles"""
def isosceles(sides):
    if not isTriangle(sides):
        return False
    a,b,c = sides
    if a != b:
        if b != c:
            if a == c:
                return True
        else:
            return True
    elif a != c:
        return True

    return equilateral(sides)

"""Return if sides form a triangle scalene"""
def scalene(sides):
    if not isTriangle(sides):
        return False

    return not isosceles(sides)
