def main(a):
    """
    Given a two-digit integer a, \
     check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1 = a % 10 
    x2 = a // 10 % 10

    return x1 % 2 == 0 + x2 % 2 == 0

print(main(45))