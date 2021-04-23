# -*- coding: utf-8 -*-
"""
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей со значениями

Функция возвращает результат в виде списка словарей,
где ключи - взяты из первого списка, а значения подставлены из второго.

Например, если функции передать как аргументы список headers и список
[('R1', '12.4(24)T1', 'Cisco 3825'),
 ('R2', '15.2(2)T1', 'Cisco 2911')]

Функция должна вернуть такой список со словарями:
[{'hostname': 'R1', 'ios': '12.4(24)T1', 'platform': 'Cisco 3825'},
 {'hostname': 'R2', 'ios': '15.2(2)T1', 'platform': 'Cisco 2911'}]

Функция не должна быть привязана к конкретным данным или количеству
заголовков/данных в кортежах.

Проверить работу функции:
* первый аргумент - список headers
* второй аргумент - список data

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

headers = ["hostname", "ios", "platform"]

data = [
    ("R1", "12.4(24)T1", "Cisco 3825"),
    ("R2", "15.2(2)T1", "Cisco 2911"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]
#import re
#from pprint import pprint
#def convert_to_dict(list_headers, list_tuples):
#    result = []
#    regex = (r'(?P<HOSTNAME>(?:R|SW)\d+)|'
#             r'(?P<IOS>\S+\.\S+)|'
#             r'(?P<PLATFORM>\S+ \S+)')
#    for line in data:
#        dict_line = {}
#        for value in line:
#            patern = re.match(regex, value)
#            if patern.group('HOSTNAME'):
#                dict_line[headers[0]] = patern.group('HOSTNAME')
#            elif patern.group('IOS'):
#                dict_line[headers[1]] = patern.group('IOS')
#            elif patern.group('PLATFORM'):
#                dict_line[headers[2]] = patern.group('PLATFORM')
#        result.append(dict_line)
#    return result

#def convert_to_dict(list_headers, list_tuples):
#    for line in list_tuples:
#        print(dict(zip(list_headers, line)))
#    result = [dict(zip(list_headers, line)) for line in list_tuples]
#    return result

convert_to_dict = lambda list_headers, list_tuples: [dict(zip(list_headers, line)) for line in list_tuples]

if __name__ == "__main__":
    pprint(convert_to_dict(headers, data))