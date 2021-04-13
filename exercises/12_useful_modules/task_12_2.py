# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress
def convert_ranges_to_ip_list(list_ip_adress_ranges):
    list_ip = []
    for ip_adress_ranges in list_ip_adress_ranges:
        try:
            if ipaddress.ip_address(ip_adress_ranges):
                list_ip.append(ip_adress_ranges)
        except ValueError:
            ip_last_octet = []
            ip_first_octet = ".".join(ip_adress_ranges.split("-")[0].split(".")[:-1])
            for ip_adress in ip_adress_ranges.split("-"):
                ip_last_octet.append(ip_adress.split(".")[-1])
            for elements in range(int(ip_last_octet[0]), int(ip_last_octet[-1]) + 1):
                list_ip.append("{}.{}".format(ip_first_octet, elements))

    return list_ip

print(convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))
