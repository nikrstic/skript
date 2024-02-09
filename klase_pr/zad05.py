def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def say_hi():
    print("hi")

say_hi()

def do_n_times(num_times):
    def decorator_do_n_times(func):
        def wrapper_do_n_times(*args,**kwargs):
            for _ in range(num_times):
                func()
        return wrapper_do_n_times
    return decorator_do_n_times
@do_n_times(num_times=5)
def say_Bye():
    print("Byw!")
say_Bye()