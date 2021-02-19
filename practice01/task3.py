import math


def f13(n, m):
    sum1 = 0
    sum2 = 0
    for i in range(1, n + 1):
        sum1 += 11 * i ** 8 - abs(i)
        sum2 += 39 * i ** 2 + math.sin(i) - 98
    return 65 * sum1 * m - sum2


print("{:.2e}".format(f13(76, 60)))
print("{:.2e}".format(f13(66, 80)))

