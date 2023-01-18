def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1 = a % 10
    x2 = a // 10 % 10
    
    s = x1 + x2

    return s % 2 == 1


print(main(36))