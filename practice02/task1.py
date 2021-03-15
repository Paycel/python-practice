d = {(1, 1994):
         {(2, 2019): 5,
          (2, 2015):
              {(0, 1990): 4,
               (0, 2015): 3,
               (0, 1979):
                   {(3, 1991): 0, (3, 1984): 1, (3, 1979): 2}}},
     (1, 2011): {(2, 2015):
                     {(4, 2011): 6, (4, 1971): 7},
                 (2, 2019):
                     {(3, 1991):
                          {(4, 2011): 8, (4, 1971): 9},
                      (3, 1984): 10, (3, 1979): 11},
                 },
     (1, 1965): 12}


def foo(way, d):
    for pair in d:
        if way[pair[0]] == pair[1] and isinstance(d[pair], dict):
            return foo(way, d[pair])
        elif way[pair[0]] == pair[1] and isinstance(d[pair], int):
            return d[pair]


def f21(lst):
    return foo(lst, d)


# print(f21([2015, 1994, 2019, 1991, 2011]))
# print(f21([2015, 2011, 2019, 1984, 2011]))
