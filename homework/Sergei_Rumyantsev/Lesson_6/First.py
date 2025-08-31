text = input()
result_list = []

text_list = text.split(" ")
for i in text_list:
    if i[-1] == "." or i[-1] == ",":
        separator = i[-1]
        step = i.strip(".,:;!?-()")
        res = step + 'ing' + separator
        result_list.append(res)
    else:
        res = i + 'ing'
        result_list.append(res)

result = ' '.join(result_list)
print(result)
