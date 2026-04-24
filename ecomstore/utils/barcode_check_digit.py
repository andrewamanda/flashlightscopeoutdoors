import functools

def add_check_digit(upc_str):
    """
    Returns a 12 digit upc-a string from an 11-digit upc-a string by adding
    a check digit

    >>> add_check_digit('02345600007')
    '023456000073'
    >>> add_check_digit('21234567899')
    '212345678992'
    >>> add_check_digit('04210000526')
    '042100005264'
    """

    upc_str = str(upc_str)
    if len(upc_str) != 11:
        raise Exception("Invalid length")

    odd_sum = 0
    even_sum = 0
    for i, char in enumerate(upc_str):
        j = i+1
        if j % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)

    total_sum = (odd_sum * 3) + even_sum
    mod = total_sum % 10
    check_digit = 10 - mod
    if check_digit == 10:
        check_digit = 0
    return upc_str + str(check_digit)

def add_check_digit_ean(upc_str):
    """
    Returns a 12 digit upc-a string from an 11-digit upc-a string by adding
    a check digit

    >>> add_check_digit('02345600007')
    '023456000073'
    >>> add_check_digit('21234567899')
    '212345678992'
    >>> add_check_digit('04210000526')
    '042100005264'
    """

    upc_str = str(upc_str)
    if len(upc_str) != 12:
        raise Exception("Invalid length")

    sum_ = lambda x, y: int(x) + int(y)
    evensum = functools.reduce(sum_, upc_str[::2])
    oddsum = functools.reduce(sum_, upc_str[1::2])
    checkdigit =  (10 - ((evensum + oddsum * 3) % 10)) % 10
    return upc_str + str(checkdigit)

def generate_upc():
    characters = '0123456789'
    upc_length = 11
    upc_seed = ''
    import random
    for y in range(upc_length):
        upc_seed += characters[random.randint(0, len(characters)-1)]
    upc = add_check_digit(upc_seed)
    return upc
