class Ticket:
    def __init__(self, name, price, available_tickets):
        self.name = name
        self.price = price
        self.available_tickets = available_tickets
        self.booked_tickets = 0

    def book_tickets(self, quantity):
        if quantity <= self.available_tickets:
            self.booked_tickets += quantity
            self.available_tickets -= quantity
            return True
        else:
            print(f"Sorry, only {self.available_tickets} tickets available.")
            return False

class BookingSystem:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def display_available_tickets(self):
        print("Available Tickets:")
        for ticket in self.tickets:
            print(f"{ticket.name}: ${ticket.price} - Available Tickets: {ticket.available_tickets}")

def main():
    booking_system = BookingSystem()

    # Menambahkan tiket-tiket objek wisata
    ticket1 = Ticket("Zoo", 20, 100)
    ticket2 = Ticket("Museum", 15, 50)
    ticket3 = Ticket("Theme Park", 30, 80)

    booking_system.add_ticket(ticket1)
    booking_system.add_ticket(ticket2)
    booking_system.add_ticket(ticket3)

    print("Welcome to Adventure Booking System!")
    booking_system.display_available_tickets()

    choice = input("\nEnter the name of the attraction you want to book tickets for: ")

    for ticket in booking_system.tickets:
        if ticket.name.lower() == choice.lower():
            quantity = int(input(f"How many tickets do you want to book for {ticket.name}? "))
            if ticket.book_tickets(quantity):
                print(f"{quantity} tickets booked successfully for {ticket.name}.")
                break
    else:
        print("Attraction not found!")

if __name__ == "__main__":
    main()
