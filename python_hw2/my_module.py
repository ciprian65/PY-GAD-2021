def sum_of_numbers(n):
    if not n:
        return 0
    else:
        return n + sum_of_numbers(n - 1)


def sum_of_even_numbers(n):
    if not n:
        return 0
    elif not n % 2:
        return n + sum_of_even_numbers(n - 1)
    else:
        return sum_of_even_numbers(n - 1)


def sum_of_odd_numbers(n):
    if not n:
        return 0
    elif n % 2:
        return n + sum_of_odd_numbers(n - 1)
    else:
        return sum_of_odd_numbers(n - 1)
