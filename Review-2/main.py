from fleet_manager import Fleetmanager

class EcoRideMain:
    def greet(self):
       print("Welcome to Eco-Ride urban Mobility system")
    def main(self):
        self.greet()
        fm = Fleetmanager()
        fm.load_from_csv()
        fm.load_from_json()
        #------ UC 1 & 2
        fm.add_hub()
        fm.add_vehicle_to_hub()
        fm.add_vehicle_to_hub()
  # UC8
        print("\n --- Search Vehicle by Hub --- ")
        hub_name = input("Enter hub to search: ")
        vehicles = fm.search_by_hub(hub_name)

        for v in vehicles:
            print(v.vehicle_id,v.model,v.get_battery_percentage())

        print("\n ~~~ Vehicle with Battery > 80% ~~~")
        high_battery = fm.search_high_battery_vehicles()

        for v in high_battery:
            print(v.vehicle_id,v.model,v.get_battery_percentage())
    #UC9
        print("\n ---  Categorized View (UC 9) ---")
        categorized = fm.categorized_view()

        print("\n --- Car ---")
        for car in categorized["Car"]:
            print(car.vehicle_id,car.model,car.get_battery_percentage())

        print("\n --- Scooters --- ")
        for scooter in categorized["Scooter"]:
            print(scooter.vehicle_id,scooter.model,scooter.get_battery_percentage())

    #UC10
            fm.fleet_analytics()
    #UC11

        print("\n--- Alphabetical Sorting by Model (UC 11) ---")
        hub_name = input("Enter hub name:")
        sorted_vehicles = fm.sort_vehicles_by_model(hub_name)

        for v in sorted_vehicles:
            print(v)
    #UC12
        print("\n --- UC12 : Sort by Battery Level ---")
        battery_sorted = fm.sort_vehicles("battery")
        for v in battery_sorted:
            print(v.vehicle_id,v.model,v.get_battery_percentage())

        print("\n --- UC12 : Sort by Fare Price ---")
        fare_sorted = fm.sort_vehicles("fare")
        for v in fare_sorted:
            print(v.vehicle_id,v.model,v.get_rental_price())

        # Export vehicles into all battery ranges
        fm.export_all_battery_ranges()

        #UC13
        fm.save_to_csv()
    #UC13
        fm.save_to_json()
if __name__ == "__main__":
    app = EcoRideMain()
    app.main()

