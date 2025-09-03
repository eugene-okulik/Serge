temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


def hot_days(temp):
    return temp >= 28


filtered_list = filter(hot_days, temperatures)
result = list(filtered_list)

print(result)
print(max(temperatures))
print(min(temperatures))
print(sum(temperatures) / len(temperatures))
