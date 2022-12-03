import unittest
from konvertor import *

class TestTemperature(unittest.TestCase):
    def test_fahrenheit_to_celesius(fahrenheit):
        self.assertEqual(fahrenheit_to_celesius(32), 0, 'should be 0')

    def test_celesius_to_fahrentheit(celesius):
        self.assertEqual(celesius_to_fahrenheit(0), 32, 'should be 0')



if __name__ == '__main__':
    unittest.main()
