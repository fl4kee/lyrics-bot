from functools import wraps

def decorator(func):

    @wraps(func)
    def inner(*args,**kwargs):
        print(f'This is your hash {hash(func(*args, **kwargs))}')
    return inner

@decorator
def qr_(x):
    """
    It s sqr
    :param x:
    :return:
    """
    return x**2


qr_(4)

help(qr_)