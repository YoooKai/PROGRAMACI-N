# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    money_back = {}
    if to_give_back == 0:
        money_back = {}
    else:
        available_currencies.sort(reverse=True)
        for currency in available_currencies:
            num_of_currency = int(to_give_back // currency)
            if num_of_currency > 0:
                money_back[currency] = num_of_currency
            to_give_back %= currency
        if to_give_back != 0:
            money_back = None

    return money_back


if __name__ == '__main__':
    run(20, [5, 2, 1])
