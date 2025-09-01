words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def func(dict):
    for key, value in dict.items():
        res = key * int(value)
        print(res)

func(words)