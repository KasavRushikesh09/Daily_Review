import json
class BatteryRangeExporter:
    BATTERY_RANGES = [
        (0, 10),
        (11, 20),
        (21, 30),
        (31, 40),
        (41, 50),
        (51, 60),
        (61, 70),
        (71, 80),
        (81, 90),
        (91, 100)
    ]
    @staticmethod
    def export_by_ranges(hubs, filename="battery_ranges.json"):
        result = {}
        for low, high in BatteryRangeExporter.BATTERY_RANGES:
            result[f"{low}-{high}"] = []

        for vehicles in hubs.values():
            for vehicle in vehicles:
                battery = vehicle.get_battery_percentage()

                for low, high in BatteryRangeExporter.BATTERY_RANGES:
                    if low <= battery <= high:
                        result[f"{low}-{high}"].append({
                            "model": vehicle.model,
                            "battery_percentage": battery
                        })
                        break

        with open(filename, "a") as file:
            json.dump(result, file, indent=4)

        print("Vehicles exported into battery ranges successfully")
