import tkinter as tk
from tkinter import messagebox, ttk

class Room():
    def __init__(self, room_no, room_type, room_price, room_status="Available"):
        self.room_no = room_no
        self.room_type = room_type
        self.room_price = room_price
        self.room_status = room_status

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

class Hotel():
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.bookings = []

    def get_available_rooms(self):
        return [room for room in self.rooms if room.room_status == "Available"]

    def book_room(self, room_no, guest_name, guest_age, guest_phone, check_in_date, check_out_date):
        room = next((r for r in self.rooms if r.room_no == room_no and r.room_status == "Available"), None)
        if room:
            guest = Guest(guest_name, guest_age, guest_phone)
            booking = Booking(room, guest, check_in_date, check_out_date)
            self.bookings.append(booking)
            room.room_status = "Booked"
            return True
        return False

    def cancel_booking(self, room_no):
        booking = next((b for b in self.bookings if b.room.room_no == room_no), None)
        if booking:
            self.bookings.remove(booking)
            booking.room.room_status = "Available"
            return True
        return False

class HotelApp(tk.Tk):
    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.title("Hotel Management System")
        self.geometry("600x400")
        
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text=self.hotel.name, font=("Arial", 16)).pack(pady=10)
        
        ttk.Button(self, text="Verfügbare Zimmer anzeigen", command=self.show_available_rooms).pack(pady=5)
        ttk.Button(self, text="Zimmer buchen", command=self.book_room).pack(pady=5)
        ttk.Button(self, text="Buchung stornieren", command=self.cancel_booking).pack(pady=5)
        ttk.Button(self, text="Beenden", command=self.quit).pack(pady=5)

    def show_available_rooms(self):
        available_rooms = self.hotel.get_available_rooms()
        if available_rooms:
            message = "\n".join([f"Zimmer {r.room_no}: {r.room_type} - {r.room_price}€" for r in available_rooms])
            messagebox.showinfo("Verfügbare Zimmer", message)
        else:
            messagebox.showinfo("Verfügbare Zimmer", "Keine Zimmer verfügbar.")

    def book_room(self):
        booking_window = tk.Toplevel(self)
        booking_window.title("Zimmer buchen")
        booking_window.geometry("300x300")

        ttk.Label(booking_window, text="Zimmernummer").pack()
        room_no_entry = ttk.Entry(booking_window)
        room_no_entry.pack()

        ttk.Label(booking_window, text="Name des Gasts").pack()
        name_entry = ttk.Entry(booking_window)
        name_entry.pack()

        ttk.Label(booking_window, text="Alter des Gasts").pack()
        age_entry = ttk.Entry(booking_window)
        age_entry.pack()

        ttk.Label(booking_window, text="Telefonnummer").pack()
        phone_entry = ttk.Entry(booking_window)
        phone_entry.pack()

        ttk.Label(booking_window, text="Check-in Datum (YYYY-MM-DD)").pack()
        check_in_entry = ttk.Entry(booking_window)
        check_in_entry.pack()

        ttk.Label(booking_window, text="Check-out Datum (YYYY-MM-DD)").pack()
        check_out_entry = ttk.Entry(booking_window)
        check_out_entry.pack()

        def confirm_booking():
            try:
                room_no = int(room_no_entry.get())
                name = name_entry.get()
                age = int(age_entry.get())
                phone = phone_entry.get()
                check_in = check_in_entry.get()
                check_out = check_out_entry.get()
                success = self.hotel.book_room(room_no, name, age, phone, check_in, check_out)
                if success:
                    messagebox.showinfo("Erfolg", "Buchung erfolgreich!")
                    booking_window.destroy()
                else:
                    messagebox.showerror("Fehler", "Zimmer nicht verfügbar oder existiert nicht.")
            except ValueError:
                messagebox.showerror("Fehler", "Ungültige Eingabe")
        
        ttk.Button(booking_window, text="Buchen", command=confirm_booking).pack(pady=10)

    def cancel_booking(self):
        cancel_window = tk.Toplevel(self)
        cancel_window.title("Buchung stornieren")
        cancel_window.geometry("300x150")

        ttk.Label(cancel_window, text="Zimmernummer").pack()
        room_no_entry = ttk.Entry(cancel_window)
        room_no_entry.pack()

        def confirm_cancel():
            try:
                room_no = int(room_no_entry.get())
                success = self.hotel.cancel_booking(room_no)
                if success:
                    messagebox.showinfo("Erfolg", "Buchung storniert!")
                    cancel_window.destroy()
                else:
                    messagebox.showerror("Fehler", "Keine Buchung gefunden.")
            except ValueError:
                messagebox.showerror("Fehler", "Ungültige Eingabe")
        
        ttk.Button(cancel_window, text="Stornieren", command=confirm_cancel).pack(pady=10)

if __name__ == "__main__":
    rooms = [Room(101, "Single", 50), Room(102, "Double", 80), Room(103, "Suite", 150)]
    hotel = Hotel("Grand Plaza", rooms)
    app = HotelApp(hotel)
    app.mainloop()