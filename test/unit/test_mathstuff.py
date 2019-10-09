from pythonstuff import mathstuff
import pytest


def test_get_whole_part_decimal():
    expected = 5
    actual = mathstuff.get_whole_part(5.7)
    assert actual == expected


def test_get_whole_part_int():
    expected = 5
    actual = mathstuff.get_whole_part(5)
    assert actual == expected


def test_get_whole_part_exception():
    num = '5.7'
    expected = f'Invalid Number, {num}, passed causing Exception'

    with pytest.raises(Exception) as e:
        mathstuff.get_whole_part(num)

    assert expected in str(e.value)


def test_get_fractional_part_decimal():
    expected = .78463
    actual = mathstuff.get_fractional_part(5.78463)
    assert actual == expected


def test_get_fractional_part_int():
    expected = 0
    actual = mathstuff.get_fractional_part(5)
    assert actual == expected


def test_get_fractional_part_exception():
    num = '5.'
    expected = f'Invalid Number, {num}, passed causing Exception'

    with pytest.raises(Exception) as e:
        mathstuff.get_fractional_part(num)

    assert expected in str(e.value)


def test_is_prime_number_false():
    actual = mathstuff.is_prime_number(4)
    assert not actual


def test_is_prime_number_true():
    actual = mathstuff.is_prime_number(17)
    assert actual


def test_is_prime_number_one():
    actual = mathstuff.is_prime_number(1)
    assert not actual


def test_is_prime_number_negative():
    actual = mathstuff.is_prime_number(-2)
    assert not actual


def test_get_prime_numbers():
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    actual = mathstuff.get_prime_numbers(2, 8)

    assert len(actual) == len(expected)

    for num in expected:
        assert num in actual


def test_get_prime_numbers_exception():
    bad_num = 8.8
    expected = f'Both 2 and {8.8} must be whole numbers'
    with pytest.raises(Exception) as e:
        mathstuff.get_prime_numbers(2, bad_num)

    assert expected in str(e.value)
