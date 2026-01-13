import csv
import os
import json
from unittest import result

from battery_range import BatteryRangeExporter
from ElectricScooter import ElectricScooter
from ElectricCar import ElectricCar

class Fleetmanager:

    def __init__(self):
        self.hubs = {}

    def add_hub(self):
        hub = input("Enter hub name: ")
        if hub in self.hubs:
            print("Hub already exists")
        else:
            self.hubs[hub] = []
            print(f"{hub} added successfully")

    def add_vehicle_to_hub(self):
        hub = input("Enter hub name: ")
        if hub not in self.hubs:
            print("Hub not found")
            return

        option = input("1. Scooter\n2. Car\nChoose: ")

        vehicle_id = input("Vehicle ID: ")
        model = input("Model: ")
        battery = int(input("Battery %: "))

        if option == '1':
            speed = int(input("Max speed: "))
            vehicle = ElectricScooter(vehicle_id, model, battery, speed)

        elif option == '2':
            seats = int(input("Seating capacity: "))
            vehicle = ElectricCar(vehicle_id, model, battery, seats)

        else:
            print("Invalid option")
            return

        for v in self.hubs[hub]:
            if v == vehicle:
                print("Vehicle already exists")
                return

        self.hubs[hub].append(vehicle)
        print("Vehicle added successfully")
    #UC 8
    def search_by_hub(self,hub_name):
        if hub_name not in self.hubs:
            print("Hub not found")
            return []
        return self.hubs[hub_name]

    def search_high_battery_vehicles(self):
        all_vehicles = []
        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)

        return list(filter(lambda v:v.get_battery_percentage()>80,all_vehicles))

    # UC 9
    def categorized_view(self):
        categorized = {
            "Car":[],
            "Scooter":[]
        }
        #collect vehicles from all hubs
        for vehicles in self.hubs.values():
            for v in vehicles:
                if isinstance(v,ElectricCar):
                    categorized["Car"].append(v)
                elif isinstance(v,ElectricScooter):
                    categorized["Scooter"].append(v)

        return categorized

        # UC 10

    def fleet_analytics(self):
        status_count = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }

        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                status = vehicle.get_maintenance_status()
                if status in status_count:
                    status_count[status] += 1

        print("\n Fleet Analytics Summary (UC 10)")
        print("-" * 35)
        print(f"Available Vehicles       : {status_count['Available']}")
        print(f"Vehicles On Trip         : {status_count['On Trip']}")
        print(f"Under Maintenance        : {status_count['Under Maintenance']}")

    #UC:11 Alphabetical Sorting by Model Name
    def sort_vehicles_by_model(self,hub_name):
        if hub_name not in self.hubs:
            print("Hub not found")
            return []
        return sorted(self.hubs[hub_name],key = lambda v:v.model.lower())

    # UC:12 Sort

    def sort_vehicles(self, sort_by):
        all_vehicles = []
        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)

        if sort_by == "battery":
            return sorted(
                all_vehicles,
                key=lambda v: v.get_battery_percentage(),
                reverse=True
            )
        elif sort_by == "fare":
            return sorted(
                all_vehicles,
                key=lambda v: v.get_rental_price(),
                reverse=True
            )
        else:
            print("Invalid soring option")
            return []

    # UC 13: Save fleet data to CSV
    def save_to_csv(self, filename="fleet_management.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)

            #header
            writer.writerow([
                "hub", "vehicle_id", "model", "battery",
                "type", "extra", "rental_price", "status"
            ])

            for hub,vehicles in self.hubs.items():
                for v in vehicles:
                    if isinstance(v,ElectricCar):
                        v_type = "Car"
                        extra = v.seating_capacity
                    else:
                        v_type = "Scooter"
                        extra = v.max_speed_limit
                    writer.writerow([
                        hub,
                        v.vehicle_id,
                        v.model,
                        v.get_battery_percentage(),
                        v_type,
                        extra,
                        v.get_rental_price(),
                        v.get_maintenance_status()
                    ])
        print("Fleet data saved Successfully to fleet_management.csv")
    def load_from_csv(self,filename="fleet_management.csv"):
        if not os.path.exists(filename):
            return
        with open(filename,mode="r")as file:
            reader = csv.DictReader(file)

            for row in reader:
                hub = row["hub"]
                if hub not in self.hubs:
                    self.hubs[hub] = []
                if row["type"] == "Car":
                    vehicle = ElectricCar(
                        row["vehicle_id"],
                        row["model"],
                        int(row["battery"]),
                        int(row["extra"])
                    )
                elif row["type"] == "Scooter":
                    vehicle = ElectricScooter(
                        row["vehicle_id"],
                        row["model"],
                        int(row["battery"]),
                        int(row["extra"])
                    )
                vehicle.set_maintenance_status(row["status"])
                self.hubs[hub].append(vehicle)
#UC14
    def save_to_json(self,filename="fleet_management.json"):
        data = {}

        for hub, vehicles in self.hubs.items():
            data[hub] = []

            for v in vehicles:
                if isinstance(v, ElectricCar):
                    vehicle_type = "Car"
                    extra = v.seating_capacity
                else:
                    vehicle_type = "Scooter"
                    extra = v.max_speed_limit

                data[hub].append({
                    "vehicle_id":v.vehicle_id,
                    "model":v.model,
                    "battery":v.get_battery_percentage(),
                    "type":vehicle_type,
                    "extra": extra,
                    "rental_price":v.get_rental_price(),
                    "status":v.get_maintenance_status()
                })
                with open(filename,"w") as file:
                    json.dump(data,file,indent=4)
        print("Fleet data saved Successfully to fleet_management.json")
    def load_from_json(self,filename = "fleet_management.json"):
        if not os.path.exists(filename):
            print("JSON file not found.Starting fresh.")
            return
        with open(filename,mode="r")as file:
            data = json.load(file)

        for hub,vehicles in data.items():
            if hub not in self.hubs:
                self.hubs[hub] = []
            for v in vehicles:
                if v["type"] == "Car":
                    vehicle = ElectricCar(
                        v["vehicle_id"],
                        v["model"],
                        v["battery"],
                        v["extra"]
                    )
                else:
                    vehicle = ElectricScooter(
                        v["vehicle_id"],
                        v["model"],
                        v["battery"],
                        v["extra"]
                    )
                vehicle.set_maintenance_status(v["status"])
                self.hubs[hub].append(vehicle)

    def export_all_battery_ranges(self):
        BatteryRangeExporter.export_by_ranges(self.hubs)

    # def export_vehicles_by_battery_range(self,min_battery = 70,max_battery=90,filename = "battery_range.json"):
    #     for vehicles in self.hubs.values():
    #         for vehicle in vehicles:
    #             battery = vehicle.get_battery_percentage()
    #
    #             if min_battery <= battery <= max_battery:
    #                 result.append({
    #                     "model":vehicle.model,
    #                     "battery_percentage":battery
    #                 })
    #
    #             with open(filename,"w")as file:
    #                 json.dump(result,file,indent=6)
    #
    #             print(
    #                 f"Vehicles with battery {min_battery} - {max_battery}%"
    #                 f"saved to {filename}"
    #             )




