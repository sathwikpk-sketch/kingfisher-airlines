from booking_category import BookingCategory

class Flight:
    def __init__(self, flight_no: str, destination: str, distance: float, base_fare: float):
        self.flight_no = flight_no
        self.destination = destination
        self.distance = distance
        self.base_fare = base_fare

    def calculate_fare(self, category: BookingCategory) -> float:
        """Calculate total fare = distance × base fare × class multiplier"""
        return self.distance * self.base_fare * category.get_multiplier()

    def __str__(self):
        return f"{self.flight_no} -> {self.destination} ({self.distance} km) ₹{self.base_fare}/km"


class NormalFlight(Flight):
    """Regular fare flight."""
    pass


class RedEyeFlight(Flight):
    """Discounted overnight flight."""
    def __init__(self, flight_no: str, destination: str, distance: float, base_fare: float, discount: float = 0.1):
        super().__init__(flight_no, destination, distance, base_fare)
        self.discount = discount

    def calculate_fare(self, category: BookingCategory) -> float:
        fare = super().calculate_fare(category)
        return fare * (1 - self.discount)
