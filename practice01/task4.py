def foo(n):
    return 3 if n == 0 else (4 if n == 1 else foo(n - 1) ** 2 / 35 - abs(foo(n - 1)))


print("{:.2e}".format(foo(10)))
print("{:.2e}".format(foo(3)))