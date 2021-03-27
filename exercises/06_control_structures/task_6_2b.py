# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите IP-адрес в формате 10.0.1.1: ')

ip_correct = False

while not ip_correct:
   for okt in ip.split("."):
       if not okt.isdigit() or len(ip.split(".")) != 4 or int(okt) not in range(256):
           print('Неправильный IP-адрес')
           ip = input('Повторите попытку ввести IP-адрес в формате 10.0.1.1: ')
           break
   else:
       ip_correct = True
       oct1, oct2, oct3, oct4 = ip.split(".")
       if ip == '255.255.255.255':
         print('local broadcast')
       elif ip == '0.0.0.0':
           print('unassigned')
       elif int(ip.split(".")[0]) in range(1, 224):
           print('unicast')
       elif int(ip.split(".")[0]) in range(224, 240):
           print('multicast')
       else:
           print('unused')

