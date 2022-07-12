# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def GCD(a: int, b: int) -> int:
    """
    返回正整数a,b的最大公约数
    """
    if b == 0:
        return a
    a %= b
    return GCD(b, a)


print(GCD(4, 8))
