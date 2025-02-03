import sys  

class Room():
    def __init__(self, room_no, room_type, room_price, room_status):
        self.room_no = room_no # Room number
        self.room_type = room_type # if its a single room, double room, or a suite
        self.room_price = room_price # Price per night 
        self.room_status = room_status # Available or Not Available

    def get_room_status(self):
        return self.room_status
    
    def get_room_type(self):
        return self.room_type

    def get_room_price(self):
        return self.room_price
    
    
    

class Guest():
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no
    

class Booking():
    def __init__(self, room, guest, check_in_date, check_out_date):
        self.room = room
        self.guest = guest
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
    
    def get_booking_details(self):
        return {
            'Room No': self.room.room_no,
            'Room Type': self.room.room_type,
            'Room Price': self.room.room_price,
            'Guest Name': self.guest.name,
            'Guest Age': self.guest.age,
            'Guest Phone No': self.guest.phone_no,
            'Check In Date': self.check_in_date,
            'Check Out Date': self.check_out_date
        }





class Hotel():

    def __init__(self, name, rooms):
        self.name = name
        if isinstance(rooms, list):
            self.rooms = rooms
        else:
            raise ValueError('Rooms should be a list of Room objects')
        self.bookings = []
        
    def get_available_rooms(self, check_in_date, check_out_date):
        available_rooms = []
        for room in self.rooms:
            if room.get_room_status() == 'Available':
                if self.is_room_available(room, check_in_date, check_out_date):
                    available_rooms.append(room)
        return available_rooms
    
    def is_room_available(self, room, check_in_date, check_out_date):
        for booking in self.bookings:
            if booking.room == room:
                if check_in_date >= booking.check_in_date and check_in_date <= booking.check_out_date:
                    return False
                if check_out_date >= booking.check_in_date and check_out_date <= booking.check_out_date:
                    return False
        return True
    
    def book_room(self, room, guest, check_in_date, check_out_date):
        if self.is_room_available(room, check_in_date, check_out_date):
            booking = Booking(room, guest, check_in_date, check_out_date)
            self.bookings.append(booking)
            return booking
        else:
            return 'Room not available'
    
    def get_bookings(self):
        return self.bookings
    
    def get_rooms(self):
        return self.rooms
    
    def cancle_booking(self, booking):
        self.bookings.remove(booking)
        return 'Booking Cancelled'
    
    def checkout(self, booking):
        self.bookings.remove(booking)
        return 'Checkout Successful'
    
    def get_hotel_details(self):
        return {
            'Hotel Name': self.name,
            'Total Rooms': len(self.rooms),
            'Total Bookings': len(self.bookings)
        }
    
    def get_booking_details(self, booking):
        return booking.get_booking_details()
    
    def get_room_details(self, room):
        return {
            'Room No': room.room_no,
            'Room Type': room.room_type,
            'Room Price': room.room_price,
            'Room Status': room.room_status
        }
    
    def get_guest_details(self, guest):
        return {
            'Guest Name': guest.name,
            'Guest Age': guest.age,
            'Guest Phone No': guest.phone_no
        }
    
    def get_booking_by_room(self, room):
        for booking in self.bookings:
            if booking.room == room:
                return booking
        return 'No Booking Found'
    


def main():
    # Testdaten erstellen
    room1 = Room(101, "Single", 50, "Available")
    room2 = Room(102, "Double", 80, "Available")
    room3 = Room(103, "Suite", 150, "Available")
    
    hotel = Hotel("Grand Plaza", [room1, room2, room3])
    
    while True:
        print("\n--- Hotel Management System ---")
        print("1. Verfügbare Zimmer anzeigen")
        print("2. Zimmer buchen")
        print("3. Buchungen anzeigen")
        print("4. Buchung stornieren")
        print("5. Checkout durchführen")
        print("6. Hotel-Details anzeigen")
        print("7. Beenden")
        
        choice = input("Wähle eine Option: ")
        
        if choice == "1":
            check_in = input("Check-in Datum (YYYY-MM-DD): ")
            check_out = input("Check-out Datum (YYYY-MM-DD): ")
            available_rooms = hotel.get_available_rooms(check_in, check_out)
            if available_rooms:
                print("Verfügbare Zimmer:")
                for room in available_rooms:
                    print(f"Zimmer {room.room_no}: {room.room_type} - {room.room_price}€ pro Nacht")
            else:
                print("Keine Zimmer verfügbar.")
        
        elif choice == "2":
            name = input("Name des Gasts: ")
            age = input("Alter des Gasts: ")
            phone = input("Telefonnummer: ")
            guest = Guest(name, age, phone)
            room_no = int(input("Zimmernummer: "))
            check_in = input("Check-in Datum (YYYY-MM-DD): ")
            check_out = input("Check-out Datum (YYYY-MM-DD): ")
            room = next((r for r in hotel.rooms if r.room_no == room_no), None)
            if room:
                booking = hotel.book_room(room, guest, check_in, check_out)
                if isinstance(booking, Booking):
                    print("Buchung erfolgreich!")
                else:
                    print("Zimmer nicht verfügbar!")
            else:
                print("Ungültige Zimmernummer!")
        
        elif choice == "3":
            bookings = hotel.get_bookings()
            if bookings:
                for booking in bookings:
                    details = booking.get_booking_details()
                    print(details)
            else:
                print("Keine Buchungen vorhanden.")
        
        elif choice == "4":
            room_no = int(input("Zimmernummer der Buchung: "))
            room = next((r for r in hotel.rooms if r.room_no == room_no), None)
            if room:
                booking = hotel.get_booking_by_room(room)
                if isinstance(booking, Booking):
                    hotel.cancle_booking(booking)
                    print("Buchung storniert.")
                else:
                    print("Keine Buchung gefunden!")
            else:
                print("Ungültige Zimmernummer!")
        
        elif choice == "5":
            room_no = int(input("Zimmernummer für Checkout: "))
            room = next((r for r in hotel.rooms if r.room_no == room_no), None)
            if room:
                booking = hotel.get_booking_by_room(room)
                if isinstance(booking, Booking):
                    hotel.checkout(booking)
                    print("Checkout erfolgreich!")
                else:
                    print("Keine Buchung gefunden!")
            else:
                print("Ungültige Zimmernummer!")
        
        elif choice == "6":
            details = hotel.get_hotel_details()
            print(details)
        
        elif choice == "7":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte erneut versuchen.")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)




