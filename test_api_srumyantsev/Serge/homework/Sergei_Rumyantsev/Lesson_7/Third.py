some_text = input()


def func(text):
    text_list = some_text.split(":")
    result = int(text_list[-1]) + 10
    print(result)


func(some_text)
