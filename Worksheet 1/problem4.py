import math

def is_prime(n):
    """
    Returns True if n is prime, False otherwise.
    """
    # Special cases for small numbers
    if n == -1 or n == 0 or n == 1:
        return False
    if n == -2 or n == 2:
        return True
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    # Check if n is a multiple of a number, besides 1 and itself
    aux = 3
    while aux <= math.ceil(math.sqrt(abs(n))):
        if n % aux == 0:
            return False
        aux += 2
    return True


assert is_prime(0) == False
assert is_prime(1) == False
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(5) == True
assert is_prime(6) == False
assert is_prime(7) == True
assert is_prime(8) == False
assert is_prime(9) == False
assert is_prime(9941) == True
assert is_prime(9943) == False
