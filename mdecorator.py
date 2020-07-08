from functools import wraps

def duration(func):
    @wraps(func)
    def time(*args, **kwargs):
        import time
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Duration of {func.__name__} is: {round(end_time - start_time, 4)} seg.")

    return time