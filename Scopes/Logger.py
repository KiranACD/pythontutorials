import datetime
def logger(fn):
    def inner(*args, **kwargs):
        dt = datetime.datetime.now()
        result = fn(*args, **kwargs)
        print('{0}:{1} called'.format(dt, fn.__name__))
        return result
    return inner