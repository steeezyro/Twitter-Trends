def is_prime(number):
    if (number == 1):
        return False
    for x in range(2,number):
        if number%x == 0:
            return False
    return True


def sum_prime_digits(n):
    """
    >>> sum_prime_digits(12345)
    10
    >>> sum_prime_digits(4681029)
    2
    """
    if n==0:
        return 0
    else:
        digits = n % 10
        if  is_prime(digit):
            return digit + sum_prime_digits(n // 10)
        return sum_prime_digits(n // 10)

