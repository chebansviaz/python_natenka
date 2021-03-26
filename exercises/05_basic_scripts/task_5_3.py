# -*- coding: utf-8 -*-
"""
Задание 5.3

Скрипт должен запрашивать у пользователя:
* информацию о режиме интерфейса (access/trunk)
* номере интерфейса (тип и номер, вида Gi0/3)
* номер VLANа (для режима trunk будет вводиться список VLANов)

В зависимости от выбранного режима, на стандартный поток вывода, должна возвращаться
соответствующая конфигурация access или trunk (шаблоны команд находятся в списках
access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем
соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Ограничение: Все задания надо выполнять используя только пройденные темы. То есть эту
задачу можно решить без использования условия if и циклов for/while.

Подсказка:
Подводящим к этому заданию было задание 5.1. Чтобы было легче решить это задание,
можно посмотреть на задание 5.1 и разобраться как там получилось
вывести разную информацию в зависимости от ввода пользователя.

Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:

$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): access
Введите тип и номер интерфейса: Fa0/6
Введите номер влан(ов): 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Пример выполнения скрипта, при выборе режима trunk:
$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): trunk
Введите тип и номер интерфейса: Fa0/7
Введите номер влан(ов): 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

interface_template = '''interface {}'''

work_mode = input("Введите режим работы интерфейса (access/trunk): ")
int_type = input("Введите тип и номер интерфейса (Fa0/7): ")
vlan_id = input("Введите номер влан(ов) (7,10,12): ")

mode_status = { 'access' : '\n'.join(access_template).format(vlan_id), 'trunk' : '\n'.join(trunk_template).format(vlan_id) }

print(interface_template.format(int_type))
print(mode_status.get(work_mode))


#ac_templ = ''' 
#{} 
#{} 
#{} 
#{} 
#{} 
#{} 
#'''                                                                                                                                                                                     
#
#tr_templ = ''' 
#{} 
#{} 
#{} 
#{} 
#'''    
#mode_status = { 'access': ac_templ.format( 
#                                        interface_template.format(int_type), 
#                                        access_template[0], 
#                                        access_template[1].format(vlan_id), 
#                                        access_template[2], 
#                                        access_template[3], 
#                                        access_template[4]),  
#                'trunk': tr_templ.format( 
#                                        interface_template.format(int_type), 
#                                        trunk_template[0], 
#                                        trunk_template[1], 
#                                        trunk_template[2].format(vlan_id)) }
#
#
#print(mode_status.get(work_mode))

