import random
from collections import Counter

# Definiere Farben und Kartentypen
farben = ['Kreuz', 'Pik', 'Herz', 'Karo']
karten_typen = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']

# Erstelle ein Deck mit allen Karten
def deck_reset():
    return [(farbe, kartentyp) for farbe in farben for kartentyp in karten_typen]

# Funktion, um eine Karte zu ziehen und aus dem Deck zu entfernen
def ziehe_karte(deck):
    if len(deck) == 0:
        raise ValueError("Keine Karten mehr im Deck!")
    gezogene_karte = random.choice(deck)
    deck.remove(gezogene_karte)
    return gezogene_karte

# Funktion, um eine Hand zu ziehen
def draw_hand(deck):
    return [ziehe_karte(deck) for _ in range(5)]

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
    # Aufteilen in Farben und karten da sie im Deck Kommbiniert sind -> einfacher kombinationen zu erkennen wenn man auteilt
    farben_in_hand = [karte[0] for karte in hand]
    karten_in_hand = [karte[1] for karte in hand]
    
    karten_counter = Counter(karten_in_hand) # zählt wie viele arten der karten in der hand es gibt

    # Flush
    if len(set(farben_in_hand)) == 1:
        return "Flush"

    # Four of a Kind
    if 4 in karten_counter.values():
        return "Four of a Kind"
    
    # Three of a Kind
    if 3 in karten_counter.values():
        return "Three of a Kind"
    
    # One Pair
    if 2 in karten_counter.values():
        return "One Pair"
    
    # Two Pair
    if list(karten_counter.values()).count(2) == 2:
        return "Two Pair"
    
    # Straight
    geordnete_hand = set_order(hand)
    geordnete_werte = [set_rang(karte[1]) for karte in geordnete_hand]
    if geordnete_werte == list(range(geordnete_werte[0], geordnete_werte[0] + 5)):
        return "Straight"
    
    # Straight Flush
    if len(set(farben_in_hand)) == 1 and geordnete_werte == list(range(geordnete_werte[0], geordnete_werte[0] + 5)):
        return "Straight Flush"
    
    # Full House
    if 2 in karten_counter.values() and 3 in karten_counter.values():
        return "Full House"

    # Royal Flush
    if royal_flush(hand):
        return "Royal Flush"

    # High Card
    return "High Card: " + max(hand, key=lambda x: set_rang(x[1]))[1]

# Hauptfunktion zum Ausführen des Tests
if __name__ == "__main__":
    deck = deck_reset()
    gezogene_hand = draw_hand(deck)
    print("Gezogene Hand:", gezogene_hand)
    print("Kombination:", kombination_bestimmen(gezogene_hand))
