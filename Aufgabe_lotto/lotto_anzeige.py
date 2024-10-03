import random
import matplotlib.pyplot as plt

min = 1   #der minimale Wert der gezogen werden kann
max = 45 #der maximale Wert der gezogen werden kann
# in diesem Beispiel machen wir das Oesterreichische Lotto 6 aus 45 
# In Deutschland ist es 6 aus 49 dann müssten wir min auf 1 und max auf 49 setzen

name_of_file = "lotto_statistik_balkendiagramm.png"


# Anzahl der Ziehungen
ziehungen = 1000


#In dieser 
def lotto_ziehung(x):
    lotto_zahlen = []
    available_numbers = [i for i in range(min, max+1)] #unser pool an verfügbaren Zahlen
    for _ in range(x):  # Das _ ist ein Platzhalter für eine Variable die nicht verwendet wird
        ranzahl = available_numbers[random.randint(0, len(available_numbers)-1)] #Zufällige Zahl aus dem Pool ziehen die len(available_numbers) - 1 gibt die länge des Pools an der verkleinert wird
        available_numbers.remove(ranzahl)   #die gezogene Zahl wird aus dem Pool entfernt und kann daher nicht nochmal gezogen werden
        lotto_zahlen.append(ranzahl)       #die gezogene Zahl wird der Lotte Liste hinzugefügt

    return lotto_zahlen

# Statistik Funktion für die Ziehungen
def statisik_lotto(dict_lotto, ziehungen):
    for zahl in ziehungen:
        if zahl in dict_lotto:
            dict_lotto[zahl] += 1

# Main-Funktion
def main():
    # Initialisierung des Lotto-Statistik-Dictionaries
    dict_lotto = {i: 0 for i in range(min, max+1)} # von Copilot vorgeschlagen

    # Ziehungen durchführen
    for _ in range(ziehungen):
        statisik_lotto(dict_lotto, lotto_ziehung(6))

    # Erstellung des Balkendiagramms
    plt.figure(figsize=(10, 6))
    plt.bar(dict_lotto.keys(), dict_lotto.values(), color='skyblue')
    plt.xlabel('Lottozahlen')
    plt.ylabel('Anzahl der Ziehungen')
    plt.title('Lotto Statistik von ' + str(ziehungen) + ' Ziehungen')

    # Diagramm anzeigen und speichern
    plt.tight_layout()
    plt.savefig(name_of_file)
    plt.show()

if __name__ == "__main__":
    main()
