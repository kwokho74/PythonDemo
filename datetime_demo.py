import datetime

def demo():
    a = datetime.date(2020, 10, 22)
    print(a)
    b = datetime.date.today()
    print(b)
    print(b - a)
    print(a.toordinal())
    c = datetime.date.fromtimestamp(0)
    print(c)
    d = datetime.datetime.now()
    print(d)
    print(d.astimezone())
    print(d.strftime("%A %d %B, %Y %H:%M:%S"))

    e = datetime.datetime(2020, 1, 1)

    f = d - e
    print(f"{f} [{type(f)}]")