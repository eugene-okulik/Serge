

def repeat_me(count):
    def decorator(func):
        def wrapper(*arg, **kwagr):
            for i in range(count):
                result = func(*arg, **kwagr)
            return result
        return wrapper
    return decorator



@repeat_me(count=5)
def example(text):
    print(text)
    
example('print me')
