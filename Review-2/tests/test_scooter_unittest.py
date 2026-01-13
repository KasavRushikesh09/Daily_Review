import  unittest
from ElectricScooter import ElectricScooter
class TestElectricScooter(unittest.TestCase):
    def test_rental_price(self):
        scooter = ElectricScooter("s1","ola",80,60)
        self.assertEqual(scooter.get_rental_price(),0.15)
    def test_trip_cost(self):
        scooter = ElectricScooter("s2","Ather",75,70)
        self.assertEqual(scooter.calculate_trip_cost(20),3.0)
    def test_invalid_speed(self):
        with self.assertRaises(ValueError):
            ElectricScooter("s3","Ather",70,-10)
if __name__ == "__main__":
    unittest.main()