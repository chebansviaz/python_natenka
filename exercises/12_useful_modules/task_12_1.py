# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(list_ip_adress):
    alive = []
    unreachable = []
    for ip in list_ip_adress:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            alive.append(ip)
        else:
            unreachable.append(ip)

    return (alive, unreachable )

print(ping_ip_addresses(["8.8.8.8", "9.9.9.9", "192.168.7.1", "192.168.7.2"]))