from vehicle import Vehicle

class ElectricScooter(Vehicle):
    def __init__(self,vehicle_id,model,battery_percentage,max_speed_limit):
        super().__init__(vehicle_id,model,battery_percentage)
        if max_speed_limit <= 0:
          raise ValueError("speed must be greater than 0")
        self.max_speed_limit = max_speed_limit
        self.set_rental_price(0.15)
    def calculate_trip_cost(self,distance):
        if distance <= 0:
            raise ValueError("Distance must be positive")
        return distance * self.get_rental_price()