# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
file = open('ospf.txt', 'r')
for line in file:
    print(f'''
Prefix               {line.split()[1]}
AD/Metric            {line.split()[2][1:-1]}
Next-Hop             {line.split()[4][:-1]}
Last update          {line.split()[5][:-1]}
Outbound Interface   {line.split()[6]}''')

