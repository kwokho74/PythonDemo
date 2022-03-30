def demo():
    a = iter(gen123())
    print(a)
    print(next(a))
    print(next(a))
    print(next(a))


def gen123():
    print("going to yield 1")
    yield 1
    print("going to yield 2")
    yield 2
    print("going to yield 3")
    yield 3
    print("going to return")
