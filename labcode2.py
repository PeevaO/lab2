def pattern_output(num_of_repetitions_x, num_of_repetitions_y, color):
    for i in range(0, num_of_repetitions_y):
        print(f"{' ' * 6}{color}{' ' * 8}{normal}{' ' * 6}" * num_of_repetitions_x)
        print(f"{' ' * 3}{color}{' ' * 4}{normal}{' ' * 6}{color}{' ' * 4}{normal}{' ' * 3}" * num_of_repetitions_x)
        print(f" {color}{' ' * 3}{normal}{' ' * 12}{color}{' ' * 3}{normal} " * num_of_repetitions_x)
        print(f"{color}{' ' * 3}{normal}{' ' * 14}{color}{' ' * 3}{normal}" * num_of_repetitions_x)
        print(f"{color}{' ' * 3}{normal}{' ' * 14}{color}{' ' * 3}{normal}" * num_of_repetitions_x)
        print(f" {color}{' ' * 3}{normal}{' ' * 12}{color}{' ' * 3}{normal} " * num_of_repetitions_x)
        print(f"{' ' * 3}{color}{' ' * 4}{normal}{' ' * 6}{color}{' ' * 4}{normal}{' ' * 3}" * num_of_repetitions_x)
        print(f"{' ' * 6}{color}{' ' * 8}{normal}{' ' * 6}" * num_of_repetitions_x)

black = '\u001b[40m'
red = '\u001b[41m'
green = '\u001b[42m'
yellow = '\u001b[43m'
blue = '\u001b[44m'
magenta = '\u001b[45m'
cyan = '\u001b[46m'
white = '\u001b[47m'
normal = '\u001b[0m'

print('Флаг Швейцарии:')
for i in range(3):
    print(f'{red}', ' ' * 27, f'{normal}')
for i in range(4):
    print(f'{red}', ' ' * 9, f'{white}', ' ' * 5, f'{red}', ' ' * 9, f'{normal}')
for i in range(4):
    print(f'{red}', ' ' * 5, f'{white}', ' ' * 13, f'{red}', ' ' * 5, f'{normal}')
for i in range(4):
    print(f'{red}', ' ' * 9, f'{white}', ' ' * 5, f'{red}', ' ' * 9, f'{normal}')
for i in range(3):
    print(f'{red}', ' ' * 27, f'{normal}')
print()

print('Введите цвет, количество повторений узора в длину и высоту.')
colorname = input('Введите цвет')
num_of_repetitions_in_row = int(input('Введите количество повторений узора в длину и высоту'))
num_of_repetitions_in_column = int(input())
match colorname:
    case 'белый':
        color = white
    case 'черный':
        color = black
    case 'синий':
        color = blue
    case 'розовый':
        color = magenta
    case 'желтый':
        color = yellow
    case 'красный':
        color = red
    case 'зеленый':
        color = green
    case 'голубой':
        color = cyan
print('Узор:')
pattern_output(num_of_repetitions_in_row, num_of_repetitions_in_column, color)

print('График функции y=x/3:')
print('↑ y')
for y in range(10, 0, -1):
    x = y * 3 * 2 - 1
    print('|',  ' ' * (x - 2),  '*')
print('*', '- ' * 10 * 3,  '→')
print('0', ' ' * 10 * 3 * 2, 'x')
print()

print('Диаграмма процентного соотношения чисел от -3 до 3 и остальных:')
min_num = -3
max_num = 3
with open('sequence.txt') as file:
    num_of_selected_numbers = 0
    num_of_remain_numbers = 0
    total_number = 0
    for line in file:
        number = float(line)
        total_number += 1
        if (min_num <= number <= max_num):
            num_of_selected_numbers += 1
        else:
            num_of_remain_numbers += 1
percent_of_selected_numbers = round(50 * num_of_selected_numbers/total_number )
percent_of_remain_numbers = round(50 * num_of_remain_numbers/total_number )
print('↑ %')
for i in range(50, 0, -1):
    if (percent_of_selected_numbers >= i) and (percent_of_remain_numbers >= i):
        print('|', '■■■■■' * 2)
    elif (percent_of_selected_numbers >= i):
        print('|', '■■■■■')
    elif (percent_of_remain_numbers >= i):
        print('|', ' ' * 5, '■■■■■')
    else:
        print('|')
print('*', '- ' * 10, '→')
