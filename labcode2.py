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
color = input()
if color == 'белый':
    color = white
if color == 'черный':
    color = black
if color == 'синий':
    color = blue
if color == 'розовый':
    color = magenta
if color == 'желтый':
    color = yellow
if color == 'красный':
    color = red
if color == 'зеленый':
    color = green
if color == 'голубой':
    color = cyan
num_of_repetitions_in_row = int(input())
num_of_repetitions_in_column = int(input())
print('Узор:')
string_of_pattern_1 = ' ' * 6 + color + ' ' * 7 + normal + ' ' * 6
string_of_pattern_2 = ' ' * 3 + color + ' ' * 4 + normal + ' ' * 5 + color + ' ' * 4 + normal + ' ' * 3
string_of_pattern_3 = ' ' + color + ' ' * 3 + normal + ' ' * 11 + color + ' ' * 3 + normal + ' '
string_of_pattern_4 = color + ' ' * 3 + normal + ' ' * 13 + color + ' ' * 3 + normal
for i in range(0, num_of_repetitions_in_column):
    print(string_of_pattern_1 * num_of_repetitions_in_row)
    print(string_of_pattern_2 * num_of_repetitions_in_row)
    print(string_of_pattern_3 * num_of_repetitions_in_row)
    print(string_of_pattern_4 * num_of_repetitions_in_row)
    print(string_of_pattern_4 * num_of_repetitions_in_row)
    print(string_of_pattern_3 * num_of_repetitions_in_row)
    print(string_of_pattern_2 * num_of_repetitions_in_row)
    print(string_of_pattern_1 * num_of_repetitions_in_row)

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
        print('|', '■■■■■ ' * 2)
    elif (percent_of_selected_numbers >= i):
        print('|', '■■■■■')
    elif (percent_of_remain_numbers >= i):
        print('|', ' ' * 5, '■■■■■')
    else:
        print('|')
print('*', '- ' * 10, '→')
