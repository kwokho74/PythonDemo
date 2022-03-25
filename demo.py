"""
This is a demo projet.

Usage:
    python Demo.py
"""


from msilib.schema import Error
from pprint import pprint as pp
import airtravel
import generatordemo
import iterationtoolsdemo
import filedemo
import fractal


def Add(x, y):
    """
    Adds 2 number and return the result.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
    """
    return x+y


def ListDemo():
    s = [45, 76, 22, 98, 123, 99, 368]
    print(s[1:3])
    print(s[1:-1])
    print(s[2:])
    print(s[:2])
    print(s[:])
    t = s
    print(f"{t}, {t is s}")
    r = s[:]
    print(f"{r}, {r is s}")
    print(f"{r}, {r == s}")
    u = s.copy()
    print(f"{u}, {u is s}")
    v = list(s)
    print(f"{v}, {v is s}")


def AsteriskDemo():
    c = [24, 56]
    d = c * 4
    print(d)
    c[0] = 3
    print(c)
    print(d)
    d[1] = 20
    print(d)
    e = [0] * 9
    print(e)
    f = [[-1, 1]] * 5
    print(f)
    f[0][1] = 5
    print(f)


def ExceptionDemo():
    m = 0
    n = 12
    try:
        return n / m
    except(Exception) as e:
        print(f"{e!r}")
        return -1
    finally:
        print("Clean up")


def ComprehensionsDemo():
    s = "This is a string that used to demostrate the comprehensions for list and set"
    words = s.split()
    print(words)

    # user [] to create a list, {} to create a set, () to create a generator

    m = [len(word)*2 for word in words]
    print(f"{type(m)}: {m}")

    n = [len(word)*2 for word in words if word != "string"]
    print(f"{type(n)}: {n}")

    o = {len(word)*2 for word in words}
    print(f"{type(o)}: {o}")

    countrytocapital = {"UK": "London",
                        "Canada": "Ottawa",
                        "Japan": "Tokyo"}
    print(countrytocapital)
    capitaltocountry = {ca: co for co, ca in countrytocapital.items()}
    print(capitaltocountry)


def GeneratorDemo():
    a = iter(generatordemo.gen123())
    print(a)
    print(next(a))
    print(next(a))
    print(next(a))


def IteratDemo():
    # iterationtoolsdemo.IsliceDemo()
    # iterationtoolsdemo.AnyAllDemo()
    iterationtoolsdemo.ZipDemo()


def AirTravelDemo():
    #aircraft = airtravel.Aircraft("J-PRG8", "B737", 25, 6)
    #flight = airtravel.Flight("CX123", aircraft)
    # print(flight.number())
    # print(flight.aircraft_model())
    # pp(flight._seating)
    #flight.allocate_seat("5B", "John")
    #flight.allocate_seat("25D", "Peter")
    # pp(flight._seating)
    #flight.relocate_passenger("25D", "5C")
    # pp(flight._seating)
    f1, f2 = airtravel.make_flights()
    pp(f1._seating)
    pp(f1.num_available_seats())
    pp(f2._seating)
    pp(f2.num_available_seats())
    f1.make_boarding_cards(airtravel.card_printer)


def FileDemo():
    # filedemo.WriteTextFileDemo()
    # filedemo.ReadTextFileDemo()

    pixels = fractal.mandelbrot(448, 256)
    filedemo.write_grayscale("mandel.bmp", pixels)


def Main():
    # print(Add(5, 6))
    # ListDemo()
    # AsteriskDemo()
    # ExceptionDemo()
    # ComprehensionsDemo()
    # GeneratorDemo()
    # IteratDemo()
    # AirTravelDemo()
    FileDemo()


if __name__ == '__main__':
    Main()
