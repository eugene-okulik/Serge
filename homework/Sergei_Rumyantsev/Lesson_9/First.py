import datetime


date = "Jan 15, 2023 - 12:05:33"
converted_date = datetime.datetime.strptime(date, "%b %d, %Y - %H:%M:%S")

print(converted_date.strftime("%B"))
print(converted_date.strftime("%d.%m.%Y, %H:%M"))
