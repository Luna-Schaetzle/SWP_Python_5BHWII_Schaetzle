# Table of Contents
- [Einführung in Python](#einführung-in-python)
      - [Typisierung](#1-typisierung)
      - [Programmierparadigmen](#2-programmierparadigmen)
      - [Speicherverwaltung und Garbage Collection](#3-speicherverwaltung-und-garbage-collection)
      - [Speicherfreigabe](#4-speicherfreigabe)
   - [Wichtige Konzepte in Python](#wichtige-konzepte-in-python)
      - [Instanzen und Referenzen](#1-instanzen-und-referenzen)
      - [Schlüsselwort `del`](#2-schlüsselwort-del)
   - [Iteration und Rekursion](#iteration-und-rekursion)
      - [Iteration](#iteration)
      - [Rekursion](#rekursion)
   - [Unterschied zwischen Prozess und Thread](#unterschied-zwischen-prozess-und-thread)
      - [Prozess](#prozess)
      - [Thread](#thread)
   - [Array Lists](#array-lists)
      - [Arrays](#arrays)
      - [Listen](#listen)
      - [Linked Lists](#linked-lists)
      - [Array Lists](#array-lists-1)
   - [Dictionary](#dictionary)
      - [Dictionary Komprehension](#dictionary-komprehension)
   - [Array vertauschen](#array-vertauschen)
   - [Array einfach letztes Element heraussuchen](#array-einfach-letztes-element-heraussuchen)
   - [Array slicing](#array-slicing)
   - [Tupel](#tupel)
   - [Datentypen in Python](#datentypen-in-python)
      - [ganze Zahlen (int)](#ganze-zahlen-int)
      - [Division zweier ganzer Zahlen](#division-zweier-ganzer-zahlen)
      - [Floor Division in Python](#floor-division-in-python)
   - [Schlüsselwörter in Python](#schlüsselwörter-in-python)
   - [Tupel, range und set](#tupel-range-und-set)
      - [Tupel](#tupel-1)
      - [range](#range)
      - [set](#set)
   - [Auswertungsreihenfolge der Operatoren](#auswertungsreihenfolge-der-operatoren)
   - [Referenz / Instanz (bestehend aus Identität, Wert und Typ)](#referenz--instanz-bestehend-aus-identität-wert-und-typ)
      - [Identität](#identität)
      - [Problem des Seiten Effekts](#problem-des-seiten-effekts)
      - [Es ergibt sich folgendes](#es-ergibt-sich-folgendes)
   - [Unterschied zwischen Immutable und Mutable Datentypen](#unterschied-zwischen-immutable-und-mutable-datentypen)
      - [Immutable Datentypen](#immutable-datentypen)
      - [Mutable Datentypen](#mutable-datentypen)
   - [Laufzeitenmodell in Python](#laufzeitenmodell-in-python)
   - [Sequenzielle Datentypen Zusammenfassung](#sequenzielle-datentypen-zusammenfassung)
- [Aufgaben](#aufgaben)
   - [Erste Aufgabe: Lottoziehung](#erste-aufgabe-lottoziehung)
      - [Aufgabenstellung](#aufgabenstellung)
   - [Zweite Aufgabe: Pokerspielsimulator](#zweite-aufgabe-pokerspielsimulator)
      - [Aufgabenstellung](#aufgabenstellung-1)
      - [Kombinationen beim Poker](#kombinationen-beim-poker)
      - [Wahrscheinlichkeiten](#wahrscheinlichkeiten)

# Einführung in Python

## Eigenschaften von Python

### 1. Plattformunabhängigkeit

### 2. Interpretierte Sprache

### 3. Hochsprache

### 4. Bytecode in Python
- 
### 5. Standardbibliotheken und Module

### 6. Rapid Prototyping

## Unterschiede zwischen Python und Java

### 1. Typisierung
- **Dynamische Typisierung in Python:**  
  Python ist **dynamisch typisiert**, d.h. Variablen müssen beim Deklarieren keinen Datentyp erhalten. Der Interpreter weist den Typ zur Laufzeit zu.
  
  ```python
  x = 10  # x ist automatisch ein Integer
  x = "Hallo"  # x wird jetzt ein String
  ```
  
- **Statische Typisierung in Java:**  
  In Java müssen Datentypen explizit angegeben werden, was eine **statische Typisierung** darstellt.
  
  ```java
  int x = 10;
  ```

### 2. Programmierparadigmen
- **Python:** unterstützt sowohl **objektorientierte** als auch **funktionale Programmierung**. Man kann Funktionen als Parameter übergeben und mit rein funktionalen Konzepten arbeiten.
  
- **Java:** ist stark auf **objektorientierte Programmierung** ausgerichtet. In Java muss nahezu jede Funktionalität in Klassen verpackt werden.

### 3. Speicherverwaltung und Garbage Collection
- In Python wird die Speicherverwaltung größtenteils durch den Interpreter und die automatische **Garbage Collection** durchgeführt. Nicht mehr genutzte Objekte (Instanzen) werden gelöscht, sobald keine Referenzen mehr darauf existieren.
  - **Referenzzähler:** Python verwendet einen Zähler, der festhält, wie oft eine Instanz referenziert wird. Sinkt der Zähler auf null, wird die Instanz freigegeben und gelöscht.
  
  ```python
  del x  # Löscht die Referenz auf x
  ```

- Java verwendet ebenfalls **Garbage Collection**, allerdings mit einem komplexeren Speicherverwaltungssystem, das in der JVM integriert ist.

### 4. Speicherfreigabe
- **"Löschen" von Speicher:** In der Informatik kann Speicher nicht wirklich gelöscht, sondern nur **freigegeben** werden. Der freigegebene Speicherplatz kann dann später überschrieben werden.


## Wichtige Konzepte in Python

### 1. Instanzen und Referenzen


### 2. Schlüsselwort `del`
- Mit dem Schlüsselwort `del` kann man eine Instanz oder Referenz explizit löschen. Allerdings wird dabei nur die Referenz gelöscht, nicht das Objekt selbst, es sei denn, keine weiteren Referenzen zeigen mehr auf das Objekt.
- In Java gibt es kein direktes Äquivalent zu `del`, da die Speicherverwaltung automatisch durch die JVM erfolgt. Der sogenaannte **Garbage Collector** löscht nicht mehr benötigte Objekte automatisch.

**beispiel:**
```python
p1 = Person("Alice")  # Erstellt eine Instanz von Person
p2 = p1  # p2 zeigt auf die gleiche Instanz wie p1 somit sind p1 und p2 gleich 
         # deshalb koennen wir p1 nun loeschen
del p1  # Löscht die Referenz auf p1
```

### 3. Python interaktiver Modus

## Iteration und Rekursion

### Iteration

Iteration ist ein Konzept in der Informatik, bei dem ein Block von Code wiederholt ausgeführt wird, bis eine bestimmte Bedingung erfüllt ist. Iteration wird oft verwendet, um über Datenstrukturen wie Listen oder Arrays zu iterieren.

### Beispiel: Summe berechnen
Die Summe der Zahlen von `1` bis `n` kann iterativ wie folgt berechnet werden:

```python
def summe(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

print(summe(5))  # Ausgabe: 15
```

### Best Practices bei for-Schleifen

Wenn wir in einer for schleife die gesetze Variable nicht brauchen, dann können wir sie durch ein `_` ersetzen. Dies diehnt dazu um zu zeigen, dass die Variable nicht verwendet wird und das es schöner aussieht.

```python
for _ in range(5):
    print("Hallo") # Gibt "Hallo" 5 mal aus
```

### Rekursion

Rekursion ist ein Konzept in der Informatik, bei dem eine Funktion sich selbst aufruft, um ein Problem in kleinere Teilprobleme zu zerlegen. Rekursion ist ein leistungsstarkes Werkzeug, um komplexe Probleme auf elegante Weise zu lösen.

### Wichtig bei Rekursion

Eine Rekursion muss immer eine Abbruchbedingung haben, um eine Endlosschleife zu vermeiden. Ohne eine Abbruchbedingung würde die rekursive Funktion sich unendlich oft selbst aufrufen. Denn wenn wir keine Abbruchbedingung haben, dann stürzt das Programm garantiert ab. Da der Programmspeicher der für das Programm zugewiesen ist, irgendwann voll ist.

### Beispiel: Fakultät berechnen
Die Fakultät einer Zahl `n` (geschrieben als `n!`) ist das Produkt aller positiven ganzen Zahlen von `1` bis `n`. Die Fakultät einer Zahl `n` kann rekursiv wie folgt berechnet werden:

```python
def fakultaet(n):
    if n == 0:
        return 1
    else:
        return n * fakultaet(n - 1)

print(fakultaet(5))  # Ausgabe: 120
```
Der vorteil von Rekursion ist, dass es die Lesbarkeit des Codes erhöht. Der Nachteil ist, dass es zu einer hohen Speicherbelastung führen kann, da für jede rekursive Aufruf eine neue Instanz der Funktion im Speicher erstellt wird.

Der Compiler wandelt die Rekursion in eine iterative Schleife um, um den Speicher zu schonen.


## Unterschied zwischen Prozess und Thread
### Prozess
Ein Prozess ist ein Programm, wie zum Beispiel ein Texteditor oder ein Browser, aber auch Systemkomponenten wie die Tastatur. Prozesse sind voneinander isoliert und können von Haus aus nicht direkt miteinander kommunizieren.

### Thread
Ein Thread ist ein Bestandteil eines Prozesses. Ein Prozess kann mehrere Threads haben, die innerhalb desselben Prozesses agieren und miteinander kommunizieren können.


## Array Lists

Grundsätzlich gibt es nur zwei arten von Datenstrukturen und zwar die Arrays und die Listen. Alle anderen Datenstrukturen sind nur erweiterungen dieser beiden. 

### Arrays

Ein Array ist eine Datenstruktur, die eine Sammlung von Elementen speichert, die alle denselben Datentyp haben. Die Elemente eines Arrays sind über einen Index zugänglich, der die Position jedes Elements im Array angibt. Array haben eine feste Größe, die bei der Erstellung festgelegt wird und nicht geändert werden kann.

In Python sind Arrays nicht standardmäßig verfügbar, aber es gibt Bibliotheken wie `array`, die Arrays bereitstellen. Denn es ist in Python üblich, Listen zu verwenden, die flexibler sind als Arrays.

```python
from array import array

arr = array('i', [1, 2, 3, 4, 5])  # Erstellt ein Integer-Array
```

### Listen

Eine Liste ist eine Datenstruktur, die eine Sammlung von Elementen speichert, die nicht denselben Datentyp haben müssen. Listen sind flexibel und können dynamisch wachsen, d.h. Elemente können hinzugefügt oder entfernt werden, ohne die Größe der Liste explizit festzulegen.

In Python können Listen mit der `list`-Klasse erstellt werden.

```python
liste = [1, 2, 3, 4, 5]  # Erstellt eine Liste von Ganzzahlen
```

#### List komprehension

List Comprehension ist eine elegante Möglichkeit, Listen in Python zu erstellen. Es ermöglicht, Listen mit einer einzigen Zeile Code zu erstellen, was den Code lesbarer und kompakter macht.

```python
liste = [i for i in range(1, 6)]  # Erstellt eine Liste von 1 bis 5
```

Man kann auch Bedingungen in die List Comprehension einbauen:

```python
liste = [i for i in range(1, 6) if i % 2 == 0]  # Erstellt eine Liste von 1 bis 5, aber nur die geraden Zahlen
```

Ein Beispiel für Quadriete Zahlen 

```python
quadrate = [i*i for i in range(1, 6)]  # Erstellt eine Liste der Quadrate von 1 bis 5
quadrate_gerade = [i*i for i in range(1, 6) if i % 2 == 0]  # Erstellt eine Liste der Quadrate von 1 bis 5, aber nur die geraden Zahlen
```

wir können auch if else bedingungen einbauen:

```python
ergebnis = ["gerade" if i % 2 == 0 else "ungerade" for i in range(1, 6)]  # Erstellt eine Liste, die angibt, ob die Zahl gerade oder ungerade ist
```

Beispiel: gib die Zahlen von 50 bis 100 aus aber jede zahl soll durch 5 teilbar sein und alle die durch 10 sollen durch 0 ersetzt werden.

```python
ergebnis = [0 if i % 10 == 0 else i for i in range(50, 101) if i % 5 == 0]
```


### Linked Lists

Eine Linked List ist eine Datenstruktur, die aus Knoten besteht, die miteinander verbunden sind. Jeder knoten hat zwei Teile: die Load also die Daten und den Pointer, der auf den nächsten Knoten zeigt. Mit diesen Pointer werden die Knoten miteinander verbunden. Listen sind langsamer als Arrays, da sie nicht direkt auf die Elemente zugreifen können, sondern den Pointer folgen müssen. Dafür sind Listen flexibler und können dynamisch wachsen.

In Python können Listen mit der `list`-Klasse erstellt werden.

```python
from typing import List

linked_list: List[int] = [1, 2, 3, 4, 5]  # Erstellt eine Liste von Ganzzahlen
```


### Array Lists 

Array Lists sind eine Kombination aus Arrays und Listen. Sie bieten die Flexibilität von Listen und die direkte Zugriffsmöglichkeit von Arrays. In Python können Array Lists mit der `list`-Klasse erstellt werden.

```python
array_list: List[int] = [1, 2, 3, 4, 5]  # Erstellt eine Array List von Ganzzahlen
array_list.append(6)  # Fügt ein Element am Ende der Liste hinzu 
                      # dadurch wird die Liste dynamisch erweitert
```


## Dictionary

Ein Dictionary ist eine art Wärterbuch in Python. Es besteht aus Schlüssel-Wert-Paaren, wobei jeder Schlüssel eindeutig ist und auf einen Wert verweist. Dictionaries sind sehr effizient, wenn es darum geht, Werte anhand eines Schlüssels abzurufen oder zu ändern.

In Python können Dictionaries mit der `dict`-Klasse erstellt werden.

```python
person = {
    "name": "Alice", # Schlüssel: "name", Wert: "Alice"
    "age": 30,       # Schlüssel: "age", Wert: 30
    "city": "Berlin" # Schlüssel: "city", Wert: "Berlin"
}
```

Oder ein Beispiel für ein Wörterbuch:

```python
woerterbuch = {
    "apple": "Apfel",
    "banana": "Banane",
    "cherry": "Kirsche"
}
```

### Dictionary Komprehension

Wie bei listen gibt es auch bei Dictionaries die Möglichkeit, sie mit einer einzigen Zeile Code zu erstellen. Dies wird als Dictionary Comprehension bezeichnet.

Wir können auch wie bei einer liste if bedingungen einbauen.

```python
zahl = {i: i for i in range(1, 6)}  # Erstellt ein Dictionary
zahl_gerade = {i: i for i in range(1, 6) if i % 2 == 0}  # Erstellt ein Dictionary, aber nur die geraden Zahlen
quadrat = {i: i*i for i in range(1, 6)}  # Erstellt ein Dictionary der Quadrate von 1 bis
quadrat_gerade = {i: i*i for i in range(1, 6) if i % 2 == 0}  # Erstellt ein Dictionary der Quadrate von 1 bis 5, aber nur die geraden Zahlen
```

Man kann auch else if bedingungen einbauen:

```python
ergebnis = {i: "gerade" if i % 2 == 0 else "ungerade" for i in range(1, 6)}  # Erstellt ein Dictionary, das angibt, ob die Zahl gerade oder ungerade ist
```
Beispiel: gib die Zahlen von 50 bis 100 aus aber jede zahl soll durch 5 teilbar sein und alle die durch 10 sollen durch 0 ersetzt werden.

```python
ergebnis = {i: 0 if i % 10 == 0 else i for i in range(50, 101) if i % 5 == 0}
```



## Array vertauschen 

In Python kann man bei einem Array die Elemente vertauschen. 

```python
arr = [1, 2, 3, 4, 5]
arr[0], arr[1] = arr[1], arr[0]
print(arr)  # Ausgabe: [2, 1, 3, 4, 5]
```

Dieser Code tauscht die Elemente an den Positionen 0 und 1 im Array `arr` aus. Das gleiche

## Array einfach letztes Element heraussuchen

In Python kann man anstat das letzte Element mit `arr[len(arr) - 1]` auch einfach `arr[-1]` schreiben.

```python
arr = [1, 2, 3, 4, 5]
print(arr[-1])  # Ausgabe: 5
print(arr[-2])  # Ausgabe: 4
```
Das Funktioniert da man mit -1 das letzte Element auswählt und mit -2 das vorletzte Element und so weiter. Weil der Compiler bei -1 anfängt zu zählen und nicht bei 0. was dazu führt das -1 das letzte Element ist.

Das funktioniert Folgendermaßen:

| Zahl | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|
| Index| 0 | 1 | 2 | 3 | 4 |
| Negativ Index | -5 | -4 | -3 | -2 | -1 |

Mittels des Negativen Indexes kann man also Elemente von hinten auswählen ohne die Länge des Arrays zu kennen.


## Array slicing

In Python kann auch ein Array gesliced werden. Das bedeut das man nur einen Teil des Arrays auswählt.

```python
arr = [1, 2, 3, 4, 5]
print(arr[1:4])  # Ausgabe: [2, 3, 4]
print(arr[:3])   # Ausgabe: [1, 2, 3]
print(arr[2:])   # Ausgabe: [3, 4, 5]
print(arr[:-2])  # Ausgabe: [1, 2, 3]
print(arr[-2:])  # Ausgabe: [4, 5]
```

Mittels des slicing kann man sich also einen Teil des Arrays auswählen. 

### Der ":" in Arrays

Wenn wir den `:` in einem Array verwenden, dann bedeutet das, dass wir alle Elemente von einem Index bis zu einem anderen Index auswählen. 

### Das problem mit Arrays in Python 

In Python gibt es eigentlich keine Arrays sondern nur Arraylisten. Das bedeutet das die Arrays in Python nicht so effizient sind wie in Java. Das liegt daran das die Arrays in Python dynamisch sind und in Java statisch. Das bedeutet das die Arrays in Python langsamer sind als in Java.

**Beispiel:**

```python
arr = [1, 2, 3, 4, 5]
arr.append(6)  # Fügt ein Element am Ende der Liste hinzu
```

in Java würde das so aussehen:

```java
int[] arr = {1, 2, 3, 4, 5};
int[] arr2 = new int[6];
for (int i = 0; i < arr.length; i++) {
    arr2[i] = arr[i];
}
arr2[5] = 6;
```


## Tupel

Ein Tupel ist eine unveränderliche Datenstruktur in Python, die eine geordnete Sammlung von Elementen speichert. Tupel sind ähnlich wie Listen, aber sie können nach der Erstellung nicht mehr geändert werden. Tupel werden mit runden Klammern `()` erstellt.

```python
tupel = (1, 2, 3, 4, 5)
```


## Datentypen in Python

### ganze Zahlen (int)

Ganze Zahlen sind Zahlen ohne Dezimalstellen. In Python können ganze Zahlen beliebig groß sein, da Python automatisch die Größe des Speichers anpasst, um große Zahlen zu unterstützen.

```python
zahl = 42
```

### Division zweier ganzer Zahlen

Wenn wir einfach zwei ganze Zahlen dividieren, dann wird das Ergebnis immer eine Fließkommazahl sein. 

```python
ergebnis = 5 / 2
print(ergebnis)  # Ausgabe: 2.5
```

Java macht Floor Division, was bedeutet das es das Ergebnis auf die nächst kleinere ganze Zahl rundet. Also die Kommerstellen werden abgeschnitten.

```java
int ergebnis = 5 / 2;
System.out.println(ergebnis);  // Ausgabe: 2
```

### Floor Division in Python

Wir können in Python auch Floor Division machen. Das bedeutet das wir das Ergebnis auf die nächst kleinere ganze Zahl runden.

```python
ergebnis = 5 // 2
print(ergebnis)  # Ausgabe: 2
```
Mittels des "//" können wir also Floor Division machen.


## Schlüßelwörter in Python

In Python gibt es ca. 35 Schlüsselwörter. Diese Schlüsselwörter sind reserviert und können nicht als Variablennamen verwendet werden. In Java gibt es auch Schlüsselwörter, viel mehr als in Python. und in SQL gibt es auch Schlüsselwörter aber ca. 100.

### Schlüsselwörter in Python

- `and` ... verwendet in logischen Ausdrücken (z.B. `if x and y:`) um zu prüfen ob beide Bedingungen wahr sind.
- `as` ... wird verwendet um einen Alias für ein Modul zu erstellen (z.B. `import numpy as np`)
- `assert` ... wird verwendet um eine Bedingung zu überprüfen und einen Fehler zu werfen, wenn die Bedingung falsch ist.
- `break` ... wird verwendet um eine Schleife zu beenden.
- `class` ... wird verwendet um eine Klasse zu definieren.
- `continue` ... wird verwendet um den Rest einer Schleife zu überspringen und mit der nächsten Iteration fortzufahren.
- `def` ... wird verwendet um eine Funktion zu definieren.
- `del` ... wird verwendet um eine Variable oder ein Element aus einer Liste zu löschen.
- `elif` ... wird verwendet um eine weitere Bedingung in einer if-Anweisung zu überprüfen.
- `else` ... wird verwendet um den Codeblock auszuführen, wenn keine der vorherigen Bedingungen wahr ist.
- `except` ... wird verwendet um eine Ausnahme in einem try-Block zu behandeln.
- `False` ... ist ein boolescher Wert, der falsch ist. **Achtung:** Der Wert `False` ist ein Schlüsselwort und muss groß geschrieben werden.
- `True` ... ist ein boolescher Wert, der wahr ist. **Achtung:** Der Wert `True` ist ein Schlüsselwort und muss groß geschrieben werden.
- `finally` ... wird verwendet um Code auszuführen, unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht.
- `for` ... wird verwendet um über eine Sequenz zu iterieren.
- `from` ... wird verwendet um bestimmte Elemente aus einem Modul zu importieren.
- `global` ... wird verwendet um eine globale Variable innerhalb einer Funktion zu deklarieren.
- `if` ... wird verwendet um eine Bedingung zu überprüfen.
- `import` ... wird verwendet um ein Modul zu importieren.
- `in` ... wird verwendet um zu überprüfen, ob ein Element in einer Sequenz vorhanden ist.
- `is` ... wird verwendet um zu überprüfen, ob zwei Variablen auf dasselbe Objekt verweisen.
- `lambda` ... wird verwendet um eine anonyme Funktion zu erstellen.
- `None` ... ist ein spezieller Wert, der verwendet wird, um anzuzeigen, dass keine Daten vorhanden sind.
- `nonlocal` ... wird verwendet um eine nichtlokale Variable innerhalb einer Funktion zu deklarieren.
- `not` ... wird verwendet um eine logische Negation durchzuführen.
- `or` ... wird verwendet um in logischen Ausdrücken (z.B. `if x or y:`) zu prüfen, ob mindestens eine Bedingung wahr ist.
- `pass` ... wird verwendet um einen leeren Codeblock zu erstellen.
- `raise` ... wird verwendet um eine Ausnahme manuell auszulösen.
- `return` ... wird verwendet um einen Wert aus einer Funktion zurückzugeben.
- `try` ... wird verwendet um Code zu schreiben, der möglicherweise eine Ausnahme auslöst.
- `while` ... wird verwendet um eine Schleife zu erstellen, die so lange ausgeführt wird, wie eine Bedingung wahr ist.
- `with` ... wird verwendet um eine Datei oder ein Objekt zu öffnen und automatisch zu schließen, wenn der Block beendet ist.
- `yield` ... wird verwendet um einen Generator zu erstellen.

## Programmendung .py

### Sehbang


### Die unterschiedlichen Dateitypen

### Tabs sind in Python wichtig

## Kommentare 

## Tupel, range und set

### Tupel

Ein Tupel ist eine unveränderliche Datenstruktur in Python, die eine geordnete Sammlung von Elementen speichert. Tupel sind ähnlich wie Listen, aber sie können nach der Erstellung nicht mehr geändert werden. Tupel werden mit runden Klammern `()` erstellt.

```python
tupel = (1, 2, 3, 4, 5)
```

### range

Eine range ist eine eingebaute Funktion in Python, die eine Sequenz von Zahlen generiert. Sie wird oft in Schleifen verwendet, um über eine Sequenz zu iterieren. Eine range kann mit einem Startwert, einem Endwert und einem Schrittweite erstellt werden.

```python
for i in range(1, 6):
    print(i)  # Ausgabe: 1, 2, 3, 4, 5
```

### set

Ein Set ist eine ungeordnete Sammlung von eindeutigen Elementen in Python. Sets werden oft verwendet, um Duplikate zu entfernen und Mengenoperationen durchzuführen. Sets werden mit geschweiften Klammern `{}` erstellt.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
```

## Auswertungsreihenfolge der Operatoren

## Referenz / Instanz (bestehend aus Idändität, Wert und Typ)

### Identität 

#### Problem des Seiten Effekts
iste.

## Unterschied zwischen Immutable und Mutable Datentypen

https://openbook.rheinwerk-verlag.de/python/07_003.html#u7.3



### Copy und Deepcopy

# DUNDER (Double Under) Methoden

... einfügen ...

## Programm einfügen __name__ == "__main__"

Wenn wir in einem Programm `__name__ == "__main__"` schreiben, dann erhält das Programm das wir ausführen dem Namen `__main__`. Das bedeutet das wir das Programm direkt ausführen und nicht importieren. Das ist nützlich wenn wir ein Programm schreiben und es testen wollen. 

```python
def main():
    print("Hallo Welt")
   
if __name__ == "__main__":
      main()
```

Das bedeutet das wenn wir das Programm ausführen, dann wird die Funktion `main()` ausgeführt. Wenn wir das Programm importieren, dann wird die Funktion `main()` nicht ausgeführt. Das ist nützlich wenn wir ein Programm schreiben und es testen wollen.

Mittels `import` können wir das Programm in ein anderes Programm importieren und die Funktion `main()` ausführen.

```python
import mein_programm

mein_programm.main()
```

## Laufzeitenmodell in Python

... einfügen ...

## Sequenzielle Datentypen Zusammenfassung

... einfügen aus Website (Zusammenfassung) ...

## Python isinstance() Funktion


## Time Complexity

**Zeitkomplexität** beschreibt, wie sich die Ausführungszeit eines Algorithmus mit wachsender Eingabemenge verhält. In Python ist es wichtig, diese Konzepte zu verstehen, um effizienten Code zu schreiben, der auch mit großen Datenmengen gut arbeitet.

#### Big-O-Notation

Die **Big-O-Notation** wird verwendet, um die obere Grenze der Zeitkomplexität eines Algorithmus zu beschreiben, also die schlimmste mögliche Ausführungszeit im Vergleich zur Größe der Eingabedaten. Sie hilft dabei, Algorithmen hinsichtlich ihrer Effizienz zu bewerten.

Hier sind einige der häufigsten Zeitkomplexitäten:

1. **O(1) – Konstante Zeitkomplexität**: 
   - Ein Algorithmus mit **O(1)** benötigt immer die gleiche Zeit, unabhängig von der Größe der Eingabe. Ein gutes Beispiel dafür ist das Zugreifen auf ein Element einer Liste über den Index.
   
   ```python
   def get_element(lst, index):
       return lst[index]  # O(1) Zeitkomplexität
   ```

2. **O(n) – Lineare Zeitkomplexität**: 
   - Ein Algorithmus mit **O(n)** wächst mit der Eingabemenge. Dies sieht man häufig bei Schleifen, die über alle Elemente einer Liste iterieren.
   
   ```python
   def sum_list(lst):
       total = 0
       for number in lst:
           total += number  # O(n) Zeitkomplexität
       return total
   ```

3. **O(n^2) – Quadratische Zeitkomplexität**: 
   - **O(n^2)** tritt häufig bei Algorithmen mit verschachtelten Schleifen auf, wo jede Iteration der äußeren Schleife eine innere Schleife mit proportionaler Anzahl an Durchläufen verursacht.
   
   ```python
   def bubble_sort(lst):
       n = len(lst)
       for i in range(n):
           for j in range(0, n-i-1):
               if lst[j] > lst[j+1]:
                   lst[j], lst[j+1] = lst[j+1], lst[j]  # O(n^2) Zeitkomplexität
   ```

4. **O(log n) – Logarithmische Zeitkomplexität**:
   - **O(log n)** beschreibt Algorithmen, die die Eingabe bei jedem Schritt halbieren. Ein Beispiel ist die **binäre Suche**, die sehr effizient ist.
   
   ```python
   def binary_search(lst, target):
       low, high = 0, len(lst) - 1
       while low <= high:
           mid = (low + high) // 2
           if lst[mid] == target:
               return mid  # O(log n) Zeitkomplexität
           elif lst[mid] < target:
               low = mid + 1
           else:
               high = mid - 1
       return -1
   ```

5. **O(n log n) – Lineare Logarithmische Zeitkomplexität**: 
   - Viele effiziente Sortieralgorithmen wie **Merge Sort** oder **Quick Sort** haben eine Zeitkomplexität von **O(n log n)**, was schneller ist als quadratische Algorithmen bei großen Datensätzen.
   
   ```python
   def merge_sort(lst):
       if len(lst) > 1:
           mid = len(lst) // 2
           left_half = lst[:mid]
           right_half = lst[mid:]
   
           merge_sort(left_half)
           merge_sort(right_half)
   
           i = j = k = 0
           while i < len(left_half) and j < len(right_half):
               if left_half[i] < right_half[j]:
                   lst[k] = left_half[i]
                   i += 1
               else:
                   lst[k] = right_half[j]
                   j += 1
               k += 1
   
           while i < len(left_half):
               lst[k] = left_half[i]
               i += 1
               k += 1
   
           while j < len(right_half):
               lst[k] = right_half[j]
               j += 1
               k += 1  # O(n log n) Zeitkomplexität
   ```

#### Analyse der Zeitkomplexität in Python

Bei der Analyse der Zeitkomplexität in Python untersucht man oft die Struktur von Schleifen und rekursiven Aufrufen. Auch die eingebauten Datenstrukturen wie Listen, Dictionaries und Sets haben spezifische Zeitkomplexitäten:

- **Listen**: Der Zugriff auf ein Element über den Index ist **O(1)**, aber das Suchen nach einem Element oder das Anhängen eines Elements ist **O(n)**.
- **Dictionaries und Sets**: Die Operationen wie Suchen, Einfügen und Löschen sind im Durchschnitt **O(1)** dank der Hash-Tabellen-Implementierung, können aber im schlimmsten Fall auf **O(n)** abfallen, wenn es viele Kollisionen gibt.

#### Beispiele für Zeitkomplexität in Python:
1. **Listenoperationen**:
   - **Zugriff per Index**: `O(1)`
   - **Anhängen ans Ende**: `O(1)`
   - **Einfügen in die Mitte**: `O(n)`
   - **Suche nach einem Element**: `O(n)`

2. **Dictionaries**:
   - **Einfügen/Aktualisieren**: `O(1)`
   - **Suchen**: `O(1)`
   - **Löschen**: `O(1)`

3. **Sets**:
   - **Einfügen/Aktualisieren**: `O(1)`
   - **Suche nach einem Element**: `O(1)`

#### Bedeutung der Zeitkomplexität

Die Zeitkomplexität ist entscheidend, weil sie hilft, die Effizienz eines Algorithmus zu bewerten. Ein Algorithmus mit einer schlechten Zeitkomplexität kann bei großen Eingabemengen sehr langsam werden und unnötig viel Zeit benötigen. Daher ist es wichtig, bei der Auswahl von Algorithmen und Datenstrukturen auch auf ihre Zeitkomplexität zu achten.

#### Fazit

Die Zeitkomplexität ist ein zentrales Konzept beim Schreiben von effizienten Algorithmen in Python. Sie hilft, die Leistungsfähigkeit von Algorithmen zu verstehen und die richtige Wahl für die jeweilige Aufgabe zu treffen. Wenn du die Zeitkomplexität deiner Algorithmen im Blick behältst, kannst du sicherstellen, dass dein Code auch mit großen Datenmengen gut funktioniert.

Für weiterführende Informationen zur Zeitkomplexität und deren Analyse kannst du Ressourcen wie das Buch *Introduction to Algorithms* von Cormen et al. oder Python-spezifische Dokumentationen und Tutorials verwenden.

## Verschiedene Arten von Python Interpreter


# Exception Handling in Python

## Raise Exception

In Python können wir Ausnahmen (Exceptions oder Fehler) mit der `raise` Anweisung explizit auslösen. Das ist nützlich, wenn wir einen Fehlerzustand erkennen und eine Ausnahme auslösen wollen, um das Programm zu stoppen und eine Fehlermeldung auszugeben.

```python
x = 10
if x > 5:
    raise Exception("Der Wert von x ist zu groß")
```


__ Einfügen __


# Aufgaben

## Erste Aufgabe: Lottoziehung

### Aufgabenstellung

1. Algorithmus zur Lottoziehung -> keine doppelten Zahlen. Wird in einer Methode gemacht. Ziehe 6 Zahlen zwischen 1 und 45 und gib sie aus. Passendes Programm: `lotto_1.py`
2. Lottoziehung Statistik als Methode ->
    - Mache 1000 Ziehungen
    - Erstelle ein Dictionary, wie oft welche Zahl gezogen wurde
    - Rufe die Methode nach jeder Ziehung auf und inkrementiere den passenden Wert im Dictionary um 1
    - Gib das Dictionary am Ende aus
    - Passendes Programm: `lotto_2.py`

## zweite Aufgabe: Pokerspielsimulator 

- Tip: Liste von 52 Karten erstellen das ist dann unser Deck. Dann ziehen wir eine Zahl z.b. wenn wir 44 erhalten können wir durch flor division durch 4 die Farbe und den Wert der Karte herausfinden. Das Symbol erhalten wir durch modulo 13 und der Restwert sind die Kartenwerte.

- Kominationen stehen in Wikipedia mit Prozentangaben. Diese sollten wir anehernd auch erreichen können.

### Aufgabenstellung

Pokerspielsimulator als Aufgabe ueber mehrere Wochen:
- Überlegen wie wir die Karten repräsentieren (vier Farben, 13 Symbole)
- gib zufällig 5 Karten aus
- recherchiere welche Kombinationen es gibt beim Poker
- schreibe Funktionen fuer die Kombinationen Paar, Drillinge, Poker, Flash, Strasse usw.
- spiele 1000 mal und zählen die Anzahl der verschiedenen Kombinationen zu der Gesamtanzahl 
- berechne den prozentuellen Anteil einer Kombination zu der Gesamtspieleanzahl
- recherchiere die richtige Anteile im Netz und vergleiche die Ergebnisse
- Git! 

#### Kombinationen beim Poker

### 1. **Royal Flush** (höchste Hand)
   - Die höchste mögliche Hand im Poker.
   - Es besteht aus den fünf höchsten Karten einer Farbe: 10, Bube (J), Dame (Q), König (K), Ass (A) derselben Farbe.
   - Beispiel: 10♠ J♠ Q♠ K♠ A♠ (alle Pik).

### 2. **Straight Flush**
   - Fünf aufeinanderfolgende Karten derselben Farbe.
   - Beispiel: 5♣ 6♣ 7♣ 8♣ 9♣ (alle Kreuz).
   - Wenn zwei Spieler einen Straight Flush haben, gewinnt der mit der höchsten Karte.

### 3. **Four of a Kind (Vierling)**
   - Vier Karten desselben Werts.
   - Beispiel: 9♠ 9♣ 9♦ 9♥ K♣.
   - Wenn zwei Spieler einen Vierling haben, gewinnt der mit den höheren Karten.

### 4. **Full House**
   - Eine Kombination aus einem Drilling und einem Paar.
   - Beispiel: 8♠ 8♦ 8♣ K♠ K♦ (Drilling 8er und Paar Könige).
   - Bei zwei Full Houses gewinnt der mit dem höheren Drilling.

### 5. **Flush**
   - Fünf beliebige Karten derselben Farbe (nicht aufeinanderfolgend).
   - Beispiel: 2♠ 6♠ 9♠ Q♠ K♠ (alle Pik).
   - Wenn zwei Spieler einen Flush haben, gewinnt der mit der höchsten Karte.

### 6. **Straight**
   - Fünf aufeinanderfolgende Karten, unabhängig von der Farbe.
   - Beispiel: 4♠ 5♣ 6♦ 7♥ 8♣.
   - Wenn zwei Spieler einen Straight haben, gewinnt der mit der höchsten Karte.

### 7. **Three of a Kind (Drilling)**
   - Drei Karten desselben Werts.
   - Beispiel: 7♠ 7♦ 7♣ 2♠ 4♣.
   - Bei zwei Drillingen gewinnt der mit dem höheren Drilling.

### 8. **Two Pair (Zwei Paare)**
   - Zwei Paare von Karten desselben Werts.
   - Beispiel: 10♠ 10♣ 5♦ 5♠ 3♣.
   - Bei zwei Paaren gewinnt das höhere Paar, falls das erste Paar gleich ist, entscheidet das zweite.

### 9. **One Pair (Ein Paar)**
   - Ein Paar von Karten desselben Werts.
   - Beispiel: A♠ A♦ 4♠ 7♣ 9♥.
   - Bei zwei Paaren gewinnt das höhere Paar.

### 10. **High Card (Höchste Karte)**
   - Wenn keine der obigen Kombinationen vorliegt, entscheidet die höchste Karte.
   - Beispiel: A♠ K♦ 7♣ 4♠ 2♥.
   - Wenn zwei Spieler keine Kombination haben, gewinnt der mit der höchsten Karte.

### Kurzgefasst:
- **Royal Flush**: 10, J, Q, K, A einer Farbe.
- **Straight Flush**: Fünf aufeinanderfolgende Karten derselben Farbe.
- **Four of a Kind**: Vier gleiche Karten.
- **Full House**: Drilling und ein Paar.
- **Flush**: Fünf beliebige Karten derselben Farbe.
- **Straight**: Fünf aufeinanderfolgende Karten verschiedener Farben.
- **Three of a Kind**: Drei gleiche Karten.
- **Two Pair**: Zwei Paare.
- **One Pair**: Ein Paar.
- **High Card**: Höchste Karte entscheidet. 

#### Wahrsccheinlichkeiten

Die Wahrscheinlichkeiten für die verschiedenen Pokerhände hängen vom spezifischen Spiel ab, aber für **Texas Hold'em** sind die Wahrscheinlichkeiten für jede Handkombination bei einem Standard-52-Karten-Deck. Hier sind die ungefähren Wahrscheinlichkeiten:

### 1. **Royal Flush**
   - Wahrscheinlichkeit: **0,000154%** (1 zu 649.740)
   - Es gibt nur vier mögliche Kombinationen für einen Royal Flush, je eine pro Farbe.

### 2. **Straight Flush** (außer Royal Flush)
   - Wahrscheinlichkeit: **0,00139%** (1 zu 72.193)
   - Ein Straight Flush besteht aus fünf aufeinanderfolgenden Karten derselben Farbe, z. B. 5♠ 6♠ 7♠ 8♠ 9♠.

### 3. **Four of a Kind (Vierling)**
   - Wahrscheinlichkeit: **0,0240%** (1 zu 4.165)
   - Vier Karten desselben Rangs, z. B. vier Asse oder vier Könige.

### 4. **Full House**
   - Wahrscheinlichkeit: **0,1441%** (1 zu 693)
   - Ein Full House besteht aus einem Drilling und einem Paar, z. B. drei Könige und zwei Zehner.

### 5. **Flush**
   - Wahrscheinlichkeit: **0,197%** (1 zu 508)
   - Ein Flush sind fünf beliebige Karten derselben Farbe, aber nicht in Reihenfolge.

### 6. **Straight**
   - Wahrscheinlichkeit: **0,3925%** (1 zu 255)
   - Ein Straight sind fünf aufeinanderfolgende Karten beliebiger Farbe, z. B. 4♠ 5♣ 6♦ 7♥ 8♣.

### 7. **Three of a Kind (Drilling)**
   - Wahrscheinlichkeit: **2,1128%** (1 zu 47)
   - Drei Karten desselben Rangs, z. B. drei Asse.

### 8. **Two Pair (Zwei Paare)**
   - Wahrscheinlichkeit: **4,7539%** (1 zu 21)
   - Zwei Paare von Karten desselben Werts, z. B. zwei Könige und zwei Zehner.

### 9. **One Pair (Ein Paar)**
   - Wahrscheinlichkeit: **42,2569%** (1 zu 2,37)
   - Ein Paar besteht aus zwei Karten desselben Rangs, z. B. zwei Asse.

### 10. **High Card (Höchste Karte)**
   - Wahrscheinlichkeit: **50,1177%** (1 zu 1,99)
   - Keine der oben genannten Kombinationen, die höchste Karte entscheidet, z. B. Ass als höchste Karte.

### Zusammenfassung der Wahrscheinlichkeiten:

| Pokerhand         | Wahrscheinlichkeit   | 1 zu ...       |
|-------------------|----------------------|----------------|
| Royal Flush       | 0,000154%            | 649.740        |
| Straight Flush    | 0,00139%             | 72.193         |
| Four of a Kind    | 0,0240%              | 4.165          |
| Full House        | 0,1441%              | 693            |
| Flush             | 0,197%               | 508            |
| Straight          | 0,3925%              | 255            |
| Three of a Kind   | 2,1128%              | 47             |
| Two Pair          | 4,7539%              | 21             |
| One Pair          | 42,2569%             | 2,37           |
| High Card         | 50,1177%             | 1,99           |

Diese Wahrscheinlichkeiten gelten für die erste Verteilung der fünf Karten in **Texas Hold'em**. Die genauen Werte können variieren, je nachdem wie viele Spieler teilnehmen und wie viele Gemeinschaftskarten verwendet werden.

