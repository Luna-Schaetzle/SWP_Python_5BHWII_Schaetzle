import random
from collections import Counter

# Definiere Farben und Kartentypen
farben = ['Kreuz', 'Pik', 'Herz', 'Karo']
karten_typen = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']

# Wir machen ein Dictionary in dem wir speichern, wie oft eine der Möglichkeiten vorgekommen ist
kombinationen_zaehler = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two Pair": 0,
    "One Pair": 0,
    "High Card": 0
}

ziehungen = 1000000
handgroeße = 5

# Erstelle ein Deck mit allen Karten
def deck_reset():
    return [(farbe, kartentyp) for farbe in farben for kartentyp in karten_typen]

# Funktion, um eine Karte zu ziehen und aus dem Deck zu entfernen
def ziehe_karte(deck):
    gezogene_karte = random.choice(deck)
    deck.remove(gezogene_karte)
    return gezogene_karte

# Funktion, um eine Hand zu ziehen
def draw_hand(deck):
    return [ziehe_karte(deck) for _ in range(handgroeße)]

# Funktion, um die Kartentypen den richtigen Wert zuzuordnen
def set_rang(karte):
    order_rang = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'Bube': 9, 'Dame': 10, 'König': 11, 'Ass': 12}
    return order_rang[karte]

# Funktion, um die Hand nach den Rängen zu sortieren
def set_order(hand):
    return sorted(hand, key=lambda karte: set_rang(karte[1]))

# Funktion, um eine Royal Flush zu überprüfen
def royal_flush(hand):
    reihenfolge_royal_flush = ['10', 'Bube', 'Dame', 'König', 'Ass']
    farben_in_hand = [karte[0] for karte in hand]
    karten_in_hand = [karte[1] for karte in hand]
    return len(set(farben_in_hand)) == 1 and all(typ in karten_in_hand for typ in reihenfolge_royal_flush)

# Funktion, um Pokerkombinationen zu erkennen
def kombination_bestimmen(hand):
    farben_in_hand = [karte[0] for karte in hand]
    karten_in_hand = [karte[1] for karte in hand]
    karten_counter = Counter(karten_in_hand)
    
    geordnete_hand = set_order(hand)
    geordnete_werte = [set_rang(karte[1]) for karte in geordnete_hand]
    
    # Royal Flush
    if royal_flush(hand):
        return "Royal Flush"

    # Straight Flush
    if len(set(farben_in_hand)) == 1 and geordnete_werte == list(range(geordnete_werte[0], geordnete_werte[0] + 5)):
        return "Straight Flush"
    
    # Four of a Kind
    if 4 in karten_counter.values():
        return "Four of a Kind"

    # Full House
    if 2 in karten_counter.values() and 3 in karten_counter.values():
        return "Full House"

    # Flush
    if len(set(farben_in_hand)) == 1:
        return "Flush"

    # Straight
    if geordnete_werte == list(range(geordnete_werte[0], geordnete_werte[0] + 5)):
        return "Straight"

    # Three of a Kind
    if 3 in karten_counter.values():
        return "Three of a Kind"

    # Two Pair
    if list(karten_counter.values()).count(2) == 2:
        return "Two Pair"

    # One Pair
    if 2 in karten_counter.values():
        return "One Pair"

    # High Card
    return "High Card"

# Erhebung der Statistik
def statistik_erheben():
    for _ in range(ziehungen):
        deck = deck_reset()
        hand = draw_hand(deck)
        kombination = kombination_bestimmen(hand)
        kombinationen_zaehler[kombination] += 1

    # Ausgabe der Ergebnisse
    for kombination, anzahl in kombinationen_zaehler.items():
        print(f"{kombination}: {anzahl} ({anzahl/ziehungen*100:.9f}%)")

# Hauptfunktion zum Ausführen des Tests
if __name__ == "__main__":
    statistik_erheben()
    print("Ziehungen:", ziehungen)
