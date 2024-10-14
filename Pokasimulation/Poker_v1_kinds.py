# Texas hold'em verschiedene arten der kombinationen
# - **Royal Flush**: 10, J, Q, K, A einer Farbe.
# - **Straight Flush**: Fünf aufeinanderfolgende Karten derselben Farbe.
# - **Four of a Kind**: Vier gleiche Karten.
# - **Full House**: Drilling und ein Paar.
# - **Flush**: Fünf beliebige Karten derselben Farbe.
# - **Straight**: Fünf aufeinanderfolgende Karten verschiedener Farben.
# - **Three of a Kind**: Drei gleiche Karten.
# - **Two Pair**: Zwei Paare.
# - **One Pair**: Ein Paar.
# - **High Card**: Höchste Karte entscheidet. 


import random 
import numpy as np
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
    
    # Ziehe eine zufällige Karte aus dem Deck
    gezogene_karte = random.choice(deck)
    deck.remove(gezogene_karte)  # Entferne die gezogene Karte aus dem Deck
    
    return gezogene_karte


# Funktion, um eine Hand zu ziehen
def draw_hand(deck):
    return [ziehe_karte(deck) for _ in range(5)]

# funktion für Royal Flush
def royal_flush(karten_in_hand):
    reihenfolge_royal_flush = ['10', 'Bube', 'Dame', 'König', 'Ass']
    #Sortieren der Karten in der Hand 
    return all(typ in karten_in_hand for typ in reihenfolge_royal_flush)

# Funktion um die Kartentypen den richtigen wert zuteilt
def set_rang(karte):
    # dictionariy um zu definieren wie viel jede karte wert ist bzw. welchen rang sie haben 
    order_rang = {'2' : 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'Bube': 9, 'Dame': 10, 'König': 11, 'Ass': 12}
    return order_rang[karte]

# Funktion die die hand in die richtigen Reihenfolge 
def set_order(karten_hand):
    # Sortiere die Karten in der Hand basierend auf ihrem Rang
    return sorted(karten_hand, key=lambda karte: set_rang(karte[1]))


# Funktion, um Pokerkombinationen zu erkennen
def kombination_bestimmen(hand):
    # Aufteilen in Farben und karten da sie im Deck Kommbiniert sind -> einfacher kombinationen zu erkennen wenn man auteilt
    farben_in_hand = [karte[0] for karte in hand]
    karten_in_hand = [karte[1] for karte in hand] # Farben und Kartentypen extrahieren

    farben_counter = Counter(farben_in_hand)
    karten_counter = Counter(karten_in_hand)

    # Flush
    if farben_counter == 1:
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
    # Sortiere die Karten in der Hand basierend auf ihrem Rang
    geordnete_werte = [set_rang(karte[1]) for karte in hand]
    geordnete_hand = set_order(geordnete_werte)
    
    # Überprüfe, ob die Karten aufeinanderfolgend sind
    if geordnete_hand == list(range(geordnete_hand[0], geordnete_hand[0] + 5)):
        return "Straight"
    
    # Straight Flush
    if farben_counter == 1 and "Straight" in kombination_bestimmen(hand): # funktioniert in dem man die funktion einfach nochmal aufruft und testet ob die kombination Straight ist
        return "Straight Flush"
    
    # Full House kombination von drilling und paar
    if 2 in karten_counter.values() and 3 in karten_counter.values():
        return "Full House"
    # Royal Flush
    if farben_counter == 1 and royal_flush() == True:
        return "Royal Flush"

    # High Card
    return "High Card: " + max(hand, key=lambda x: karten_typen.index(x[1]))[1]


# Hauptfunktion zum Ausführen des Tests
if __name__ == "__main__":
    deck = deck_reset()
    gezogene_hand = draw_hand(deck)
    print("Gezogene Hand:", gezogene_hand)
    print("Kombination:", kombination_bestimmen(gezogene_hand))

