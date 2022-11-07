# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = [1,2,3,4,5]
BIG_STRAIGHT = [2,3,4,5,6]
CHOICE = "choice"

list_categories = [ONES,TWOS,THREES,FOURS,FIVES,SIXES]
def func(dice, category):
    """this functions is generic for somethings categories."""
    return category * dice.count(category) if dice.count(category) > 0 else 0
def score(dice, category):
    """Returns the score of the categories."""
    if category == YACHT:
        return YACHT if len(set(dice)) == 1 else 0
    if category in list_categories:
        return func(dice, category)
    if category == FULL_HOUSE:
        if len(set(dice)) != 2:
            return 0
        for n in set(dice):
            if dice.count(n) != 2 and dice.count(n) != 3:
                return 0
        return sum(dice)
    if category == FOUR_OF_A_KIND:
        if len(set(dice)) > 2:
            return 0
        for n in set(dice):
            if dice.count(n) == 4:
                return n * dice.count(n)
            if dice.count(n) == 5:
                return n * dice.count(n) - n
        return 0
    if category == LITTLE_STRAIGHT or category == BIG_STRAIGHT:
        return 30 if sorted(dice) == category else 0
    if category == CHOICE:
        return sum(dice)

x = score([1,1,5,4,2],LITTLE_STRAIGHT)
print(x)
x = score([1,3,5,4,2],BIG_STRAIGHT)
print(x)
x = score([6,5,4,3,1],FOURS)
print(x)


