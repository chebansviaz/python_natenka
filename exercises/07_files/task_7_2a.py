# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
file = argv[1]
ignore = ["duplex", "alias", "configuration"]
f = open(file, 'r')
for line in f:
    if line.startswith('!'):
        continue
    for key in ignore:
        if key in line:
            break
    else:
        print(*line.rstrip().split('\n'),)

