# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network = input('Введите IP-сети в формате: 10.1.1.0/24 : ')
ip, mask = network.split("/")
network_template = '''
Network:
{ip0:<8}  {ip1:<8}  {ip2:<8}  {ip3:<8}
{ip0:08b}  {ip1:08b}  {ip2:08b}  {ip3:08b}
'''
mask_bin = "1"*int(mask) + "0"*(32-int(mask))
mask_template = '''
Mask:
/{mask}
{okt0:<8}  {okt1:<8}  {okt2:<8}  {okt3:<8}
{okt0:08b}  {okt1:08b}  {okt2:08b}  {okt3:08b}
'''

print(network_template.format(  ip0 = int(ip.split('.')[0]),
                                ip1 = int(ip.split('.')[1]),
                                ip2 = int(ip.split('.')[2]),
                                ip3 = int(ip.split('.')[3])))
print(mask_template.format( mask = mask,
                            okt0 = int(mask_bin[0:8], 2),
                            okt1 = int(mask_bin[8:16], 2),
                            okt2 = int(mask_bin[16:24], 2),
                            okt3 = int(mask_bin[24:32], 2)))
