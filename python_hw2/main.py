import my_module


def my_function(*args, **kwargs):
    n = 0
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            n += i
    return n


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param1=2))
print('\n')


print(my_module.sum_of_numbers(4))
print(my_module.sum_of_even_numbers(4))
print(my_module.sum_of_odd_numbers(4))
print('\n')


def read_int():
    i = input('Enter the input: ')
    try:
        while int(i):
            print(f'{i} is integer')
            i = input('Enter the input: ')
    except ValueError:
        print(f'{i} is not integer')
        return 0


read_int()


