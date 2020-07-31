import time

def time_wrapper(func):
    def decorator(*args, **kwargs):
        start_time = time.time()
        print("%s %s" % (func.__name__, " is executed"))
        result = func(*args, **kwargs)
        print("%s %s %s %s" % (func.__name__ , " is finished. It takes ", str(time.time()-start_time), "seconds"))
        return result
    return decorator
