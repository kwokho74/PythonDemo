from decimal import Decimal
import decimal
from fractions import Fraction


def demo():
    #decDemo()
    #trapFloatDemo()
    fractionDemo()


def decDemo():
    m = 0.8
    n = 0.7
    o = m-n
    print(f"m: {m}\nn: {n}\no: {o} [{type(o)}]\n")

    p = Decimal(m)
    q = Decimal(n)
    r = p-q
    print(f"p: {p}\nq: {q}\nr: {r} [{type(r)}]\n")

    t = Decimal(0.8)
    u = Decimal(0.7)
    v = t-u
    print(f"t: {t}\nu: {u}\nv: {v} [{type(v)}]\n")

    x = Decimal("0.8")
    y = Decimal("0.7")
    z = x-y
    print(f"x: {x}\ny: {y}\nz: {z} [{type(z)}]\n")


def trapFloatDemo():
    # enable decimal.FloatOperation exception
    decimal.getcontext().traps[decimal.FloatOperation] = True

    x = Decimal("0.8")
    y = Decimal("0.7")
    z = x-y
    print(f"x: {x}\ny: {y}\nz: {z} [{type(z)}]\n")

    t = Decimal(0.8)
    u = Decimal(0.7)
    v = t-u
    # decimal.FloatOperation exception
    print(f"t: {t}\nu: {u}\nv: {v} [{type(v)}]\n")


def fractionDemo():
    a = Fraction(5, 7)
    b = Fraction(1, 3)
    c = a + b
    d = a - b
    e = a * b
    print(f"a={a}\nb={b}\nc={c}\nd={d}\ne={e}")


