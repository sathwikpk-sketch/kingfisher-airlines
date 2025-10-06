from flight import Flight, NormalFlight, RedEyeFlight
from booking import Booking
from booking_category import EconomyClass, BusinessClass, FirstClass

class BookingSystem:
    def __init__(self):
        self.flights = []
        self.bookings = []
        self.seat_counter = 0

    def add_flight(self, f: Flight):
        self.flights.append(f)

    def view_flights(self):
        print("\nAvailable Flights:")
        if not self.flights:
            print("No flights available.")
        for f in self.flights:
            print(f"- {f}")

    def make_booking(self, name: str, flight_no: str, category_choice: int):
        flight = next((f for f in self.flights if f.flight_no == flight_no), None)
        if not flight:
            print("Invalid flight number.")
            return None

        category_map = {1: EconomyClass, 2: BusinessClass, 3: FirstClass}
        if category_choice not in category_map:
            print("Invalid category choice.")
            return None

        category = category_map[category_choice]()
        self.seat_counter += 1
        booking = Booking(len(self.bookings) + 1, name, flight, category, self.seat_counter)
        self.bookings.append(booking)
        print("\n✅ Booking successful!")
        print(booking)

    def cancel_booking(self, booking_id: int):
        for b in self.bookings:
            if b.booking_id == booking_id:
                self.bookings.remove(b)
                print(f"\n❌ Booking ID {booking_id} cancelled successfully.")
                return
        print("Booking ID not found.")

    def view_bookings(self):
        print("\nYour Bookings:")
        if not self.bookings:
            print("No bookings found.")
        for b in self.bookings:
            print(b)

    def menu(self):
        while True:
            print("\n✈️ Airline Ticket Booking System")
            print("1. View All Flights")
            print("2. Make a New Booking")
            print("3. View My Bookings")
            print("4. Cancel a Booking")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.view_flights()
            elif choice == "2":
                name = input("Enter passenger name: ")
                self.view_flights()
                flight_no = input("Enter Flight No: ")
                print("1. Economy | 2. Business | 3. First Class")
                category_choice = int(input("Choose class: "))
                self.make_booking(name, flight_no, category_choice)
            elif choice == "3":
                self.view_bookings()
            elif choice == "4":
                booking_id = int(input("Enter Booking ID to cancel: "))
                self.cancel_booking(booking_id)
            elif choice == "5":
                print("Thank you for using the Airline Booking System. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
