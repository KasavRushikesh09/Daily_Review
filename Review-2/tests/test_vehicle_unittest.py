import unittest
from vehicle import Vehicle

class DummyVehicle(Vehicle):
    def calculate_trip_cost(self,distance):
        return 0
class TestVehicle(unittest.TestCase):

    def test_valid_battery_percentage(self):
        v = DummyVehicle("V1","TestModel",80)
        self.assertEqual(v.battery_percentage(),80)
    def test_invalid_battery_percentage(self):
        with self.assertRaises(ValueError):
            DummyVehicle("V2","Test",120)
    def test_valid_equality(self):
        v1 = DummyVehicle("V1","A",50)
        v2 = DummyVehicle("V1","B",90)
        self.assertEqual(v1,v2)
if __name__ == "__main__":
    unittest.main()