import unittest
from ElectricCar import ElectricCar

class TestCar(unittest.TestCase):
    def test_rental_price(self):
        car = ElectricCar("c1","Tesla",90,5)
        self.assertEqual(car.get_rental_price(),0.50)
    def test_trip_cost(self):
        car = ElectricCar("c2","BMW",80,4)
        self.assertEqual(car.calculate_trip_cost(10),5.0)
    def test_invalid_distance(self):
        car = ElectricCar("c3","Audi",70,4)
        with self.assertRaises(Exception):
            car.calculate_trip_cost(-5)
if __name__ == '__main__':
    unittest.main()
