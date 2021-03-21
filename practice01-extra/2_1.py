def naive_mul(x, y):
    r = 0
    for i in range(y):
        r += x
    return r


def test_func():
    for x in range(101):
        for y in range(101):
            assert naive_mul(x, y) == x * y
    print("All tests passed")


test_func()
