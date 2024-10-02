import random

#In dieser 
def lotto_ziehung(x):
    lotto_zahlen = []
    available_numbers = list(range(1, 46)) #unser pool an verfügbaren Zahlen
    for _ in range(x):
        ranzahl = available_numbers[random.randint(0, len(available_numbers)-1)] #Zufällige Zahl aus dem Pool ziehen die len(available_numbers) - 1 gibt die länge des Pools an der verkleinert wird
        available_numbers.remove(ranzahl)   #die gezogene Zahl wird aus dem Pool entfernt und kann daher nicht nochmal gezogen werden
        lotto_zahlen.append(ranzahl)       #die gezogene Zahl wird der Lotte Liste hinzugefügt

    return lotto_zahlen

def statisik_lotto(dict_lotto, ziehungen):
    for zahl in ziehungen:
        if zahl in dict_lotto:
            dict_lotto[zahl] += 1

dict_lotto = {}
for i in range(1, 46):
    dict_lotto[i] = 0

#hier machen wir nun die Ziehungen
ziehungen = 1000

for i in range(1, ziehungen):
    statisik_lotto(dict_lotto, lotto_ziehung(6))

#Ausgabe der Statistik
print("Statistik der Lottozahlen:")
for i in dict_lotto:
    print(f"Die Zahl {i} wurde {dict_lotto[i]} mal gezogen")
    print("")