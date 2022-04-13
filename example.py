import pkg
from utils import server


class Foo:
    def __init__(self, bar="hello"):
        self.bar = bar

    def __repr__(self):
        return f"<Foo: {self.bar}>"


@server.call
def func(a=1, b=None):
    print("FUNC()")
    return 42 + a, b


def main():
    r = func(5, b=Foo())
    print(r)
    print(pkg.test.foo(pkg.test.Foo))


if __name__ == "__main__":
    main()
