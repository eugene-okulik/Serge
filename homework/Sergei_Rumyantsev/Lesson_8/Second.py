

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_number(number):
    step = fibonacci_generator()
    for _ in range(number - 1):
        next(step)
    return next(step)


indexes_list = input().split(",")

for i in indexes_list:
    result = get_fibonacci_number(int(i))
    print(result)
