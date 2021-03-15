def f23(table):
    new_t = []
    for row in table:
        if row not in new_t:
            new_t.append(row)
    for row in new_t:
        index = row[0].find("|")
        value = row[0][:index]
        row[0] = row[0][index + 1:]
        row.append(value)
        index2 = row[0].find(" ")
        row[0] = row[0][index2 + 1:]
        row[1] = row[1][row[1].find(" ") + 1:]
        row[2] = row[2][0].lower() + row[2][1:]
    new_t = sorted(new_t, key=lambda x: x[1])
    new_t = [list(i) for i in zip(*new_t)]
    return new_t


# print(f23([
#     ['Нет|(989) 726-46-38', 'Тихон Шеникянц'],
#     ['Нет|(524) 946-56-59', 'Илья Мебин'],
#     ['Нет|(524) 946-56-59', 'Илья Мебин'],
#     ['Нет|(524) 946-56-59', 'Илья Мебин'],
#     ['Нет|(523) 242-12-80', 'Никита Нишезин']
# ]))
