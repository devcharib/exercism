def exchange_money(budget, exchange_rate):
    """
    The function exchange_money return the value of the exchanged currency.
    """
    return budget / exchange_rate
def get_change(budget, exchanging_value):
    """
    The function get_change return the amount of money that is left from the budget.
    """
    return budget -  exchanging_value
def get_value_of_bills(denomination, number_of_bills):
    """
    The function get_value_of_bills return only the total value of the bills
    (excluding fractional amounts) the booth would give back.
    """
    return denomination * int(number_of_bills)
def get_number_of_bills(budget, denomination):
    """
    This function get_number_of_bills should return the number of new currency
    bills that you can receive within the given budget.
    """
    return int(budget // denomination)
def get_leftover_of_bills(budget, denomination):
    """
    This function get_leftover_of_bills return the leftover amount that cannot be
    exchanged from your budget given the denomination of bills
    """
    return budget % denomination
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    This function exchangeable return the maximum value of the new currency
    after calculating the exchange rate plus the spread.
    money_exchanged reiceived return of the function exchange_money()
    leftover_amount reiceived return of the funtion get_leftover_of_bills() with
    money exchanged
    """
    exchange_rate += exchange_rate * exchange_money(spread, 100)
    money_exchanged = exchange_money(budget, exchange_rate)
    leftover_amount = get_leftover_of_bills(money_exchanged, denomination)
    return get_change(money_exchanged, leftover_amount)
