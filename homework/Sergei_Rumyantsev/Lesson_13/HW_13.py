import os
from datetime import datetime, timedelta


base_path = os.path.dirname(os.path.abspath(__file__))
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")


with open(file_path, 'r', encoding='utf-8') as file:
    data_list = []
    for files in file:
        data_list.append(files)

liist = []

for data in data_list:
    a = data.split(' ')

    if a[0][0] == '1':
        first = a[1] + ' ' + a[2]
        first_datetime = datetime.strptime(first, "%Y-%m-%d %H:%M:%S.%f")
        first_res = first_datetime + timedelta(7)
        print(f'Какая дата была через неделю от запрошенной: {first_res}')

    elif a[0][0] == '2':
        second = a[1] + ' ' + a[2]
        second_datetime = datetime.strptime(second, "%Y-%m-%d %H:%M:%S.%f")
        print(f'Какой будет день недели: {second_datetime.strftime("%A")}')

    elif a[0][0] == '3':
        third = a[1] + ' ' + a[2]
        third_datetime = datetime.strptime(third, "%Y-%m-%d %H:%M:%S.%f")
        thrid_diff = datetime.now() - third_datetime
        print(f'Сколько дней назад была эта дата: {thrid_diff.days}')
