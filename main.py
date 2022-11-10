# -------------------------------- 1 ---------------------------------------
with open('text_01.txt', 'a', encoding='utf-8') as n_f:
    while True:
        user_str = input('Введите построчно данные, для завершения нажмите Enter: ')
        n_f.write(f'{user_str}\n')
        if not user_str:
            break

# -------------------------------- 2 ---------------------------------------
with open('text_02.txt', 'r', encoding='utf-8') as n_f:
    my_line = n_f.readlines()
    for str, word in enumerate(my_line, 1):
        num_words = len(word.split())
        print(f'Строка {str} содержит {num_words} слова')
    print(f'Всего строк: {str} шт.')

# -------------------------------- 3 ---------------------------------------
def info():
    dict = {}
    with open('text_03.txt', 'r', encoding='utf-8') as n_f:
        for string in n_f:
            dict[string.split()[0]] = float(string.split()[1])
    print('Меньше 20000 получают: ')
    for name, zp in dict.items():
        if zp < 20000:
            print(name)
    print(f'Средняя зарплата равна: {sum(dict.values()) / len(dict)}')
info()

# -------------------------------- 4 ---------------------------------------
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text_04(1).txt', 'w', encoding='utf-8') as n_f_1:
   with open('text_02.txt.txt', 'r', encoding='utf-8') as n_f:
      n_f_1.writelines([string.replace(string.split()[0], rus.get(string.split()[0])) for string in n_f])

# -------------------------------- 5 ---------------------------------------
from random import randint

with open('text_05.txt', 'w', encoding='utf-8') as n_f:
   my_list = [randint(1, 10) for i in range(10)]
   n_f.write(''.join(map(str, my_list)))
print(f'Общая сумма элементов: {sum(my_list)}')

# -------------------------------- 6 ---------------------------------------
my_dict = {}
num = '0123456789'

with open('text_06.txt', 'r', encoding='utf-8') as n_f:
   for string in n_f:
      item, info = string.split(':')
      my_dict[item] = sum(map(int, ''.join([i for i in info if i in num]).split()))
print(my_dict)

# -------------------------------- 7 ---------------------------------------
import json

dict = {}
av_dict = {'average_profit': 0}
res = [dict, av_dict]
with open('text_07.txt', encoding='utf-8') as file:
    firm_count = 0
    lines = file.readlines()
    for line in lines:
        if len(line):
            name, type, revenue, costs = line.split()
            firm_profit = float(revenue) - float(costs)
            dict[name] = firm_profit
            if firm_profit > 0:
                av_dict['average_profit'] += firm_profit
                firm_count += 1
        if firm_count:
            av_dict['average_profit'] /= firm_count
            print(f"\t{json.dumps(res, ensure_ascii=False)}\n")
with open('text_07(j).json', 'w') as write_file:
    json.dump(res, write_file, ensure_ascii=False)