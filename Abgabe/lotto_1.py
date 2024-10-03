import random

min = 1   #der minimale Wert der gezogen werden kann
max = 45 #der maximale Wert der gezogen werden kann
# in diesem Beispiel machen wir das Oesterreichische Lotto 6 aus 45 
# In Deutschland ist es 6 aus 49 dann müssten wir min auf 1 und max auf 49 setzen


#In dieser 
def lotto_ziehung(x):
    lotto_zahlen = []
    available_numbers = list(range(min, max+1)) #unser pool an verfügbaren Zahlen
    for _ in range(x):
        ranzahl = available_numbers[random.randint(0, len(available_numbers)-1)] #Zufällige Zahl aus dem Pool ziehen die len(available_numbers) - 1 gibt die länge des Pools an der verkleinert wird
        available_numbers.remove(ranzahl)   #die gezogene Zahl wird aus dem Pool entfernt und kann daher nicht nochmal gezogen werden
        lotto_zahlen.append(ranzahl)       #die gezogene Zahl wird der Lotte Liste hinzugefügt

    return lotto_zahlen

groeße_ziehung = 6
print("Hier sin die Lottozahlen:")
gezoogene_zahlen = lotto_ziehung(groeße_ziehung)
print(end="| ")
for i in gezoogene_zahlen:
    print(i, end=" | ")
