# ********************
# CUALIFICANDO NÚMEROS
# ********************


def run(number: int) -> str:
    """
    Given a positive number, separate the thousands digits with commas.

    :param number: positive integer received by the function.
    :type number: integer
    :param three_digits: stores 3 numbers and resets on each iteration of the loop. 
    At the end of the loop, it stores the remaining numbers.
    :type three_digits: string
    :param group_of_digits: list to which the 3 numbers from the variable three_digits are added in each
    iteration, and at the end the remaining numbers are added to it.
    :type group_of_digits: list
    :param qnumber: joining of the group_of_digits list using a join with a comma.
    :type qnumber: string

    :return rev_qnumber: the reversed string qnumber.
    :type: string
"""
    three_digits = ''
    rev_qnumber = ''
    group_of_digits = []

    for digit in str(number)[::-1]:
        three_digits += digit
        if len(three_digits) == 3:
            group_of_digits.append(three_digits)
            three_digits = ''
    if three_digits:
        group_of_digits.append(three_digits)
    qnumber = ','.join(group_of_digits)
    rev_qnumber = qnumber[::-1]

    return rev_qnumber


if __name__ == '__main__':
    run(1)