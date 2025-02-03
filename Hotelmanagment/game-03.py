import sys
import random
import json  # NEU: Für das Speichern und Laden des Spiels
from faker import Faker  # NEU: Für die Generierung zufälliger Gästedaten

fake = Faker()  # NEU: Initialisierung von Faker

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
        self.guest_queue = []  # NEU: Gästeschlange
        self.income = 0  # NEU: Einnahmen
        self.expenses = 0  # NEU: Ausgaben

    def get_daily_costs(self):
        staff_cost = len(self.staff) * 50
        maintenance_cost = len(self.rooms) * self.maintenance_cost_per_room
        return staff_cost + maintenance_cost

    def get_available_rooms(self, check_in_day, check_out_day, room_type=None):
        """
        Gibt alle verfügbaren Zimmer zurück. Optional kann room_type angegeben werden,
        um nur bestimmte Zimmertypen zu filtern.
        """
        available_rooms = []
        for room in self.rooms:
            if room.get_room_status() == 'Available':
                if self.is_room_available(room, check_in_day, check_out_day):
                    if room_type is None or room.room_type == room_type:
                        available_rooms.append(room)
        return available_rooms

    def is_room_available(self, room, check_in, check_out):
        for booking in self.bookings:
            if booking.room == room:
                # Überschneidet sich der Zeitraum?
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
        daily_income = 0  # NEU: Tageseinnahmen
        for booking in self.bookings:
            # Wenn der Gast in diesem Zimmer übernachtet (aktueller Tag liegt im Buchungszeitraum)
            if booking.check_in_day <= self.current_day < booking.check_out_day:
                daily_income += booking.room.room_price
        self.balance += daily_income
        self.income += daily_income  # NEU: Gesamt einnahmen aktualisieren

        # Tägliche Kosten abziehen
        daily_costs = self.get_daily_costs()
        self.balance -= daily_costs
        self.expenses += daily_costs  # NEU: Gesamt Ausgaben aktualisieren

        # Zufallsereignisse und neue Gäste
        self.handle_random_events()

        # Gästeschlange verarbeiten (optional, je nach Design)
        # self.process_guest_queue()  # NEU: Gästeschlange verarbeiten (kann deaktiviert werden)

        # Ruf aktualisieren
        self.update_reputation()

        # Zum nächsten Tag
        self.current_day += 1

    def handle_random_events(self):
        # Mit 20% Wahrscheinlichkeit tritt ein Ereignis auf
        if random.randint(1, 100) <= 20:
            # NEU: Füge 'new_guest_event' als mögliches Ereignis hinzu
            event = random.choice(['VIP', 'maintenance', 'compliment', 'complaint', 'new_guest_event'])
            
            if event == 'VIP':
                suites = [r for r in self.rooms if r.room_type == 'Suite' and r.room_status == 'Available']
                if suites and self.is_room_available(suites[0], self.current_day, self.current_day+1):
                    print("\n🌟 VIP-Gast möchte eine Suite buchen! (Doppelte Einnahmen)")
                    if input("Annehmen? (j/n): ").lower() == 'j':
                        guest = Guest("VIP Gast", 45, "000-000000")
                        booking = self.book_room(suites[0], guest, self.current_day, self.current_day+1)
                        if booking:
                            # VIP zahlt doppelt
                            self.balance += suites[0].room_price
                            self.income += suites[0].room_price  # NEU: Zusätzliche Einnahmen
                            self.reputation += 5

            elif event == 'maintenance':
                # Zufälliges Zimmer belegen
                room = random.choice(self.rooms)
                room.room_status = 'Not Available'
                cost = random.randint(50, 200)
                self.balance -= cost
                self.expenses += cost  # NEU: Zusätzliche Ausgaben
                print(f"\n🔧 Raum {room.room_no} benötigt Wartung! Kosten: €{cost}")

            elif event == 'compliment':
                print("\n😊 Ein Gast lobt den ausgezeichneten Service!")
                self.reputation += 10

            elif event == 'complaint':
                print("\n😡 Ein Gast beschwert sich über schmutzige Zimmer!")
                self.reputation -= 10

            # NEU: Zusätzliche Ereignisse
            elif event == 'new_guest_event':
                # Ein neuer Gast möchte buchen und wird der Gästeschlange hinzugefügt
                requested_type = random.choice(['Single', 'Double', 'Suite'])
                requested_nights = random.randint(1, 5)
                # Generiere zufällige Gästedaten mit Faker
                guest_name = fake.name()
                guest_age = random.randint(18, 75)
                guest_phone = fake.phone_number()
                guest = Guest(guest_name, guest_age, guest_phone)
                print(f"\n🚪 Ein neuer Gast namens {guest.name} möchte ein {requested_type}-Zimmer für {requested_nights} Nacht/Nächte buchen.")
                self.guest_queue.append((guest, requested_type, requested_nights))
            
            # Reputation in Grenzen halten
            self.reputation = max(0, min(100, self.reputation))

    def process_guest_queue(self):  # NEU
        if self.guest_queue:
            print("\n📋 Gästeschlange:")
            for idx, (guest, room_type, nights) in enumerate(self.guest_queue, start=1):
                print(f"{idx}. {guest.name}, Alter: {guest.age}, Telefon: {guest.phone_no} möchte ein {room_type}-Zimmer für {nights} Nacht/Nächte.")
            
            while True:
                try:
                    choice = input("\nMöchtest du eine Buchungsanfrage bearbeiten? (j/n): ").lower()
                    if choice == 'j':
                        guest_idx = int(input("Gib die Nummer des Gastes ein, den du bearbeiten möchtest: ")) - 1
                        if 0 <= guest_idx < len(self.guest_queue):
                            guest, room_type, nights = self.guest_queue.pop(guest_idx)
                            available_rooms = self.get_available_rooms(self.current_day, self.current_day + nights, room_type)
                            if available_rooms:
                                print(f"\n📋 Buchungsanfrage von {guest.name}: {room_type}-Zimmer für {nights} Nacht/Nächte.")
                                decision = input("Annehmen? (j/n): ").lower()
                                if decision == 'j':
                                    booking = self.book_room(available_rooms[0], guest, self.current_day, self.current_day + nights)
                                    if booking:
                                        print("✅ Buchung angenommen!")
                                        self.reputation += 1
                                else:
                                    print(f"❌ Buchungsanfrage von {guest.name} abgelehnt.")
                                    self.reputation -= 1
                            else:
                                print(f"\n📋 Buchungsanfrage von {guest.name}: Kein {room_type}-Zimmer verfügbar. Buchung abgelehnt.")
                                self.reputation -= 2
                        else:
                            print("❌ Ungültige Nummer!")
                    elif choice == 'n':
                        break
                    else:
                        print("❌ Ungültige Eingabe!")
                except ValueError:
                    print("❌ Ungültige Eingabe!")

    def update_reputation(self):
        # Auf Basis der Auslastung Reputation anpassen
        # (Sehr einfache Logik: pro belegtem Zimmer ein kleiner Bonus, fester Malus)
        occupancy = self.get_occupancy_rate()
        self.reputation += int(occupancy * 5) - 2
        self.reputation = max(0, min(100, self.reputation))

    def get_occupancy_rate(self):
        """
        Aktuelle Auslastung am heutigen Tag (Anteil gebuchter Zimmer).
        Da Buchungen über mehrere Tage laufen können, zählen wir,
        wie viele Zimmer am current_day belegt sind.
        """
        occupied = 0
        for room in self.rooms:
            for booking in self.bookings:
                if booking.room == room and (booking.check_in_day <= self.current_day < booking.check_out_day):
                    occupied += 1
                    break
        if len(self.rooms) == 0:
            return 0
        return occupied / len(self.rooms)

    # NEU: Methoden zum Speichern und Laden des Spiels
    def save_game(self, filename="hotel_save.json"):
        data = {
            'name': self.name,
            'rooms': [{'room_no': r.room_no, 'room_type': r.room_type, 'room_price': r.room_price, 'room_status': r.room_status} for r in self.rooms],
            'bookings': [{'room_no': b.room.room_no, 'guest_name': b.guest.name, 'guest_age': b.guest.age, 'guest_phone': b.guest.phone_no,
                          'check_in_day': b.check_in_day, 'check_out_day': b.check_out_day} for b in self.bookings],
            'balance': self.balance,
            'current_day': self.current_day,
            'reputation': self.reputation,
            'staff': self.staff,
            'income': self.income,
            'expenses': self.expenses,
            'guest_queue': [{'name': g.name, 'age': g.age, 'phone_no': g.phone_no, 'room_type': rt, 'nights': n} for (g, rt, n) in self.guest_queue]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"💾 Spiel gespeichert unter '{filename}'.")

    @staticmethod
    def load_game(filename="hotel_save.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            rooms = [Room(r['room_no'], r['room_type'], r['room_price'], r['room_status']) for r in data['rooms']]
            hotel = Hotel(data['name'], rooms, data['balance'])
            hotel.current_day = data['current_day']
            hotel.reputation = data['reputation']
            hotel.staff = data['staff']
            hotel.income = data['income']
            hotel.expenses = data['expenses']
            for b in data['bookings']:
                room = next((room for room in rooms if room.room_no == b['room_no']), None)
                if room:
                    guest = Guest(b['guest_name'], b['guest_age'], b['guest_phone'])
                    booking = Booking(room, guest, b['check_in_day'], b['check_out_day'])
                    hotel.bookings.append(booking)
            for g in data['guest_queue']:
                guest = Guest(g['name'], g['age'], g['phone_no'])
                hotel.guest_queue.append((guest, g['room_type'], g['nights']))
            print(f"📂 Spiel geladen von '{filename}'.")
            return hotel
        except FileNotFoundError:
            print(f"❌ Datei '{filename}' nicht gefunden. Ein neues Spiel wird gestartet.")
            return None
        except Exception as e:
            print(f"❌ Fehler beim Laden des Spiels: {e}")
            return None

def main():
    print("🏨 Willkommen zum Hotel Management Spiel!")
    print("1. Neues Spiel starten")
    print("2. Spiel laden")
    choice = input("Auswahl: ")

    if choice == "1":
        # Initialisierung
        rooms = [
            Room(101, "Single", 50, "Available"),
            Room(102, "Double", 80, "Available"),
            Room(103, "Suite", 150, "Available")
        ]
        hotel = Hotel("Grand Hotel", rooms, initial_balance=2000)
    elif choice == "2":
        hotel = Hotel.load_game()
        if not hotel:
            # Falls Laden fehlgeschlagen, starte ein neues Spiel
            rooms = [
                Room(101, "Single", 50, "Available"),
                Room(102, "Double", 80, "Available"),
                Room(103, "Suite", 150, "Available")
            ]
            hotel = Hotel("Grand Hotel", rooms, initial_balance=2000)
    else:
        print("❌ Ungültige Auswahl!")
        return

    while True:
        print(f"\n--- Tag {hotel.current_day} ---")
        print(f"💰 Kontostand: €{hotel.balance}")
        print(f"📈 Ruf: {hotel.reputation}/100")
        print(f"💼 Mitarbeiter: {len(hotel.staff)}")
        print("1. Zimmer anzeigen")
        print("2. Zimmer buchen")
        print("3. Preise ändern")
        print("4. Zimmer upgraden")
        print("5. Personal einstellen")
        print("6. Nächsten Tag verarbeiten")
        print("7. Hotel erweitern (neue Zimmer kaufen)")
        print("8. Spiel speichern")
        print("9. Spiel laden")
        print("10. Gästeschlange anzeigen und bearbeiten")  # NEU: Menüpunkt zur Gästeschlange
        print("11. Beenden")
        
        choice = input("Auswahl: ")
        
        if choice == "1":
            available = hotel.get_available_rooms(hotel.current_day, hotel.current_day+1)
            print("\nVerfügbare Zimmer (für heute Nacht):")
            if not available:
                print("Keine Zimmer verfügbar.")
            for r in available:
                status = "🟢" if r.room_status == "Available" else "🔴"
                print(f"{status} Zimmer {r.room_no} ({r.room_type}): €{r.room_price}/Nacht")

        elif choice == "2":
            # Manuelles Buchen durch den Spieler
            name = input("Gastname: ")
            try:
                age = int(input("Alter: "))
            except ValueError:
                print("❌ Ungültiges Alter!")
                continue
            phone = input("Telefon: ")
            guest = Guest(name, age, phone)
            
            # Zimmer für den gewünschten Zeitraum
            # Hier vereinfachend: Wir gehen davon aus, dass ab heute gebucht wird
            available = hotel.get_available_rooms(hotel.current_day, hotel.current_day+1)
            if not available:
                print("Keine Zimmer verfügbar!")
                continue
            
            print("\nVerfügbare Zimmer:")
            for i, r in enumerate(available):
                print(f"{i+1}. Zimmer {r.room_no} ({r.room_type}) - €{r.room_price}/Nacht")
            
            try:
                room_idx = int(input("Bitte Zimmerauswahl eingeben (Index): "))-1
                nights = int(input("Nächte: "))
                if room_idx < 0 or room_idx >= len(available):
                    print("❌ Ungültiger Index!")
                    continue
                room = available[room_idx]
                
                booking = hotel.book_room(room, guest, hotel.current_day, hotel.current_day+nights)
                if booking:
                    print(f"✅ Buchung erfolgreich für {nights} Nächte!")
                else:
                    print("❌ Zimmer nicht verfügbar!")
            except ValueError:
                print("❌ Ungültige Eingabe!")
            except Exception as e:
                print(f"❌ Fehler: {e}")

        elif choice == "3":
            # Preise manuell ändern
            for r in hotel.rooms:
                print(f"Zimmer {r.room_no} ({r.room_type}): Aktuell €{r.room_price}")
            try:
                room_no = int(input("Zimmernummer, dessen Preis geändert werden soll: "))
                new_price = int(input("Neuer Preis: "))
                room_found = False
                for r in hotel.rooms:
                    if r.room_no == room_no:
                        r.room_price = new_price
                        print("✅ Preis aktualisiert!")
                        room_found = True
                        break
                if not room_found:
                    print("❌ Zimmernummer nicht gefunden!")
            except ValueError:
                print("❌ Ungültige Eingabe für Zimmernummer oder Preis!")

        elif choice == "4":
            # Zimmer upgraden
            print("Zimmer upgraden (Kosten: Single €200, Double €300, Suite €500)")
            for r in hotel.rooms:
                print(f"Zimmer {r.room_no}: {r.room_type} (aktueller Preis: €{r.room_price})")
            try:
                room_no = int(input("Zimmernummer: "))
                new_type = input("Neuer Typ (Single/Double/Suite): ").capitalize()
                
                if new_type not in ["Single", "Double", "Suite"]:
                    print("❌ Ungültiger Zimmertyp!")
                    continue
                
                cost_map = {"Single": 200, "Double": 300, "Suite": 500}
                price_map = {"Single": 50, "Double": 80, "Suite": 150}
                
                if new_type not in cost_map:
                    print("❌ Ungültiger Zimmertyp!")
                    continue

                cost = cost_map[new_type]
                if hotel.balance >= cost:
                    upgraded = False
                    for r in hotel.rooms:
                        if r.room_no == room_no:
                            r.room_type = new_type
                            r.room_price = price_map[new_type]
                            hotel.balance -= cost
                            hotel.expenses += cost  # NEU: Ausgaben aktualisieren
                            print("✅ Upgrade erfolgreich!")
                            upgraded = True
                            break
                    if not upgraded:
                        print("❌ Zimmernummer nicht gefunden!")
                else:
                    print("❌ Nicht genug Geld für ein Upgrade!")
            except ValueError:
                print("❌ Ungültige Eingabe!")
            except Exception as e:
                print(f"❌ Fehler: {e}")

        elif choice == "5":
            # Personal einstellen
            cost = 50
            print(f"Personal einstellen (Kostet täglich €{cost} pro Person).")
            if input("Einstellen? (j/n): ").lower() == 'j':
                hotel.staff.append("Mitarbeiter")
                print(f"👨💼 Aktuelle Anzahl Mitarbeiter: {len(hotel.staff)}")

        elif choice == "6":
            # Nächster Tag
            hotel.process_day()
            print("\n=== Tageszusammenfassung ===")
            print(f"Einnahmen heute: €{hotel.income - (hotel.income - (hotel.balance - hotel.expenses))}")
            print(f"Ausgaben heute: €{hotel.expenses}")
            print(f"Neuer Kontostand: €{hotel.balance}")
            print(f"Gesamteinnahmen: €{hotel.income}")
            print(f"Gesamtausgaben: €{hotel.expenses}")
            
            if hotel.balance <= 0:
                print("❌ GAME OVER - Kein Geld mehr!")
                break

        elif choice == "7":
            # ERWEITERUNG: Hotel (Zimmer) kaufen
            print("Hotel erweitern - neue Zimmer kaufen")
            print("Single-Zimmer = 1.000€, Double-Zimmer = 1.500€, Suite = 2.000€")
            new_type = input("Welchen Zimmertyp möchtest du hinzufügen? (Single/Double/Suite): ").capitalize()
            cost_map = {"Single": 1000, "Double": 1500, "Suite": 2000}
            price_map = {"Single": 50, "Double": 80, "Suite": 150}
            
            if new_type not in cost_map:
                print("❌ Ungültiger Zimmertyp!")
                continue
            
            try:
                anzahl = int(input("Wie viele Zimmer dieses Typs möchtest du bauen? "))
                if anzahl <= 0:
                    print("❌ Ungültige Anzahl!")
                    continue
            except ValueError:
                print("❌ Ungültige Eingabe für Anzahl!")
                continue
            
            total_cost = cost_map[new_type] * anzahl
            if hotel.balance >= total_cost:
                # Finde die aktuell höchste Zimmernummer
                max_room_no = max(r.room_no for r in hotel.rooms) if hotel.rooms else 100
                for i in range(1, anzahl+1):
                    new_room_no = max_room_no + i
                    # Füge neues Zimmer hinzu
                    new_room = Room(
                        room_no=new_room_no,
                        room_type=new_type,
                        room_price=price_map[new_type],
                        room_status="Available"
                    )
                    hotel.rooms.append(new_room)
                
                hotel.balance -= total_cost
                hotel.expenses += total_cost  # NEU: Ausgaben aktualisieren
                print(f"✅ {anzahl} neue '{new_type}'-Zimmer gebaut!")
            else:
                print("❌ Nicht genug Geld, um diese Zimmer zu bauen!")

        elif choice == "8":
            # NEU: Spiel speichern
            filename = input("Gib einen Dateinamen zum Speichern ein (z.B. 'mein_hotel_save.json'): ")
            hotel.save_game(filename)

        elif choice == "9":
            # NEU: Spiel laden
            filename = input("Gib den Dateinamen zum Laden ein (z.B. 'mein_hotel_save.json'): ")
            loaded_hotel = Hotel.load_game(filename)
            if loaded_hotel:
                hotel = loaded_hotel

        elif choice == "10":
            # NEU: Gästeschlange anzeigen und bearbeiten
            if not hotel.guest_queue:
                print("\n📋 Die Gästeschlange ist leer.")
            else:
                hotel.process_guest_queue()

        elif choice == "11":
            print("Auf Wiedersehen!")
            break

        else:
            print("❌ Ungültige Auswahl!")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Fehler: {e}")
        sys.exit(1)
