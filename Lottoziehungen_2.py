import random

# generierung von x Zuffalszahlen zwischen 1 und 45 wobei jede Zahl nur einmal vorkommen darf
def lotto_ziehung(x):
    lotto_zahlen = []
    for i in range(x):
        ranzahl = random.randint(1, 45)
        while ranzahl in lotto_zahlen:
            ranzahl = random.randint(1, 45)
        lotto_zahlen.append(ranzahl)
    return lotto_zahlen


    # Generierung eines Dictionaries mit den Lottoziehungen
def generiere_lotto_dict(anzahl_ziehungen, anzahl_zahlen):
    lotto_dict = {}
    for i in range(anzahl_ziehungen):
        ziehung = lotto_ziehung(anzahl_zahlen)
        lotto_dict[f'Ziehung {i+1}'] = ziehung
    return lotto_dict

    # Beispielaufruf
anzahl_ziehungen = 100
anzahl_zahlen = 6
lotto_dict = generiere_lotto_dict(anzahl_ziehungen, anzahl_zahlen)
print(lotto_dict)