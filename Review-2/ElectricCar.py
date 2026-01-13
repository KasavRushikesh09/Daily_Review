from vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self,vehicle_id,model,battery_percentage,seating_capacity):
        super().__init__(vehicle_id,model,battery_percentage)
        if seating_capacity<=0:
            raise ValueError("Seating capacity must be positive")
        self.seating_capacity = seating_capacity
        self.set_rental_price(0.50)

    def calculate_trip_cost(self,distance):
        if distance <= 0:
            raise Exception("Distance must be a positive number")
        return distance * self.get_rental_price()

