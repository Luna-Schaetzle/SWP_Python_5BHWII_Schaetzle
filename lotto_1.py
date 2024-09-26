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


print("Hier sin die Lottozahlen:")
gezoogene_zahlen = lotto_ziehung(6)
print(end="| ")
for i in gezoogene_zahlen:
    print(i, end=" | ")
