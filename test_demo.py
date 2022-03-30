import unittest
import general_demo
import airtravel


class DemoTestCase(unittest.TestCase):
    """Test demo"""

    def setUp(self):
        self.aircraft = airtravel.AirbusA319("ABNN901")

    def test_general_demo(self):
        result = general_demo.add(3, 5)
        self.assertEqual(result, 8)

    def test_airtravel(self):
        seats = self.aircraft.num_seats()
        self.assertEqual(seats, 132)


if __name__ == "__main__":
    unittest.main()
