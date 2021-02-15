import math


def foo(x):
    if x < 123:
        return 64 * x ** 3 + 30 * x ** 5
    elif x < 196:
        return 30 * x - math.log(x) / math.log(math.e)
    elif x < 228:
        return x ** 2 - math.tan(x)
    elif x < 296:
        return x ** 8 + 28 * x ** 7
    else:
        return x + 65 * x ** 7


print("{:.2e}".format(foo(94)))
print("{:.2e}".format(foo(172)))

