SIDE = lambda x, y: len(set(x)) == y


"""Return if sides form a triangle inequality"""
def isTriangle(sides):
    for n in sides:
        if n <= 0:
            return False
    a, b, c = sides
    return (a+b) >= c and (b+c) >= a and (a+c) >= b

"""Return if sides form a triangle equialateral"""
def equilateral(sides):
    if not isTriangle(sides):
        return False
    return SIDE(sides, 1)

"""Return is sides form a triangle isosceles"""
def isosceles(sides):
    if not isTriangle(sides):
        return False
    return SIDE(sides, 2) or SIDE(sides, 1)

"""Return if sides form a triangle scalene"""
def scalene(sides):
    if not isTriangle(sides):
        return False
    return SIDE(sides, 3)


x = equilateral([5,5,5])
print(x)
x = isosceles([5,5,5])
print(x)
x = scalene([5,5,5])
print(x)