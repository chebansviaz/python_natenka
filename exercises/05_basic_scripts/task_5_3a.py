# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
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
#vlan_id = "Введите номер VLAN: "
#vlans_id = "Введите разрешенные VLANы: "
#vlan_status = { 'access' : vlan_id , 'trunk' : vlans_id }

vlan_status = { 'access' : "Введите номер VLAN: ", 'trunk' : "Введите разрешенные VLANы: " }

vlan = input(vlan_status.get(work_mode))

mode_status = { 'access' : '\n'.join(access_template).format(vlan), 'trunk' : '\n'.join(trunk_template).format(vlan) }

print(interface_template.format(int_type))
print(mode_status.get(work_mode))

