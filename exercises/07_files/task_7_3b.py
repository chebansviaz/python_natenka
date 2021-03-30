# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = input('Enter VLAN number: ')
with open('CAM_table.txt', 'r' ) as f: 
    for line in f: 
        if 'DYNAMIC' in line and vlan == line.split()[0]: 
            result = line.split() 
            print('{:10}{:20}{:30}'.format(result[0], result[1], result[3]))        


