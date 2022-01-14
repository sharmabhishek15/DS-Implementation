
def decorator(func):
    print("Decorator function")
    def inner(*args, **kwargs):
        print("Inside inner")
        func()
    return inner

@decorator
def need_to_decorate():
    print("Decorate this function")


if __name__ == '__main__':
    print(need_to_decorate())