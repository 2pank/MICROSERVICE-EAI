class Room:
    def __init__(self, room_number, price, is_booked=False):
        self.room_number = room_number
        self.price = price
        self.is_booked = is_booked

class HotelBookingSystem:
    def __init__(self):
        self.rooms = [Room("101", 100), Room("102", 120), Room("103", 150)]

    def display_available_rooms(self):
        print("Available Rooms:")
        for room in self.rooms:
            if not room.is_booked:
                print(f"Room: {room.room_number} - Price: ${room.price}")

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_booked:
                room.is_booked = True
                return True
        return False

def main():
    booking_system = HotelBookingSystem()

    print("Welcome to Hotel XYZ Booking System!")

    name = input("Enter your name: ")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
    nights = int(input("Enter number of nights: "))
    num_rooms = int(input("Enter number of rooms: "))

    print("\nAvailable Rooms:")
    booking_system.display_available_rooms()

    for _ in range(num_rooms):
        room_number = input("\nEnter room number to book: ")
        if booking_system.book_room(room_number):
            print(f"Room {room_number} booked successfully!")
        else:
            print(f"Room {room_number} is either not available or does not exist.")

    total_cost = sum(room.price * nights for room in booking_system.rooms if room.is_booked)
    print(f"\nThank you, {name}! Your booking details:")
    print(f"Check-in date: {check_in_date}")
    print(f"Number of nights: {nights}")
    print(f"Total cost: ${total_cost}")

if __name__ == "__main__":
    main()
