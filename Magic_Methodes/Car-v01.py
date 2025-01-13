"""
AUFGBE:

- Magic methods

- len(a) = a.__len__()

- Auto Klasse erzeugen
- PS als attribut vergeben
- wenn a1 50PS hat und a2 60PS und a1+a2 rechnet soll direkt 110 ausgegeben werden
- subtraktion und multiplikation soll auf den auto-objekten möglich sein
- achtung überprüfen ob geegnete objekte addiert, subtrahiert usw. werden
- EQ,LT,GT vergleichsoperationen abbilden
- für alle magicmethods testzeilen angeben
"""

import sys

class Car: 
    def __init__(self, ps):
        self.ps = ps

    def __len__(self):
        return self.ps

    def __add__(self, other):
        return self.ps + other.ps

    def __sub__(self, other):
        return self.ps - other.ps

    def __mul__(self, other):
        return self.ps * other.ps

    def __eq__(self, other):
        return self.ps == other.ps

    def __lt__(self, other):
        return self.ps < other.ps

    def __gt__(self, other):
        return self.ps > other.ps


def main():
    a1 = Car(50)
    a2 = Car(60)

    print("Testzeilen für Magic Methods in Car Klasse")
    print("-------------------------------------------")
    print("len(a) = a.__len__()")
    print(len(a1))
    print(len(a2))

    print("\na1 + a2")
    print(a1 + a2)

    print("\na1 - a2")
    print(a1 - a2)

    print("\na1 * a2")
    print(a1 * a2)

    print("\nEQ,LT,GT vergleichsoperationen abbilden")
    print("---------------------------------------")
    print("a1 == a2")
    print(a1 == a2)
    print("\na1 != a2")
    print(a1 != a2)
    print("\na1 < a2")
    print(a1 < a2)
    print("\na1 > a2")
    print(a1 > a2)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

