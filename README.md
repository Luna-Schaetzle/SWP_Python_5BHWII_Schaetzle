# SWP Python Projekte - 5BHWII - Luna Schäzle
Willkommen im Repository für alle SWP Python-Projekte der 5. Klasse von Luna Schäzle. Hier findest du alle Programme und Projekte, die im Rahmen des SWP-Unterrichts (Softwareentwicklung und Programmierung) erstellt wurden.

# Inhalt
Dieses Repository enthält:

Verschiedene Python-Programme und -Skripte, die während des Schuljahres entwickelt wurden.
Lösungen zu Aufgaben und Projekten aus dem Unterricht.
Beispielanwendungen und kleine Projekte, die verschiedene Aspekte der Python-Programmierung abdecken, wie Datenstrukturen, Algorithmen, Dateiverarbeitung und vieles mehr.

# Voraussetzungen
Um die hier enthaltenen Python-Skripte auszuführen, benötigst du:

Python 3.10 installiert auf deinem Computer.

# Mitschriften 

Hier sind die Verbesserungen, der Notizen, die ich wärend der SWP Stunden gemacht habe:

# Einführung in Python

Python ist eine plattformunabhängige, interpretierte und hochabstrakte Programmiersprache. Diese Eigenschaften machen Python vielseitig und leicht zugänglich für Entwickler.

## Eigenschaften von Python

### 1. Plattformunabhängigkeit
- **Plattformunabhängig** bedeutet, dass Python auf allen gängigen Betriebssystemen (Windows, Linux, macOS) läuft. Einmal geschriebener Code kann ohne Anpassungen auf verschiedenen Systemen ausgeführt werden.

### 2. Interpretierte Sprache
- Python ist eine **interpretierte Sprache**, d.h. der Code wird zur Laufzeit direkt interpretiert, anstatt vorab in Maschinencode (wie bei kompilierte Sprachen) übersetzt zu werden. Dies ermöglicht eine direkte Ausführung des Codes ohne Zwischenschritte.

**Beispiele für Interpreter Sprachen:**
- Python
- php 
- Ruby

**Unterschied zwischen interpretierten und kompilierten Sprachen**
- **Kompilierte Sprachen:** Der Code wird vor dem Ausführen in Maschinencode übersetzt, was zu einer schnelleren Ausführung führen kann. Beispiele: C, C++, Java.
- **Interpretierte Sprachen:** Der Code wird zur Laufzeit interpretiert, was eine flexiblere und dynamischere Entwicklung ermöglicht. Beispiele: Python, JavaScript, Ruby.



### 3. Hochsprache
- Python ist eine **höhere Programmiersprache**, was bedeutet, dass sie sehr nah an der natürlichen menschlichen Sprache liegt und einfach zu lesen und zu schreiben ist.
  
  **Vergleich:**  
  - **Maschinensprachen** wie C oder Assembler sind schwerer zu verstehen und zu schreiben, da sie sehr nah an der Hardware arbeiten.  
  - **Hochsprachen** wie Python, Java oder C# abstrahieren viele hardwarenahe Details und machen das Programmieren einfacher.

Ein Beispiel für Assembler Code:
```asm
section .data
  num1 db 5
  num2 db 10
  result db 0

section .text
  global _start

_start:
  ; Load the first number into AL register
  mov al, [num1]
  
  ; Add the second number to AL register
  add al, [num2]
  
  ; Store the result in the result variable
  mov [result], al
  
  ; Exit the program
  mov eax, 60         ; syscall: exit
  xor edi, edi        ; status: 0
  syscall
```
Das gleiche Programm in Python:
```python
num1 = 5
num2 = 10
result = num1 + num2
```
Also man sieht das der Python Code viel einfacher zu lesen und zu schreiben ist.

Der code muss allerdings in Python interpretiert werden, was halt python eine der langsameren Sprachen macht.

### 4. Bytecode in Python
- Obwohl Python interpretiert wird, gibt es sogenannte **Bytecode-Dateien** (mit der Endung `.pyc`), die beim Speichern von Python-Dateien erstellt werden. Diese Dateien enthalten eine kompilierte Version des Codes, die bei späteren Ausführungen die Startzeit verkürzen kann. Python kann den Code jedoch auch ohne diese Bytecode-Dateien ausführen.

### 5. Standardbibliotheken und Module
- **Umfangreiche Standardbibliotheken:** Python bietet eine Vielzahl vorinstallierter Module, die häufige Programmieraufgaben abdecken (z.B. für Dateioperationen, Netzwerke, Webentwicklung). Im Vergleich zu Sprachen wie Java oder C# ist die Installation und Nutzung von Bibliotheken in Python besonders einfach.
  - **Installation von Bibliotheken via pip** erfolgt meist über den Paketmanager `pip`:  
    ```bash
    pip install <Bibliothek>
    ```
  - **Installation von Bibliotheke via apt-get install** erfolgt meist über den Paketmanager `apt-get`:  
    ```bash
    sudo apt-get install python3-<Bibliothek>
    ```
  - In Java hingegen müssen Bibliotheken oft manuell heruntergeladen und in das Projekt integriert werden.
    - **Installation von Bibliotheken in Java** erfolgt meist über Maven oder Gradle:  
    ```xml
    <dependency>
        <groupId>...</groupId>
        <artifactId>...</artifactId>
        <version>...</version>
    </dependency>
    ```
    - **Installation von Bibliotheken in Java** erfolgt meist über Maven oder Gradle:  
    ```gradle
    dependencies {
        implementation '...'
    }
    ```

### 6. Rapid Prototyping
- Python eignet sich sehr gut für **Rapid Prototyping**, da es in der Regel weniger Code benötigt, um eine Lösung zu implementieren, verglichen mit Sprachen wie Java. Dies macht Python besonders nützlich für schnelle Entwicklungszyklen.

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
- **Instanz:** Eine Instanz ist ein konkretes Objekt auf dem ein Zeiger (Referenz) zeigt. Instanzen können Klassenattribute und Methoden enthalten.
  
  ```python
  class Person:
      def __init__(self, name):
          self.name = name
  
  p1 = Person("Alice")  # p1 ist eine Instanz der Klasse Person
  ```
- **Referenz:** Eine Referenz zeigt auf eine Instanz, d.h. es ist eine Art Zeiger auf den Speicherort einer Instanz. Mehrere Referenzen können auf dieselbe Instanz zeigen.
    ```python
    p2 = p1  # p2 zeigt auf die gleiche Instanz wie p1
    ```

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

Der Interaktive Modus ist ein Modus in Python, in dem der Code Zeile für Zeile ausgeführt wird. Dies ermöglicht es, den Code schrittweise zu testen und die Ausgabe direkt zu sehen. 
'''bash
python3
'''
mit diesem Beffehl starten wir den interaktiven Modus von Python.

Der sieht dann so aus:
```bash
Python 3.10.0 (default, Oct  8 2021, 16:02:42)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Dann kann man in Python code eingeben und er wird sofort ausgeführt. Das sieht dann so aus:
```bash
>>> print("Hallo Welt")
Hallo Welt
```

Man kann auch Rechnungen machen:
```bash
>>> 5 + 5
10
```

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

Dateiendungen sind in der Informatik wichtig, da sie anzeigen, um welchen Dateityp es sich handelt und welches Programm verwendet werden soll, um die Datei zu öffnen. In Python haben Dateien mit der Endung `.py` eine besondere Bedeutung, da sie Python-Skripte enthalten. Python-Skripte sind Textdateien, die Python-Code enthalten und mit dem Python-Interpreter ausgeführt werden können. 

### Sehbang

Der Shebang ist eine spezielle Zeile am Anfang einer Datei, die dem Betriebssystem mitteilt, welcher Interpreter verwendet werden soll, um die Datei auszuführen. In Python-Skripten wird oft der Shebang `#!/usr/bin/env python3` verwendet, um den Python-Interpreter zu starten.

Damit weiß das Betriebssystem, dass es den Python-Interpreter verwenden soll, um das Skript auszuführen. Der Shebang ist optional, aber empfohlen, da er die Ausführung des Skripts erleichtert. 

Nach dem `#!` wird der Pfad zum Python-Interpreter angegeben, in diesem Fall `python3`. Das `env`-Programm sucht nach dem Python-Interpreter im System und verwendet die Version, die standardmäßig installiert ist.

### Die unterschiedlichen Dateitypen

In einer **.exe** steht für eine ausführbare Datei. Diese Dateien können direkt ausgeführt werden, ohne dass ein spezielles Programm benötigt wird. Da dort Maschienen Code drinnen ist.

In einer **.txt** steht für eine Textdatei. Diese Dateien enthalten Text und können mit einem Texteditor geöffnet und bearbeitet werden. Da stehen nur Text drinnen.
Es gibt auch andere Textdateien wie .docx oder .pdf die aber nicht so einfach zu öffnen sind, aber auch Programmdateien sind textdateien wie .py oder .java. Diese müssen erst Interpretiert werden. 

### Tabs sind in Python wichtig

In manchen Programmiersprachen sind Tabs nicht wichtig, aber in Python sind sie sehr wichtig. Tabs werden in Python verwendet, um Blöcke von Code zu definieren, z.B. in Schleifen oder Funktionen. Wenn die Einrückung nicht korrekt ist, wird ein IndentationError ausgelöst.

In Python 3 ist ein Tab als 4 Leerzeichen definiert. Das bedeutet, dass ein Tab durch 4 Leerzeichen ersetzt wird. Es ist wichtig, konsistent zu sein und entweder Tabs oder Leerzeichen zu verwenden, aber nicht beides gemischt.

## Kommentare 

Kommentare macht man mit einem `#` in Python. Kommentare sind nützlich, um den Code zu dokumentieren und zu erklären, was er tut. Kommentare werden vom Interpreter ignoriert und haben keinen Einfluss auf die Ausführung des Codes.

```python
# Dies ist ein Kommentar
print("Hallo Welt")  # Dies ist auch ein Kommentar
```

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

... einfügen ...

## Referenz / Instanz (bestehend aus Idändität, Wert und Typ)

### Identität 

Eine Identität ist eine eindeutige Kennung (Fingerabdruck) eines Objekts in Python. Die Identität eines Objekts wird durch die Funktion `id()` zurückgegeben. Die Identität eines Objekts ändert sich während seiner Lebensdauer nicht.

```python
x = 42
print(id(x))  # Ausgabe: 140735000221424
```

Wenn wir zwei Variablen auf denselben Wert setzen, dann haben sie die gleiche Identität.

```python
x = 42
y = 42
print(id(x))  # Ausgabe: 140735000221424
print(id(y))  # Ausgabe: 140735000221424
```

Das kommt daher da Python um Speicher zu sparen, die gleichen Werte auf den gleichen Speicherplatz speichert.

Wenn wir aber zwei Variablen auf unterschiedliche Werte setzen, dann haben sie unterschiedliche Identitäten.

```python
x = 42
y = 43
print(id(x))  # Ausgabe: 140735000221424
print(id(y))  # Ausgabe: 140735000221456
```

Wenn wir nun listen oder Dictionaries haben, dann haben sie eine eigene Identität.

```python
liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
print(id(liste1))  # Ausgabe: 140735000221424
print(id(liste2))  # Ausgabe: 140735000221456
```

#### Problem des Seiten Effekts

Wenn wir nun eine liste auf eine andere Liste setzen, dann haben sie die gleiche Identität. 
Das führt dazu das wenn wir eine Liste ändern, dann ändert sich auch die andere Liste.

```python
liste1 = [1, 2, 3]
liste2 = liste1
liste2.append(4)
print(liste1)  # Ausgabe: [1, 2, 3, 4]
print(liste2)  # Ausgabe: [1, 2, 3, 4]
```

**Achtung:** Das ist ein Problem des Seiten Effekts. Das bedeutet das wenn wir eine Liste ändern, dann ändert sich auch die andere Liste. Das kann zu unerwünschten Nebeneffekten führen. Das kann einem das Leben schwer machen weil dadurch Fehler entstehen können.

### Es ergibt sich folgendes:

Bei Datenstruckturen werden eigentlich nur Referenzen auf die Daten gespeichert. Das bedeutet das keine Daten gespeichert werden sondern nur die Referenzen auf die Daten. Das bedeutet das wenn wir eine Liste auf eine andere Liste setzen, dann haben sie die gleiche Identität. Das führt dazu das wenn wir eine Liste ändern, dann ändert sich auch die andere Liste.

## Unterschied zwischen Immutable und Mutable Datentypen

https://openbook.rheinwerk-verlag.de/python/07_003.html#u7.3

### Immutable Datentypen

Immutable Datentypen (unveränderliche Datentypen) können nach ihrer Erstellung nicht verändert werden. Wenn der Wert einer Variablen geändert wird, die auf einen immutablen Datentyp zeigt, wird eine neue Instanz des Wertes erstellt, und die Referenz der Variablen wird auf diesen neuen Wert gesetzt. Der ursprüngliche Wert bleibt unverändert, es wird lediglich ein neuer Wert erzeugt und der Variable zugewiesen.

```python
x = 42
print(id(x))  # Ausgabe: 140735000221424
x = 43
print(id(x))  # Ausgabe: 140735000221456
z = x
print(id(z))  # Ausgabe: 140735000221456
z = 55
print(x)  # Ausgabe: 43, also bleibt x unverändert bei 43
```

**Beispiele für Immutable Datentypen:**
- `int`
- `float`
- `str`
- `tuple`

### Mutable Datentypen

Mutable Datentypen (veränderliche Datentypen) können nach ihrer Erstellung direkt verändert werden. Wenn eine Variable auf einen mutable Datentyp zeigt, bleiben Änderungen an der Datenstruktur bestehen, ohne dass eine neue Referenz erstellt wird. Werden zwei Variablen auf dieselbe mutable Datenstruktur gesetzt, beeinflussen Änderungen an einer dieser Variablen auch die andere, da beide auf dasselbe Objekt zeigen.

```python
liste = [1, 2, 3]
print(id(liste))  # Ausgabe: 140735000221424
liste.append(4)
print(id(liste))  # Ausgabe: 140735000221424
liste2 = liste
print(id(liste2))  # Ausgabe: 140735000221424
liste2.append(5)
print(liste)  # Ausgabe: [1, 2, 3, 4, 5], die Liste wurde verändert, obwohl wir liste2 bearbeitet haben
              # liste und liste2 verweisen auf dasselbe Objekt
```

**Beispiele für Mutable Datentypen:**
- `list`
- `dict`
- `set`

## Laufzeitenmodell in Python

... einfügen aus Website ...

## Sequenzielle Datentypen Zusammenfassung

... einfügen aus Website (Zusammenfassung) ...


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



