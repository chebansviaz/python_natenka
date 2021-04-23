# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re

#def get_ip_from_cfg(router_cfg):
#    result = {}
#    regex = re.compile(r'interface (?P<INTF>\S+)\n'
#                       r'(.*\n)*'
#                       r' ip address (?P<IP>\S+) (?P<MASK>\S+)\n'
#                       r'( ip address (?P<IP_S>\S+) (?P<MASK_S>\S+) secondary)*')
#    with open(router_cfg) as f:
#        for line in f.read().split('!'):
#            if 'interface' in line and 'ip address' in line:
#                match = regex.search(line)
#                if match:
#                    if match.group('IP_S') == None:
#                        result[match.group('INTF')] = [(match.group('IP'), match.group('MASK'))]
#                    else:
#                        result[match.group('INTF')] = [(match.group('IP'), match.group('MASK')), (match.group('IP_S'), match.group('MASK_S'))]
#
#    return result

def get_ip_from_cfg(router_cfg):
    result = {}
    reg_intf = r'interface (\S+)\n'
    reg_addr = r'ip address (\S+) (\S+)'
    with open(router_cfg) as f:
        for line in f.read().split('!'):
            if 'interface' in line and 'ip address' in line:
                match_intf = re.search(reg_intf, line)
                if match_intf:
                    match_addr = re.findall(reg_addr, line)
                    if match_addr:
                        result[match_intf.group(1)] = match_addr
    return result

if __name__ == "__main__":
    print(get_ip_from_cfg("config_r2.txt"))