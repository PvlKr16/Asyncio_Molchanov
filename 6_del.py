def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except BlaBlaException:
            print('BlaBla')
        else:
            print('.......', message)


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    yield from g
