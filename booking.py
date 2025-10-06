from flight import Flight
from booking_category import BookingCategory

class Booking:
    def __init__(self, booking_id: int, passenger_name: str, flight: Flight, category: BookingCategory, seat_no: int):
        self.booking_id = booking_id
        self.passenger_name = passenger_name
        self.flight = flight
        self.category = category
        self.seat_no = seat_no
        self.ticket_cost = self.flight.calculate_fare(category)

    def __str__(self):
        return (f"Booking ID: {self.booking_id} | Passenger: {self.passenger_name} | "
                f"Flight: {self.flight.flight_no} -> {self.flight.destination} | "
                f"Class: {self.category.__class__.__name__} | Seat: {self.seat_no} | "
                f"Cost: ₹{self.ticket_cost:.2f}")
