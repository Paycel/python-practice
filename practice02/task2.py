def f22(n):
    a = (n & 0x0000007f) << 3
    b = (n & 0x007fff80) << 9
    c = (n & 0x1f800000) >> 13
    d = (n & 0xe0000000) >> 29
    return b + c + a + d


# print(f22(0x7443d405))
# print(f22(0x891bcfe7))
