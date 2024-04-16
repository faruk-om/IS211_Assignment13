def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_0, fib_1 = 0, 1
        for i in range(2, n):
            fib_0, fib_1 = fib_1, fib_0 + fib_1
        return fib_1


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    if not s1:
        return -ord(s2[0])
    if not s2:
        return ord(s1[0])
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    return compareTo(s1[1:], s2[1:])


