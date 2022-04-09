def ignore_error(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return
    return func_wrapper

@ignore_error
def division(a, b):
    return a/b
