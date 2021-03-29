# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
file_r = argv[1]
file_w = argv[2]

ignore = ["duplex", "alias", "configuration"]

f_r = open(file_r, 'r')
f_w = open(file_w, 'w')

for line in f_r:
    if line.startswith('!'):
        continue
    for key in ignore:
        if key in line:
            break
    else:
        f_w.write(line)
f_w.close()
#        print(*line.rstrip().split('\n'),)


