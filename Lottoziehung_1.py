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

print("Hier sin die Lottozahlen:")
gezoogene_zahlen = lotto_ziehung(6)
print(end="| ")
for i in gezoogene_zahlen:
    print(i, end=" | ")
