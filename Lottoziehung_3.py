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

    def statistik(lotto_zahlen, statistik_dict):
        for zahl in lotto_zahlen:
            if zahl in statistik_dict:
                statistik_dict[zahl] += 1
            else:
                statistik_dict[zahl] = 1

    statistik_dict = {}

    for _ in range(1000):
        ziehung = lotto_ziehung(6)
        statistik(ziehung, statistik_dict)

    print(statistik_dict)