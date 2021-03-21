def mul_12(x):
    twice = x + x
    fourth = twice + twice
    eighth = fourth + fourth
    return eighth + fourth


def mul_16(x):
    twice = x + x
    fourth = twice + twice
    eighth = fourth + fourth
    return eighth + eighth


def mul_15(x):
    twice = x + x
    fourth = twice + twice
    eighth = fourth + fourth
    return eighth - (x - eighth)


def mul_29(x):
    twice = x + x
    fourth = twice + twice
    eighth = fourth + fourth
    sixteenth = eighth + eighth
    return sixteenth + sixteenth - (twice + x)
