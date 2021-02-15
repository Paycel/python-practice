import math


def foo(x, y, z):
    return (11 * y ** 3 - abs(x)) / (12 * y ** 5 + z ** 2 - 94) - (83 * y ** 4 + x ** 2 + 24) / (
            math.tan(y) + math.log(x) / math.log(math.e)) - (76 * z ** 7 - y ** 5 - 47)


print("{:.2e}".format(foo(53, -90, -76)))
print("{:.2e}".format(foo(70, 65, 27)))
