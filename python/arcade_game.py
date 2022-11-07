# def funcao(a,b):# true false  true
#     return True if a == True and b == False else False

# print(funcao(False,True))
# print(funcao(True,False))
# print(funcao(True,True))
# print(funcao(False,True))
# def lose(a,b):
#     return True if a==False and b==True else False

# def funcao(x,y,z):# false true false = true
#     return True if x == True and lose(y,z) == False else False

# print(funcao(True,True,True))
# print(funcao(True,False,True))
# print(funcao(False,True,False))

# def eat(a,b):
#     return a and b
# print(eat(True,True))
# print(eat(True,False))

# def score(a,b):
#     return a or b
# print(score(True,False))
# print(score(True,True))
# print(score(False,False))

def lose(a,b):
    # if bool(a and b) is True:
    #     return False
    # else:
    #     return bool(not a and b)
    return bool(not a and b) if bool(a and b) is True else bool(not a and b)
def win(x,y,z): #false true false = false
    return x and not lose(y,z)

print(win(False,True,False))
print(win(False,True,True))
print(win(False,False,True))
print(win(False,False,False))
print(win(True,False,False))
print(win(True,True,True))


# return True if power_pellet_active is False and touching_ghost is True else False

def eat_ghost(power_pellet_active, touching_ghost):
    """
    Function eat_ghost() returns a Boolean True if Pac-Man has a power
    active and if it is touching a ghost
    """
    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    """
    Function score() returns a Boolean True if Pac-Man is touching a power and
    if touching a dot
    """
    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):
    """
    Function lose() returns a Boolean True if Pac-Man lose
    """
    return bool(not power_pellet_active and touching_ghost) if bool(power_pellet_active and touching_ghost) is True else bool(not power_pellet_active and touching_ghost)

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    Function win() returns a Boolean True if Pac-Man wins
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)