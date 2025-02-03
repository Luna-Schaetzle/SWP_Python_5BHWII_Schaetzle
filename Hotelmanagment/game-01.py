import sys
import random

class Room:
    def __init__(self, room_no, room_type, room_price, room_status):
        self.room_no = room_no
        self.room_type = room_type
        self.room_price = room_price
        self.room_status = room_status

    def get_room_status(self):
        return self.room_status
    
    def get_room_type(self):
        return self.room_type

    def get_room_price(self):
        return self.room_price

class Guest:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

class Booking:
    def __init__(self, room, guest, check_in_day, check_out_day):
        self.room = room
        self.guest = guest
        self.check_in_day = check_in_day
        self.check_out_day = check_out_day

    def get_booking_details(self):
        return {
            'Room No': self.room.room_no,
            'Room Type': self.room.room_type,
            'Nights': self.check_out_day - self.check_in_day,
            'Guest Name': self.guest.name,
            'Check In Day': self.check_in_day,
            'Check Out Day': self.check_out_day
        }

class Hotel:
    def __init__(self, name, rooms, initial_balance):
        self.name = name
        self.rooms = rooms
        self.bookings = []
        self.balance = initial_balance
        self.current_day = 1
        self.reputation = 50
        self.staff = []
        self.maintenance_cost_per_room = 10

    def get_daily_costs(self):
        staff_cost = len(self.staff) * 50
        maintenance_cost = len(self.rooms) * self.maintenance_cost_per_room
        return staff_cost + maintenance_cost

    def get_available_rooms(self, check_in_day, check_out_day):
        available_rooms = []
        for room in self.rooms:
            if room.get_room_status() == 'Available':
                if self.is_room_available(room, check_in_day, check_out_day):
                    available_rooms.append(room)
        return available_rooms

    def is_room_available(self, room, check_in, check_out):
        for booking in self.bookings:
            if booking.room == room:
                if (check_in < booking.check_out_day) and (check_out > booking.check_in_day):
                    return False
        return True

    def book_room(self, room, guest, check_in, check_out):
        if self.is_room_available(room, check_in, check_out):
            booking = Booking(room, guest, check_in, check_out)
            self.bookings.append(booking)
            return booking
        return None

    def process_day(self):
        # Einnahmen berechnen
        for booking in self.bookings:
            if booking.check_in_day <= self.current_day < booking.check_out_day:
                self.balance += booking.room.room_price
        
        # Kosten abziehen
        daily_costs = self.get_daily_costs()
        self.balance -= daily_costs
        
        # Zufallsereignisse
        self.handle_random_events()
        
        # Ruf aktualisieren
        self.update_reputation()
        
        self.current_day += 1

    def handle_random_events(self):
        if random.randint(1, 100) <= 20:
            event = random.choice(['VIP', 'maintenance', 'compliment', 'complaint'])
            
            if event == 'VIP':
                suites = [r for r in self.rooms if r.room_type == 'Suite']
                if suites and self.is_room_available(suites[0], self.current_day, self.current_day+1):
                    print("\n🌟 VIP-Gast möchte eine Suite buchen! (Doppelte Einnahmen)")
                    if input("Annehmen? (j/n): ").lower() == 'j':
                        guest = Guest("VIP Gast", 45, "000-000000")
                        self.book_room(suites[0], guest, self.current_day, self.current_day+1)
                        self.balance += suites[0].room_price
                        self.reputation += 5
            
            elif event == 'maintenance':
                room = random.choice(self.rooms)
                room.room_status = 'Not Available'
                cost = random.randint(50, 200)
                self.balance -= cost
                print(f"\n🔧 Raum {room.room_no} benötigt Wartung! Kosten: €{cost}")
            
            elif event == 'compliment':
                print("\n😊 Ein Gast lobt den ausgezeichneten Service!")
                self.reputation += 10
            
            elif event == 'complaint':
                print("\n😡 Ein Gast beschwert sich über schmutzige Zimmer!")
                self.reputation -= 10
            
            self.reputation = max(0, min(100, self.reputation))

    def update_reputation(self):
        occupancy = len(self.bookings) / len(self.rooms)
        self.reputation += int(occupancy * 5) - 2
        self.reputation = max(0, min(100, self.reputation))

def main():
    # Initialisierung
    rooms = [
        Room(101, "Single", 50, "Available"),
        Room(102, "Double", 80, "Available"),
        Room(103, "Suite", 150, "Available")
    ]
    hotel = Hotel("Grand Hotel", rooms, initial_balance=2000)
    
    while True:
        print(f"\n--- Tag {hotel.current_day} ---")
        print(f"💰 Kontostand: €{hotel.balance}")
        print(f"📈 Ruf: {hotel.reputation}/100")
        print("1. Zimmer anzeigen")
        print("2. Zimmer buchen")
        print("3. Preise ändern")
        print("4. Zimmer upgraden")
        print("5. Personal einstellen")
        print("6. Nächsten Tag verarbeiten")
        print("7. Beenden")
        
        choice = input("Auswahl: ")
        
        if choice == "1":
            available = hotel.get_available_rooms(hotel.current_day, hotel.current_day+1)
            print("\nVerfügbare Zimmer:")
            for r in available:
                status = "🟢" if r.room_status == "Available" else "🔴"
                print(f"{status} Zimmer {r.room_no} ({r.room_type}): €{r.room_price}/Nacht")

        elif choice == "2":
            name = input("Gastname: ")
            age = input("Alter: ")
            phone = input("Telefon: ")
            guest = Guest(name, age, phone)
            
            available = hotel.get_available_rooms(hotel.current_day, hotel.current_day+1)
            for i, r in enumerate(available):
                print(f"{i+1}. Zimmer {r.room_no} ({r.room_type})")
            
            try:
                room_idx = int(input("Zimmernummer: "))-1
                nights = int(input("Nächte: "))
                room = available[room_idx]
                
                booking = hotel.book_room(room, guest, hotel.current_day, hotel.current_day+nights)
                if booking:
                    print(f"✅ Buchung erfolgreich für {nights} Nächte!")
                else:
                    print("❌ Zimmer nicht verfügbar!")
            except:
                print("❌ Ungültige Eingabe!")

        elif choice == "3":
            for r in hotel.rooms:
                print(f"Zimmer {r.room_no} ({r.room_type}): Aktuell €{r.room_price}")
            room_no = int(input("Zimmernummer: "))
            new_price = int(input("Neuer Preis: "))
            for r in hotel.rooms:
                if r.room_no == room_no:
                    r.room_price = new_price
                    print("✅ Preis aktualisiert!")
                    break

        elif choice == "4":
            print("Zimmer upgraden (Kosten: Single €200, Double €300, Suite €500)")
            for r in hotel.rooms:
                print(f"Zimmer {r.room_no}: {r.room_type}")
            room_no = int(input("Zimmernummer: "))
            new_type = input("Neuer Typ (Single/Double/Suite): ").capitalize()
            
            cost = 200 if new_type == "Single" else 300 if new_type == "Double" else 500
            if hotel.balance >= cost:
                for r in hotel.rooms:
                    if r.room_no == room_no:
                        r.room_type = new_type
                        r.room_price = {"Single":50, "Double":80, "Suite":150}[new_type]
                        hotel.balance -= cost
                        print("✅ Upgrade erfolgreich!")
                        break
            else:
                print("❌ Nicht genug Geld!")

        elif choice == "5":
            cost = 50
            print(f"Personal einstellen (€{cost}/Tag pro Person)")
            if input("Einstellen? (j/n): ").lower() == 'j':
                hotel.staff.append("Mitarbeiter")
                print(f"👨💼 Aktuelle Mitarbeiter: {len(hotel.staff)}")

        elif choice == "6":
            hotel.process_day()
            print("\n=== Tageszusammenfassung ===")
            print(f"Einnahmen: €{sum(r.room_price for r in hotel.rooms if any(b.room == r for b in hotel.bookings))}")
            print(f"Kosten: €{hotel.get_daily_costs()}")
            if hotel.balance <= 0:
                print("❌ GAME OVER - Kein Geld mehr!")
                return

        elif choice == "7":
            print("Auf Wiedersehen!")
            break

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Fehler: {e}")
        sys.exit(1)