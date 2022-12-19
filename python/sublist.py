# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0


def sublist(list_one, list_two):
    """Return if the lists are EQUAL, SUBLIST, SUPERLIST and UNEQUAL."""
    one = (str(list_one).strip('[]') + ',')
    two = (str(list_two).strip('[]') + ',')

    if one == two:
        return 3
    if one in two:
        return 1
    if two in one:
        return 2
    return 0


print(sublist([1, 2, 3], [1, 2, 3, 4, 5]))
