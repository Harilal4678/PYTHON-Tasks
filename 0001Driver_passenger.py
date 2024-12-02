class Ride:
    def __init__(self, pickup_location, drop_location, distance):
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.distance = distance
        self.fare = self.calculate_fare()

    def calculate_fare(self):
        rate_per_km = 10
        return self.distance * rate_per_km

class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle
        self.is_available = True

class Passenger:
    def __init__(self, name):
        self.name = name

    def request_ride(self, pickup_location, drop_location, distance, drivers):
        for driver in drivers:
            if driver.is_available:
                driver.is_available = False
                ride = Ride(pickup_location, drop_location, distance)
                return driver, ride
        return None, None

drivers = [Driver("Alice", "Car A"), Driver("Bob", "Car B")]
passenger = Passenger("John")

pickup = "Location A"
drop = "Location B"
distance = 15

assigned_driver, ride = passenger.request_ride(pickup, drop, distance, drivers)

if assigned_driver and ride:
    print(f"Driver {assigned_driver.name} assigned with vehicle {assigned_driver.vehicle}.")
    print(f"Pickup: {ride.pickup_location}, Drop: {ride.drop_location}, Fare: {ride.fare}")
else:
    print("No drivers available.")
