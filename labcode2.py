print('Флаг Швейцарии:')
for i in range(3):
    print("\033[31m■ " * 26)
for i in range(4):
    print("\033[31m■ " * 11 + "\033[37m■ " * 4 + "\033[31m■ " * 11)
for i in range(4):
    print("\033[31m■ " * 7 + "\033[37m■ " * 12 + "\033[31m■ " * 7)
for i in range(4):
    print("\033[31m■ " * 11 + "\033[37m■ " * 4 + "\033[31m■ " * 11)
for i in range(3):
    print("\033[31m■ " * 26)
print()

print('\033[37mУзор:')
print('◯' * 50)
print()

print('График функции y=x/3:')
print('↑ y')
for y in range(10, 0, -1):
    x = y * 3 * 2 - 1
    print('|' + ' ' * x + '*')
print("* " + "- " * 10 * 3 + '→')
print('0' + '  ' * 10 * 3 + 'x')
print()

print('Диаграмма процентного соотношения чисел от -3 до 3 и остальных:')
with open("sequence.txt") as f:
    kol3 = 0
    kolost = 0
    count = 0
    for line in f:
        b = float(line)
        count += 1
        if (-3 <= b <= 3):
            kol3 += 1
        else:
            kolost += 1
proc3 = round(100 * kol3/count)
procost = round(100 * kolost/count)
print('↑ %')
for i in range(100, 0, -1):
    if (proc3 >= i) and (procost >= i):
        print('|', '■ ' * 2)
    elif (proc3 >= i):
        print('|', '■')
    elif (procost >= i):
        print('|', ' ', '■')
    else:
        print('|')
print("* " + "- " * 5 + '→')
