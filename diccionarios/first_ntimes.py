# ********************************
# PRIMER ELEMENTO REPETIDO N-VECES
# ********************************


def run(numbers: list, nrep: int) -> int:
    frequency_dict = {}
    for num in numbers:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    target_num = -1

    for num, frequency in frequency_dict.items():
        if frequency == nrep:
            target_num = num
            break
    # otra manera #################################################

    # frequency_dict = {}
    #
    # target_num = -1
    #
    # for num in numbers:
    #    if num in frequency_dict:
    #        frequency_dict[num] += 1
    #    else:
    #        frequency_dict[num] = 1
    #    if frequency_dict[num] == nrep:
    #        target_num = num
    #        break

    return target_num


if __name__ == '__main__':
    run([2, 3, 5, 3, 2, 1, 8, 2], 3)
