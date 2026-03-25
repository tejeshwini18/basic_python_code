"""Simple decorator demonstration."""


def decorator_func(func):
    def wrapper_func():
        print("wrapper_func worked")
        return func()

    print("decorator_func worked")
    return wrapper_func


def show():
    print("show worked")


decorator_show = decorator_func(show)
decorator_show()
