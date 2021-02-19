def f14(n):
    return 3 if n == 0 else (4 if n == 1 else f14(n - 1) ** 2 / 35 - abs(f14(n - 1)))

print("{:.2e}".format(f14(10)))
print("{:.2e}".format(f14(3)))
