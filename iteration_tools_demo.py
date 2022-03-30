import itertools


def demo():
    # islice_demo()
    # iterationtoolsdemo.any_all_demo()
    zip_demo()


def islice_demo():
    r = range(20)
    print(r)
    s = itertools.islice(r, 0, 15, 6)

    print(s)
    for i in s:
        print(i)

    li = [2, 4, 5, 7, 8, 10, 20]
    print(list(itertools.islice(li, 1, 6, 2)))

    cnt = itertools.count(5, 3)
    print(cnt)
    items = (x for x in cnt)  # use () to create a generator
    print(items)
    tp = itertools.islice(items, 10)
    print(tp)
    tpl = list(tp)
    print(tpl)


def any_all_demo():
    # user [] to create a list, {} to create a set
    m = [i % 3 == 0 for i in range(10)]
    print(m)
    print(any(m))
    print(all(m))


def zip_demo():
    m = [3, 5, 8, 23, 1, 78, 7, 9]
    n = [8, 2, 15, 8, 55, 9, 81]
    o = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    x = zip(m, n, o)
    print(x)
    for item in x:
        print(f"{type(item)}: {item}")
