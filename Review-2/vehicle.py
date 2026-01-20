from abc import ABC, abstractmethod

class Vehicle(ABC):

     def __init__(self, vehicle_id, model, battery_percentage):
         self.vehicle_id = vehicle_id
         self.model = model
         self.__rental_price = 0
         self.__maintenance_status = "Available"
        #correct setter call
         self.battery_percentage = battery_percentage
         self.set_battery_percentage(battery_percentage)

     @abstractmethod
     def calculate_trip_cost(self,distance):
        pass
     #-----------Battery Percentage-------
     def get_battery_percentage(self):
         return self.__battery_percentage
     def set_battery_percentage(self, battery_percentage):
         if 0 <= battery_percentage <= 100:
             self.__battery_percentage = battery_percentage
         else:
              raise ValueError("battery must be between 0 and 100")
    # --------Rental Price --------
     def get_rental_price(self):
        return self.__rental_price

     def set_rental_price(self,price):
        if price > 0:
            self.__rental_price = price
        else:
            raise ValueError("rental price must be positive")

     def get_maintenance_status(self):
         return self.__maintenance_status

     def set_maintenance_status(self, status):
         self.__maintenance_status = status

     def __str__(self):
         return (
             f"ID: {self.vehicle_id},"
             f"model: {self.model},"
             f"battery percentage: {self.battery_percentage}%,"
             f"status: {self.get_maintenance_status()}"
         )
     def __eq__(self,other):
         return isinstance(other,Vehicle) and self.vehicle_id == other.vehicle_id

# def check_required(text_value, field_name, field_path):
#     if text_value is None or (isinstance(text_value, str) and text_value.strip() == ""):
#         return {
#             "field": field_name,
#             "path": field_path,
#             "error_code": "REQUIRED",
#             "message": "This field is required."
#         }
#     return None
#
#
# def check_string_type(text_value, field_name, field_path):
#     if text_value is None:
#         return None
#
#     if not isinstance(text_value, str):
#         return {
#             "field": field_name,
#             "path": field_path,
#             "error_code": "TYPE_ERROR",
#             "message": "Value must be a string."
#         }
#     return None
#
#
# def check_max_size(text_value, field_name, field_path, limit):
#     if not isinstance(text_value, str):
#         return None
#
#     if len(text_value) > limit:
#         return {
#             "field": field_name,
#             "path": field_path,
#             "error_code": "MAX_LENGTH",
#             "message": f"Text must be <= {limit} characters."
#         }
#     return None
#
#
# def check_bad_patterns(text_value, field_name, field_path):
#
#     if not isinstance(text_value, str):
#         return None
#
#     bad_rules = [
#         ("SCRIPT_TAG", r"<\s*script\b"),             # <script>
#         ("REPEATED_SYMBOLS", r"([!@#$%^&*])\1{2,}"), # !!! or @@@
#         ("UNCLOSED_BRACKET", r"\[[^\]]*$")           # [abc (not closed)
#     ]
#
#     for code, pattern in bad_rules:
#         if re.search(pattern, text_value, flags=re.IGNORECASE):
#             return {
#                 "field": field_name,
#                 "path": field_path,
#                 "error_code": code,
#                 "message": "Malformed text pattern detected."
#             }
#
#     return None
#
#
# def validate_payload_texts(request_body):
#     """
#     Main validator function
#     Returns:
#         {
#             "valid": True/False,
#             "errors": [...]
#         }
#     """
#
#     config = [
#         {"field": "bio", "path": "user.bio", "max_len": 50},
#         {"field": "note", "path": "data.note", "max_len": 100}
#     ]
#
#     all_errors = []
#
#     for item in config:
#         field_name = item["field"]
#         field_path = item["path"]
#         max_len = item["max_len"]
#
#         text_value = pick_value(request_body, field_path)
#
#         # run checks
#         err = check_required(text_value, field_name, field_path)
#         if err:
#             all_errors.append(err)
#             continue  # no need to check other rules
#
#         err = check_string_type(text_value, field_name, field_path)
#         if err:
#             all_errors.append(err)
#             continue
#
#         err = check_max_size(text_value, field_name, field_path, max_len)
#         if err:
#             all_errors.append(err)
#
#         err = check_bad_patterns(text_value, field_name, field_path)
#         if err:
#             all_errors.append(err)
#
#     return {
#         "valid": len(all_errors) == 0,
#         "errors": all_errors
#     }
#
# if __name__ == "__main__":
#     payload = {
#         "user": {"bio": "Hello!!! <script>alert(1)</script>"},
#         "data": {"note": "Good [test"}
#     }
#
#     output = validate_payload_texts(payload)
#     print(output)