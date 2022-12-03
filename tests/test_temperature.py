import unittest
from konvertor.temperature import *

class TestTemperature(unittest.TestCase):
    def test_fahrenheit_to_celesius(self):
        self.assertEqual(fahrenheit_to_clesius(32), 0, 'should be 0')

    def test_celesius_to_fahrentheit(self):
        self.assertEqual(clesius_to_fahrenheit(0), 32, 'should be 32')



if __name__ == '__main__':
    unittest.main()
