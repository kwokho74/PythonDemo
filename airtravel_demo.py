import airtravel
from pprint import pprint as pp


def demo():
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
