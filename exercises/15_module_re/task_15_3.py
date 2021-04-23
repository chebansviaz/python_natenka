# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re

def convert_ios_nat_to_asa(NAT_Cisco_IOS, NAT_Cisco_ASA):
    with open(NAT_Cisco_IOS, 'r') as f_src, open(NAT_Cisco_ASA, 'w') as f_dst:
        for line in f_src.readlines():
            line_ios = re.split(r' ', line.rstrip())
            line_asa = [f'object network LOCAL_{line_ios[6]}\n',
                        f' host {line_ios[6]}\n',
                        f' nat (inside,outside) static interface service {line_ios[5]} {line_ios[7]} {line_ios[10]}\n']
            f_dst.writelines(line_asa)

if __name__ == "__main__":
    convert_ios_nat_to_asa('cisco_nat_config.txt', 'cisco_nat_config_asa.txt')

