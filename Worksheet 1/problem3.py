def sum_to(n):
    """
    Sums all integers up to and including n.
    """
    sum_int = 0
    for i in range(1, n+1):
        sum_int += i
    return sum_int


def sum_to_gauss(n):
    """
    Returns the sum of all integers up to
    and including n, by using Gauss's formula.
    """
    return n*(n+1)//2


print(sum_to(10))
print(sum_to_gauss(10))
