def getNthFib1(n):
    # O(n) time, O(n) space
    if n == 1:
        return 0
    if n == 2:
        return 1
    f = [None] * n
    f[0] = 0
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
        print(f[i])
    return f[n - 1]


def getNthFib2(n):
    # O(2^n) time, O(1) space
    if n == 1:
        return 0
    if n == 2:
        return 1
    return getNthFib2(n - 1) + getNthFib2(n - 2)


def getNthFib3(n):
    #  O(n) time, O(1) space
    if n == 1:
        return 0
    if n == 2:
        return 1
    f0 = 0
    f1 = 1
    for i in range(2, n):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    return f2
