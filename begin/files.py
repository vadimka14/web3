# Файл log_100.json :

# import json
#
# with open('log_100.json', encoding='utf-8') as f:
#     d = json.load(f)
#
# ip_dict = {}
# for row in d:
#     if row['ip'] not in ip_dict:
#         ip_dict[row['ip']] = 1
#     else:
#         ip_dict[row['ip']] += 1
#
# 1) чему равен общий вклад топ-3 всех IP по количеству посещений? Указать процентом
# numbers = []
# for val in ip_dict.values():
#     numbers.append(val)
#
# print(f'{int(sum(sorted(numbers, reverse=True)[:3]) / sum(numbers) * 100)}%')

# 2) сколько в файле уникальных IP, с которых на сайт заходили только 1 раз
#




# counter = 0
# for key, value in ip_dict.items():
#     if value == 1:
#         counter += 1
#
# print(f"Одноразові ір:{counter}")
#
#


# Файл log_cereals.csv :
# 3) наименьшая стоимость пачки манки
# import csv

# with open('./log_cereals (2).csv', encoding='utf-8') as f:
#     reader = csv.reader(f)
    # i = 0
    # semolina = []
    # for row in reader:
    #     if i == 0:
    #         i += 1
    #         continue
    #     semolina.append(float(row[1]))
    # print(min(semolina))

    # m = 0
    # grechka = []
    # for row in reader:
    #     if m == 0:
    #         m += 1
    #         continue
    #     grechka.append(float(row[2]))
    # print(grechka)
    # print(sum(grechka) / len(grechka))
#
# 4) средняя цена на крупу за весь период наблюдений
#
# Файл log_full.csv:
# import csv
#
# with open('./log_full.csv') as f:
#     reader = csv.reader(f)
#     ip_dict = {}
#     for row in reader:
#         ip = row[1]
#         if ip not in ip_dict:
#             ip_dict[ip] = 1
#         else:
#             ip_dict[ip] += 1
# max_val = 0
# max_ip = ''
# for ip in ip_dict:
#     if ip_dict[ip] > max_val:
#         max_val = ip_dict[ip]
#         max_ip = ip
#
#
# fraction = max_val / sum(ip_dict.values()) * 100
#






# 5) найти максимально часто встречающийся IP

# 6) посчитать в процентах вклад этого IP адреса в общее кол-во запросов
# 7) найти последнюю запись в логах с этим IP и выяснить какой user-agent был у этой записи
# получить словарь:
# suspicious_agent = {
#     "ip": '...',            # самый частовстречаемый ip в логах
#     'fraction': 70.205,     # процент запросов с таким ip от общего кол-ва запросов
#     'count': 29427,         # число запросов с таким IP
#     'last': {               # вложенный словарь с 2-мя полями
#         'agent': '...',     # последний user-agent для этого ip
#         'timestamp': '...', # последний timestap для этого ip
#     }
# }
# with open('log_full.csv') as f:
#     reader = csv.reader(f)
#     agent = ''
#     timestamp = ''
#     for row in reader:
#         if row[1] == max_ip:
#             agent = row[2]
#             timestamp = row[0]
#
# suspicious_agent = {
#      "ip": max_ip,            # самый частовстречаемый ip в логах
#      'fraction': fraction,     # процент запросов с таким ip от общего кол-ва запросов
#      'count': max_val,         # число запросов с таким IP
#      'last': {               # вложенный словарь с 2-мя полями
#          'agent': agent,     # последний user-agent для этого ip
#          'timestamp': timestamp, # последний timestap для этого ip
#      }
#  }
#
# print(suspicious_agent)