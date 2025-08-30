"""
# Выглядит проще, но не подходит под условие задачи "С помощью срезов и метода index" :(
some_text = input()

text_list = some_text.split(":")
result = int(text_list[-1]) + 10

print(result)
"""

some_text = input()

colon_index = some_text.index(":")

number_str = some_text[colon_index + 1:].strip()

result = int(number_str) + 10

print(result)
