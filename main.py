from booking_system import BookingSystem
from flight import NormalFlight, RedEyeFlight

def setup_system():
    system = BookingSystem()
    # Add some sample flights
    system.add_flight(NormalFlight("AI101", "Mumbai", 1200, 2.5))
    system.add_flight(RedEyeFlight("AI202", "Delhi", 1500, 2.2))
    system.add_flight(NormalFlight("AI303", "Bangalore", 800, 3.0))
    return system

if __name__ == "__main__":
    system = setup_system()
    system.menu()
