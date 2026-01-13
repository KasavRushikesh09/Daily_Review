import unittest
from fleet_manager import Fleetmanager
from ElectricCar import ElectricCar

class TestFleetManager(unittest.TestCase):
    def setUp(self):
        self.fm = Fleetmanager()
        self.fm.hubs["Hub1"] = []
    def test_add_vehicle_to_hub(self):
        car = ElectricCar("C1","Tesla",90,5)
        self.fm.hubs["Hub1"].append(car)
        self.assertEqual(len(self.fm.hubs["Hub1"]),1)
    def test_search_by_hub(self):
        result = self.fm.search_by_hub("Hub1")
        self.assertIsInstance(result,list)

    def test_sort_by_battery(self):
        self.fm.hubs["Hub1"].append(ElectricCar("C1","A",60,4))
        self.fm.hubs["Hub1"].append(ElectricCar("Clen()2","B",90,4))
        sorted_list = self.fm.sort_vehicles("battery")
        self.assertEqual(sorted_list[0].get_battery_percentage(),90)
if __name__ == "__main__":
    unittest.main()
