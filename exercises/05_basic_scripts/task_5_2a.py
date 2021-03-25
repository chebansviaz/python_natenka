# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
network_input = input('Введите IP-сети в формате: 10.1.1.0/24 : ')

ip, mask = network_input.split("/")

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

ip_bin = "{:08b}{:08b}{:08b}{:08b}".format( int(ip.split('.')[0]), int(ip.split('.')[1]), int(ip.split('.')[2]), int(ip.split('.')[3]))

#ip_template = '''{ip0:08b}{ip1:08b}{ip2:08b}{ip3:08b}'''

#ip_bin = ip_template.format( ip0 = int(ip.split('.')[0]), ip1 = int(ip.split('.')[1]), ip2 = int(ip.split('.')[2]), ip3 = int(ip.split('.')[3]))

net_bin = "{}{}".format(ip_bin[0:int(mask)], "0"*len(ip_bin[int(mask):32]))

print(network_template.format(  ip0 = int(net_bin[0:8], 2),
                                ip1 = int(net_bin[8:16], 2),
                                ip2 = int(net_bin[16:24], 2),
                                ip3 = int(net_bin[24:32], 2)))

print(mask_template.format( mask = mask,
                            okt0 = int(mask_bin[0:8], 2),
                            okt1 = int(mask_bin[8:16], 2),
                            okt2 = int(mask_bin[16:24], 2),
                            okt3 = int(mask_bin[24:32], 2))) 
