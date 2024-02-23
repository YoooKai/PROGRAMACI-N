# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    money_back = {}
    if to_give_back == 0:
        money_back = {}
    else:
        available_currencies = sorted(available_currencies.items(), reverse=True)
        for currency, max_units in available_currencies:
            num_of_currency = min(int(to_give_back // currency), max_units)
            if num_of_currency > 0:
                money_back[currency] = num_of_currency
                to_give_back -= num_of_currency * currency

    if to_give_back > 0:
        money_back = None

    return money_back


if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})
