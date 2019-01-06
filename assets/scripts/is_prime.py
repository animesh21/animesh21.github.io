def is_prime(n):
    """
    :param n: int, greater than or equal to 1
    :return: bool, True if n is prime else False
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    """
    Tests the function is_prime for some set of inputs -> {1, 2, 3, 4, 5, 100, 101, 557}
    """
    prime_nums = {2, 3, 5, 101, 557}
    non_prime_nums = {1, 4, 100, 553}

    for n in prime_nums:
        result = is_prime(n)
        assert result is True, "{} is a prime number while `is_prime` returned `False`".format(n)

    for n in non_prime_nums:
        result = is_prime(n)
        assert result is False, "{} is not a prime number while `is_prime` returned `True`".format(n)
    print("Tested `is_prime` on input set -> {}".format(prime_nums.union(non_prime_nums)))
    print("Ok")


if __name__ == '__main__':
    test_is_prime()
