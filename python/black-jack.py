""" Black Jack Rules """
def value_of_card(card):
    return int(card) if card.isnumeric() else (10 if card != "A" else 1)

def higher_card(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    return card_one if value_of_card(card_one) > value_of_card(card_two) else card_two

def value_of_ace(card_one, card_two):
    return 11 if sum([value_of_card(card_one), value_of_card(card_two)]) <= 10 and "A" not in [card_one, card_two] else 1

def is_blackjack(card_one, card_two):
    if "A" in (card_one, card_two):
        return 10 in (value_of_card(card_one), value_of_card(card_two))
    return False

def can_split_pairs(card_one, card_two):
    return isinstance(higher_card(card_one, card_two), tuple)

def can_double_down(card_one, card_two):
    return sum([value_of_card(card_one), value_of_card(card_two)]) in [9, 10, 11]

    


x = value_of_ace('2','A')
print(x)