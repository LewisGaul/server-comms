from utils import server


class Foo:
    pass


@server.call
def foo(a=None):
    print("FOO:", a)
    return a
