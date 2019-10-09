import math


def get_whole_part(num):
    try:
        ret = int(num - (num % 1))
    except Exception as e:
        raise Exception(f'Invalid Number, {num}, passed causing Exception {e}')
    else:
        return ret


def get_fractional_part(num):
    try:
        if '.' in str(num):
            sting_num = f'.{str(num).split(".")[1]}'
            ret = float(sting_num)
        else:
            ret = 0
    except Exception as e:
        raise Exception(f'Invalid Number, {num}, passed causing Exception {e}')
    else:
        return ret


def is_prime_number(num):
    if num < 2:
        return False
    else:
        for x in range(2, num):
            if num % x == 0:
                return False

    return True


def get_prime_numbers(start, num):
    if not isinstance(start, int) or not isinstance(num, int):
        raise Exception(f'Both {start} and {num} must be whole numbers')

    ret = []
    num_to_test = start

    while len(ret) < num:
        if is_prime_number(num_to_test):
            ret.append(num_to_test)

        num_to_test += 1

    return ret
