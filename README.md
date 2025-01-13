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

# Table of Contents
- [Einführung in Python](#einführung-in-python)
   - [Eigenschaften von Python](#eigenschaften-von-python)
      - [Plattformunabhängigkeit](#1-plattformunabhängigkeit)
      - [Interpretierte Sprache](#2-interpretierte-sprache)
      - [Hochsprache](#3-hochsprache)
      - [Bytecode in Python](#4-bytecode-in-python)
      - [Standardbibliotheken und Module](#5-standardbibliotheken-und-module)
      - [Rapid Prototyping](#6-rapid-prototyping)
   - [Unterschiede zwischen Python und Java](#unterschiede-zwischen-python-und-java)
      - [Typisierung](#1-typisierung)
      - [Programmierparadigmen](#2-programmierparadigmen)
      - [Speicherverwaltung und Garbage Collection](#3-speicherverwaltung-und-garbage-collection)
      - [Speicherfreigabe](#4-speicherfreigabe)
   - [Wichtige Konzepte in Python](#wichtige-konzepte-in-python)
      - [Instanzen und Referenzen](#1-instanzen-und-referenzen)
      - [Schlüsselwort `del`](#2-schlüsselwort-del)
      - [Python interaktiver Modus](#3-python-interaktiver-modus)
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
   - [Programmendung .py](#programmendung-py)
      - [Sehbang](#sehbang)
      - [Die unterschiedlichen Dateitypen](#die-unterschiedlichen-dateitypen)
      - [Tabs sind in Python wichtig](#tabs-sind-in-python-wichtig)
   - [Kommentare](#kommentare)
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

In Python gibt es eine bestimmte Reihenfolge, in der Operatoren ausgewertet werden. Diese Reihenfolge wird als Operatorpräzedenz bezeichnet. Hier ist eine Übersicht der Operatoren in absteigender Reihenfolge ihrer Präzedenz:

1. **Klammern**: `()`
   - Klammern haben die höchste Präzedenz und werden zuerst ausgewertet.
   - Beispiel: `(2 + 3) * 4` ergibt `20`.

2. **Exponentiation**: `**`
   - Exponentiation wird vor allen anderen arithmetischen Operationen ausgewertet.
   - Beispiel: `2 ** 3 ** 2` ergibt `512` (nicht `64`).

3. **Vorzeichen**: `+x`, `-x`, `~x`
   - Vorzeichenoperatoren werden vor Multiplikation und Division ausgewertet.
   - Beispiel: `-3 ** 2` ergibt `-9`.

4. **Multiplikation, Division, Modulo und Ganzzahl-Division**: `*`, `/`, `//`, `%`
   - Diese Operatoren haben die gleiche Präzedenz und werden von links nach rechts ausgewertet.
   - Beispiel: `10 / 2 * 3` ergibt `15`.

5. **Addition und Subtraktion**: `+`, `-`
   - Diese Operatoren haben die gleiche Präzedenz und werden von links nach rechts ausgewertet.
   - Beispiel: `10 - 2 + 3` ergibt `11`.

6. **Bitweise Verschiebung**: `<<`, `>>`
   - Diese Operatoren verschieben die Bits eines Wertes nach links oder rechts.
   - Beispiel: `2 << 3` ergibt `16`.

7. **Bitweise UND**: `&`
   - Dieser Operator führt ein bitweises UND durch.
   - Beispiel: `5 & 3` ergibt `1`.

8. **Bitweise XOR**: `^`
   - Dieser Operator führt ein bitweises exklusives ODER durch.
   - Beispiel: `5 ^ 3` ergibt `6`.

9. **Bitweise ODER**: `|`
   - Dieser Operator führt ein bitweises ODER durch.
   - Beispiel: `5 | 3` ergibt `7`.

10. **Vergleichsoperatoren**: `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in`
    - Diese Operatoren vergleichen Werte und geben `True` oder `False` zurück.
    - Beispiel: `3 > 2` ergibt `True`.

11. **Logisches NICHT**: `not`
    - Dieser Operator negiert einen booleschen Wert.
    - Beispiel: `not True` ergibt `False`.

12. **Logisches UND**: `and`
    - Dieser Operator gibt `True` zurück, wenn beide Operanden `True` sind.
    - Beispiel: `True and False` ergibt `False`.

13. **Logisches ODER**: `or`
    - Dieser Operator gibt `True` zurück, wenn mindestens einer der Operanden `True` ist.
    - Beispiel: `True or False` ergibt `True`.

### Beispiel zur Operatorpräzedenz

```python
result = 3 + 4 * 2 / (1 - 5) ** 2
print(result)  # Ausgabe: 3.5
```

In diesem Beispiel wird die Reihenfolge der Auswertung wie folgt sein:
1. Klammern: `(1 - 5)` ergibt `-4`
2. Exponentiation: `(-4) ** 2` ergibt `16`
3. Multiplikation und Division: `4 * 2 / 16` ergibt `0.5`
4. Addition: `3 + 0.5` ergibt `3.5`

Die Kenntnis der Operatorpräzedenz hilft dabei, den Code korrekt zu schreiben und zu verstehen, wie Ausdrücke ausgewertet werden.

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

### Copy und Deepcopy

#### Copy

In Python gibt es die Funktionen `copy` und `deepcopy` aus dem Modul `copy`, um Kopien von Datenstrukturen zu erstellen. Diese Funktion erstellt eine flache Kopie der Datenstruktur, d.h. nur die oberste Ebene der Datenstruktur wird kopiert. Bei einer flachen Kopie wird die Datenstruktur kopiert, aber die Elemente der Datenstruktur bleiben die gleichen.

```python
import copy

liste = [1, 2, 3]
liste2 = copy.copy(liste)
liste2.append(4)
print(liste)  # Ausgabe: [1, 2, 3], die Liste wurde nicht verändert
```

Somit wird der seiten Effekt umgangen.

#### Deepcopy

In Python gibt es die Funktionen `copy` und `deepcopy` aus dem Modul `copy`, um Kopien von Datenstrukturen zu erstellen. Diese Funktion erstellt eine tiefe Kopie der Datenstruktur, d.h. die gesamte Datenstruktur wird kopiert. Bei einer tiefen Kopie wird die Datenstruktur kopiert und alle Elemente der Datenstruktur werden ebenfalls kopiert.

```python
import copy

liste = [1, 2, 3, [4, 5]]
liste2 = copy.deepcopy(liste)
liste2[4] = 6
print(liste)  # Ausgabe: [1, 2, 3, [4, 5]], die Liste wurde nicht verändert
```
Wenn wir nur copy angewändet hätten, dann wäre die Liste verändert worden.

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

[Python isinstance() Funktion Beschreibung](https://www.programiz.com/python-programming/methods/built-in/isinstance)

Die `isinstance()` Funktion wird verwendet, um zu überprüfen, ob ein Objekt einer bestimmten Klasse oder einem bestimmten Datentyp entspricht. Die Funktion gibt `True` zurück, wenn das Objekt der angegebenen Klasse oder dem angegebenen Datentyp entspricht, andernfalls gibt sie `False` zurück.

### Syntax

```python
isinstance(object, classinfo)
```
**Beispiel:**

```python
x = 5
print(isinstance(x, int))  # Ausgabe: True
print(isinstance(x, str))  # Ausgabe: False
liste = [1, 2, 3]
print(isinstance(liste, list))  # Ausgabe: True
print(isinstance(liste, tuple))  # Ausgabe: False
list_2 = (1, 2, 3) # Tuple weil es mit runden Klammern erstellt wurde
print(isinstance(list_2, list))  # Ausgabe: False
print(isinstance(list_2, tuple))  # Ausgabe: True
```

### Praktische Anwendung

Da wir in Pyhton listen gemischt verwenden können, ist es manchmal nützlich zu überprüfen, ob ein Objekt einer bestimmten Klasse oder einem bestimmten Datentyp entspricht. Das kann uns helfen, Fehler zu vermeiden und sicherzustellen, dass wir mit den richtigen Daten arbeiten.

**Beispiel:**

```python
liste = [1, 2, 3, "vier", "fünf"]
#wir saubern die liste in einer Zeile
liste_clean = [x for x in liste if isinstance(x, int)]
print(liste_clean)  # Ausgabe: [1, 2, 3]
```

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

Es gibt verschiedene Arten von Python-Interpretern, die für unterschiedliche Zwecke und Anwendungen entwickelt wurden. Hier sind einige der bekanntesten Python-Interpretern:

1. **CPython**: 
   - CPython ist der Standard-Interpreter für Python und wird von der Python-Software-Stiftung entwickelt. Er ist in C geschrieben und implementiert die offizielle Python-Spezifikation. CPython ist die am weitesten verbreitete Implementierung von Python und wird für die meisten Anwendungen verwendet.
2. **JYTHON**: 
   - Jython ist eine Implementierung von Python, die in Java geschrieben ist und auf der Java Virtual Machine (JVM) ausgeführt wird. Jython ermöglicht die nahtlose Integration von Python-Code in Java-Anwendungen und umgekehrt.
3. **IronPython**:
   - IronPython ist eine Implementierung von Python, die in C# geschrieben ist und auf der .NET-Plattform ausgeführt wird. IronPython ermöglicht die Integration von Python-Code in .NET-Anwendungen und umgekehrt.

# Fehlerbehandlung in Python: `try` und `except`

## Was ist Fehlerbehandlung?

Fehlerbehandlung ermöglicht es deinem Programm, auf **Ausnahmen** (Fehler) zu reagieren, ohne abzustürzen. Mit `try` und `except` kannst du solche Fehler abfangen und angemessen darauf reagieren.

## Grundstruktur

```python
try:
    # Code, der ausgeführt wird und Fehler verursachen kann
    result = 10 / 0
except ZeroDivisionError:
    # Code, der ausgeführt wird, wenn ein ZeroDivisionError auftritt
    print("Division durch Null ist nicht erlaubt.")
```

**Erklärung:**
- **`try`-Block:** Enthält den Code, der potenziell Fehler verursachen könnte.
- **`except`-Block:** Fängt spezifische Fehler ab und definiert, wie darauf reagiert werden soll.

## Allgemeine Syntax

```python
try:
    # Gefährlicher Code
    pass
except [Fehlertyp]:
    # Fehlerbehandlung
    pass
```

## Häufig verwendete `except`-Blöcke

### Fangen eines spezifischen Fehlers

```python
try:
    zahl = int(input("Gib eine Zahl ein: "))
    result = 10 / zahl
except ZeroDivisionError:
    print("Du kannst nicht durch Null teilen.")
except ValueError:
    print("Bitte gib eine gültige Zahl ein.")
```

### Allgemeiner Fehlerabfang

```python
try:
    # Gefährlicher Code
    pass
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
```

**Hinweis:** Das Fangen aller Fehler mit `Exception` sollte sparsam verwendet werden, um spezifische Fehler nicht zu übersehen.

## `else`-Block

Wird ausgeführt, wenn kein Fehler im `try`-Block auftritt.

```python
try:
    zahl = int(input("Gib eine Zahl ein: "))
    result = 10 / zahl
except ZeroDivisionError:
    print("Du kannst nicht durch Null teilen.")
else:
    print(f"Ergebnis ist {result}")
```

## `finally`-Block

Wird immer ausgeführt, unabhängig davon, ob ein Fehler aufgetreten ist oder nicht. Nützlich für Aufräumarbeiten.

```python
try:
    datei = open("beispiel.txt", "r")
    inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden.")
finally:
    datei.close()
    print("Datei wurde geschlossen.")
```

## Mehrere `except`-Blöcke

Du kannst mehrere `except`-Blöcke verwenden, um verschiedene Fehlertypen unterschiedlich zu behandeln.

```python
try:
    # Gefährlicher Code
    pass
except ValueError:
    print("Ein Wertfehler ist aufgetreten.")
except TypeError:
    print("Ein Typfehler ist aufgetreten.")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
```

## Benutzerdefinierte Fehler werfen

Du kannst eigene Fehler mit `raise` auslösen.

```python
def überprüfe_alter(alter):
    if alter < 0:
        raise ValueError("Alter kann nicht negativ sein.")
    else:
        print(f"Alter ist {alter}")

try:
    überprüfe_alter(-5)
except ValueError as ve:
    print(f"Fehler: {ve}")
```

## Best Practices

- **Spezifische Fehler fangen:** Fange immer die spezifischen Fehler, die auftreten können, anstatt allgemeine Fehler.
- **Vermeide leere `except`-Blöcke:** Fange nicht einfach alle Fehler ab, ohne sie zu behandeln.
- **Nutze `finally` für Aufräumarbeiten:** Stelle sicher, dass Ressourcen wie Dateien oder Netzwerksockets ordnungsgemäß geschlossen werden.
- **Verwende `else` für Code ohne Fehlerbehandlung:** Halte den `try`-Block für den fehleranfälligen Code und den `else`-Block für den erfolgreichen Ablauf.

## Zusammenfassung

- **`try`-Block:** Enthält den Code, der potenziell Fehler verursachen kann.
- **`except`-Block:** Fängt und behandelt spezifische Fehler.
- **`else`-Block:** Wird ausgeführt, wenn kein Fehler auftritt.
- **`finally`-Block:** Wird immer ausgeführt, unabhängig vom Fehlerstatus.
- **Benutzerdefinierte Fehler:** Mit `raise` können eigene Fehler ausgelöst werden.
- **Best Practices:** Fange spezifische Fehler, vermeide allgemeine und leere `except`-Blöcke, nutze `finally` für Aufräumarbeiten.


# Python f-Strings (formatierte String-Literale)

## Was sind f-Strings?

- **f-Strings** (formatierte String-Literale) sind eine Möglichkeit zur String-Formatierung in Python, eingeführt in Python 3.6.
- Sie ermöglichen das Einfügen von Variablen und Ausdrücken direkt innerhalb von Strings durch Voranstellen eines `f` vor den Anführungszeichen.

## Grundlegende Syntax

```python
name = "Alice"
alter = 30
grüße = f"Hallo, mein Name ist {name} und ich bin {alter} Jahre alt."
print(grüße)
# Ausgabe: Hallo, mein Name ist Alice und ich bin 30 Jahre alt.
```

## Vorteile von f-Strings

- **Lesbarkeit:** Klar und intuitiv.
- **Performance:** Schneller als ältere Formatierungsmethoden (`%`-Operator, `str.format()`).
- **Flexibilität:** Unterstützt Ausdrücke und komplexe Formatierungen.

## Einfügen von Ausdrücken

```python
a = 5
b = 10
ergebnis = f"Fünf plus zehn ist {a + b}."
print(ergebnis)
# Ausgabe: Fünf plus zehn ist 15.
```

## Formatierungsmöglichkeiten

### Zahlenformatierung

- **Dezimalstellen festlegen:**

  ```python
  pi = 3.14159
  formatted = f"Pi auf zwei Dezimalstellen: {pi:.2f}"
  print(formatted)
  # Ausgabe: Pi auf zwei Dezimalstellen: 3.14
  ```

- **Ganzzahlen mit führenden Nullen:**

  ```python
  zahl = 42
  formatted = f"Die Zahl ist {zahl:05}"
  print(formatted)
  # Ausgabe: Die Zahl ist 00042
  ```

### Zeichenkettenausrichtung

- **Links-, Rechts- und Zentrierte Ausrichtung:**

  ```python
  text = "Python"
  links = f"{text:<10}"    # Links ausgerichtet
  rechts = f"{text:>10}"   # Rechts ausgerichtet
  mitte = f"{text:^10}"    # Zentriert
  print(links, rechts, mitte)
  # Ausgabe: Python    Python    Python   
  ```

## Mehrzeilige f-Strings

- Verwendung von dreifachen Anführungszeichen für mehrzeilige Strings:

  ```python
  name = "Bob"
  alter = 25
  info = f"""
  Name: {name}
  Alter: {alter}
  """
  print(info)
  # Ausgabe:
  # Name: Bob
  # Alter: 25
  ```

## Escaping und Literale

- **Doppelte geschweifte Klammern für Literale:**

  ```python
  literal = f"{{Dies ist ein Literal}}"
  print(literal)
  # Ausgabe: {Dies ist ein Literal}
  ```

## Debugging mit f-Strings

- **Ausgabe von Variablen und ihren Werten:**

  ```python
  wert = 100
  debug = f"{wert=}"
  print(debug)
  # Ausgabe: wert=100
  ```

## Best Practices

- **Verwendung von f-Strings für einfache und lesbare Formatierungen.**
- **Vermeidung von komplexen Ausdrücken innerhalb der geschweiften Klammern für bessere Lesbarkeit.**
- **Kombination mit Funktionen und Methoden zur sauberen Strukturierung.**

## Fazit

f-Strings sind eine leistungsstarke und flexible Methode zur String-Formatierung in Python. Sie verbessern die Lesbarkeit und Wartbarkeit des Codes und bieten gleichzeitig eine hohe Performance. Durch die Unterstützung von Ausdrücken und umfangreichen Formatierungsoptionen sind f-Strings ideal für eine Vielzahl von Anwendungsfällen.


# Python `unittest` Modul Zusammenfassung

## Einführung in `unittest`

- **`unittest`** ist das standardmäßige Testframework in Python.
- Es basiert auf dem **xUnit**-Framework und unterstützt automatisiertes Testen von Code.
- Ermöglicht das Schreiben und Ausführen von **Testfällen**, **Test-Suites** und **Test-Runnern**.


Es ist sehr nützlich da man mit `unittest` sich alle Tests die man vertielt hat, 

## Grundkonzepte

### TestCase

- **`TestCase`** ist die Basisklasse für alle Testfälle.
- Jeder Testfall ist eine Methode innerhalb einer `TestCase`-Unterklasse, die mit `test_` beginnt.

**Beispiel:**

```python
import unittest

class TestMathe(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
```

### Testmethoden

- Testmethoden müssen mit `test_` beginnen, damit sie vom Test-Runner erkannt werden.
- Innerhalb dieser Methoden werden **Assertions** verwendet, um Erwartungen zu überprüfen.

### Assertions

- Methoden zur Überprüfung von Bedingungen.
- Wichtige Assertions:
  - `assertEqual(a, b)`: Prüft, ob `a == b`.
  - `assertNotEqual(a, b)`: Prüft, ob `a != b`.
  - `assertTrue(x)`: Prüft, ob `x` wahr ist.
  - `assertFalse(x)`: Prüft, ob `x` falsch ist.
  - `assertRaises(exception, func, *args, **kwargs)`: Prüft, ob eine Exception ausgelöst wird.

**Beispiel:**

```python
def test_subtraktion(self):
    self.assertEqual(5 - 3, 2)

def test_exception(self):
    with self.assertRaises(ZeroDivisionError):
        1 / 0
```

## Test Fixtures

- **Fixtures** sind Setup- und Teardown-Methoden, die vor und nach jedem Test ausgeführt werden.
- Methoden:
  - `setUp()`: Wird vor jedem Test ausgeführt.
  - `tearDown()`: Wird nach jedem Test ausgeführt.
  - `setUpClass()`: Wird einmal vor allen Tests in der Klasse ausgeführt.
  - `tearDownClass()`: Wird einmal nach allen Tests in der Klasse ausgeführt.

**Beispiel:**

```python
class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DatenbankVerbindung()

    def setUp(self):
        self.db.start_transaction()

    def tearDown(self):
        self.db.rollback_transaction()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
```

## Test Suites

- **Test-Suites** gruppieren mehrere Testfälle.
- Ermöglichen das gleichzeitige Ausführen mehrerer Tests.

**Beispiel:**

```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMathe('test_addition'))
    suite.addTest(TestMathe('test_subtraktion'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

## Test Runner

- **Test Runner** führt die Tests aus und gibt die Ergebnisse aus.
- Standardmäßig wird der **TextTestRunner** verwendet, der Ergebnisse in der Konsole anzeigt.

**Ausführen der Tests:**

```bash
python -m unittest test_module.py
```

## Organisieren von Tests

- Tests können in separate Dateien und Verzeichnisse organisiert werden.
- Verwendung von Namenskonventionen (`test_*.py`) erleichtert das Auffinden durch den Test-Runner.

**Beispiel-Verzeichnisstruktur:**

```
projekt/
│
├── modul.py
├── test_modul.py
└── tests/
    ├── __init__.py
    └── test_andere_modul.py
```

## Erweiterte Features

### Mocking

- **`unittest.mock`** ermöglicht das Ersetzen von Teilen des Systems unter Test durch Mock-Objekte.
- Nützlich für das Testen von Komponenten in Isolation.

**Beispiel:**

```python
from unittest.mock import patch

class TestAPI(unittest.TestCase):
    @patch('modul.requests.get')
    def test_api_call(self, mock_get):
        mock_get.return_value.status_code = 200
        response = modul.api_call()
        self.assertEqual(response.status_code, 200)
```

### Skipping Tests

- Tests können übersprungen werden mit:
  - `@unittest.skip(reason)`
  - `@unittest.skipIf(condition, reason)`
  - `@unittest.skipUnless(condition, reason)`

**Beispiel:**

```python
@unittest.skip("Wird momentan nicht unterstützt")
def test_feature(self):
    pass
```

## Best Practices

- **Isolierte Tests:** Jeder Test sollte unabhängig von anderen Tests sein.
- **Aussagekräftige Namen:** Testmethoden sollten klar den getesteten Aspekt beschreiben.
- **Verwendung von Fixtures:** Gemeinsame Setup-/Teardown-Logik zentralisieren.
- **Regelmäßiges Ausführen:** Tests sollten häufig ausgeführt werden, z.B. bei jedem Commit.

## Zusammenfassung

- **`unittest`** ist ein leistungsfähiges Framework für automatisierte Tests in Python.
- Ermöglicht das Schreiben von **Testfällen** mit **Assertions**, **Test Fixtures** zur Vorbereitung und Reinigung sowie **Test Suites** zur Gruppierung von Tests.
- Unterstützt **Mocking** und das **Überspringen** von Tests für flexible Teststrategien.
- Förderung von **guter Testpraxis** durch klare Strukturierung und Isolierung von Tests.


# Anonyme Funktionen in Python: `lambda`-Ausdrücke

## Einführung in `lambda`-Ausdrücke

Lambda-Ausdrücke sind eine Möglichkeit, **anonyme Funktionen** in Python zu erstellen. Sie sind nützlich für kurze Funktionen, die nur einmal verwendet werden.

## Grundlegende Syntax

```python
f = lambda x: x * 2
print(f(3))  # Ausgabe: 6
```

Es können auch mehrere Argumente verwendet werden:

```python
g = lambda x, y: x + y
print(g(2, 3))  # Ausgabe: 5
```

---

## Unterschied zwischen `def` und `lambda`

### `def` ist eine Anweisung (Statement)
- Eine Anweisung führt eine **Aktion** aus und hat keinen Wert.
- Mit `def` wird ein **Objekt vom Typ `function`** erzeugt, die Definition selbst ist jedoch **kein Ausdruck**.
- Beispiel:
  ```python
  def ist_even(x):
      return x % 2 == 0

  print(ist_even(4))  # Ausgabe: True
  ```
  Hier ist die Funktion `ist_even` ein benanntes Objekt, das wiederverwendet werden kann.

---

### `lambda` ist ein Ausdruck (Expression)
- Ein Ausdruck hat **einen Wert** und kann direkt **ausgewertet** werden.
- `lambda` kann überall verwendet werden, wo ein **Ausdruck erwartet** wird, z. B. in Funktionen, Schleifen oder anderen Ausdrücken.
- Beispiel:
  ```python
  numbers = [1, 2, 3, 4, 5, 6]
  even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
  print(even_numbers)  # Ausgabe: [2, 4, 6]
  ```
  Hier wird der `lambda`-Ausdruck direkt innerhalb der `filter`-Funktion verwendet.

---

## Warum `lambda`-Ausdrücke?

- **Kürze:** Kompakte Darstellung von Funktionen.
- **Einfachheit:** Weniger Code und weniger Ablenkung.
- **Lesbarkeit:** Bei kurzen Funktionen klar und verständlich.
- **geringfügige Funktionen:** Ideal für **kurzlebige Funktionen**, z. B. für Transformationen und Filter.

---

## Einschränkungen von `lambda`
- `lambda` kann nur **einen einzigen Ausdruck** enthalten.
- Es ist nicht geeignet für komplexere Logik oder mehrere Anweisungen.
- Beispiel:
  ```python
  # Nicht möglich:
  # lambda x: if x > 0: print(x)  # SyntaxError
  ```

---

**Zusammenfassung**: `lambda`-Ausdrücke sind nützlich für kurze, einmalige Funktionen, während `def` für längere und komplexere Funktionsdefinitionen verwendet wird. Beide haben ihren Platz in Python und ergänzen sich je nach Anwendungsfall.


## `map()` Funktion

Die `map()` Funktion in Python wird verwendet, um eine Funktion auf jedes 
Element einer iterierbaren Objekt anzuwenden und das Ergebnis als neues 
iterables zurückzugeben.

#### Syntax
```python
map(function, iterable)
```

- **function**: Die Funktion, die auf jedes Element angewendet werden 
soll.
- **iterable**: Ein iterierbares Objekt (z.B. eine Liste, ein Tupel 
usw.), dessen Elemente mit der Funktion verarbeitet werden.

#### Beispiele

1. **Multiplizieren von Zahlen in einer Liste:**
   ```python
   def multiply_by_two(x):
       return x * 2

   numbers = [1, 2, 3, 4, 5]
   result = map(multiply_by_two, numbers)
   print(list(result))  # Output: [2, 4, 6, 8, 10]
   ```

2. **Umwandeln von Text in Großbuchstaben:**
   ```python
   def to_upper(text):
       return text.upper()

   words = ["hello", "world", "python"]
   result = map(to_upper, words)
   print(list(result))  # Output: ['HELLO', 'WORLD', 'PYTHON']
   ```

3. **Zwei Listen addieren:**
   ```python
   def add(a, b):
       return a + b

   list1 = [1, 2, 3]
   list2 = [4, 5, 6]
   result = map(add, list1, list2)
   print(list(result))  # Output: [5, 7, 9]
   ```

Wenn die funktion 1 Argument hat dann muss auch eine Iterierbare Objekt angegeben werden. Wenn die Funktion 2 Argumente hat dann müssen auch 2 Iterierbare Objekte angegeben werden.

also bei `map()` wird die Funktion auf jedes Element des Iterierbaren Objekts angewendet und das Ergebnis wird in einem neuen Iterierbaren Objekt zurückgegeben.

### Arten der Funktionen in map()

Es gibt verschiedene Arten von Funktionen, die mit `map()` verwendet werden können:
- **Benannte Funktionen:** Definierte Funktionen, die auf jedes Element angewendet werden.
- **Lambda-Funktionen:** Kurze, anonyme Funktionen, die direkt in `map()` verwendet werden können.
- **Methoden:** Methoden von Objekten können auch auf jedes Element angewendet werden.

#### Hinweise
- Die `map()` Funktion gibt ein map-Objekt zurück, das durch Iteration 
durchlaufen werden kann.
- Es ist wichtig, die Ergebnisse oft in eine Liste oder anderes iterables 
umzuwandeln, wenn man sie direkt verwenden möchte.

# Python: `filter`-Funktion

Die `filter`-Funktion ist ein eingebautes Werkzeug in Python, das verwendet wird, um Elemente aus einer iterierbaren Datenstruktur (wie Listen, Tupel, Sets etc.) basierend auf einer bestimmten Bedingung zu filtern. Sie arbeitet in Kombination mit einer Funktion, die eine Bedingung definiert.

## Unterschied zwischen `map` und `filter`

- **`map`**: Wird verwendet, um eine Funktion auf jedes Element einer iterierbaren Datenstruktur anzuwenden und die Ergebnisse zurückzugeben.
- **`filter`**: Wird verwendet, um eine Funktion auf jedes Element einer iterierbaren Datenstruktur anzuwenden und nur die Elemente zurückzugeben, für die die Funktion `True` zurückgibt.

## Syntax:
```python
filter(function, iterable)
```

- **`function`**: Eine Funktion, die auf jedes Element der `iterable` angewendet wird. Sie sollte `True` oder `False` zurückgeben.
- **`iterable`**: Eine Sammlung von Elementen (z. B. Liste, Tupel, Set), die gefiltert werden soll.

### Rückgabewert:
Ein **Iterator**, der nur die Elemente enthält, für die die `function` den Wert `True` zurückgibt.

---

## Beispiel 1: Gerade Zahlen filtern
```python
# Definieren einer Bedingungsfunktion
def is_even(number):
    return number % 2 == 0

# Liste von Zahlen
numbers = [1, 2, 3, 4, 5, 6]

# Filter anwenden
even_numbers = filter(is_even, numbers)

# Ergebnis in eine Liste umwandeln
print(list(even_numbers))  # Ausgabe: [2, 4, 6]
```

---

## Beispiel 2: Anonyme Funktion mit `lambda`
Anstatt eine separate Funktion zu definieren, kann man eine `lambda`-Funktion verwenden:
```python
numbers = [1, 2, 3, 4, 5, 6]

# Filter mit lambda
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # Ausgabe: [2, 4, 6]
```

---

## Beispiel 3: Strings filtern
Filtern von Wörtern, die mit einem bestimmten Buchstaben beginnen:
```python
words = ["apple", "banana", "cherry", "date", "apricot"]

# Wörter, die mit 'a' beginnen
words_starting_with_a = filter(lambda word: word.startswith('a'), words)

print(list(words_starting_with_a))  # Ausgabe: ['apple', 'apricot']
```

---

## Wichtige Hinweise:
1. **Iterator-Verhalten**: Die `filter`-Funktion gibt einen Iterator zurück. Um die Ergebnisse anzuzeigen, muss dieser in eine Liste oder ein anderes iterierbares Format umgewandelt werden (z. B. `list()`, `tuple()`).
2. **Unveränderte Originaldaten**: Die Originaldatenstruktur bleibt unverändert.
3. **Alternativen**: Für einfache Filteroperationen kann auch List Comprehension verwendet werden:
   ```python
   even_numbers = [x for x in numbers if x % 2 == 0]
   print(even_numbers)  # Ausgabe: [2, 4, 6]
   ```


# zip Funktion in Python

Die Zip funktion in Python kann verwendet werden, um zwei oder mehr Listen, Tupel oder andere Sequenzen zu kombinieren, indem sie Elemente paarweise in einer Liste von Tupeln zusammenfasst. Dies ist besonders

## Syntax
```python
zip(iterable1, iterable2, ...)
```

- **`iterable
- **`iterable2`**: Eine weitere Sequenz, die kombiniert werden soll.

### Rückgabewert

Ein **Iterator** von Tupeln, wobei das erste Element jedes Iterators zu einem Tupel zusammengefasst wird, das dann das erste Element des Ergebnisses ist.

---

## Beispiel 1: Kombinieren von Listen
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
names_and_ages = zip(names, ages)
print(list(names_and_ages))  # Ausgabe: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

## vorteile 

- **Kombination von Daten**: Ermöglicht die Kombination von Daten aus verschiedenen Quellen.
- **Effizienz**: Spart Speicherplatz, da es nur Tupel von Referenzen auf die ursprünglichen Daten erstellt.
- **Einfachheit**: Einfache Syntax und Verwendung.

# Virtuelle Umgebungen in Python: `venv`

Virtuelle Umgebungen (venvs) ermöglichen es, Python-Projekte voneinander zu isolieren, sodass jedes Projekt seine eigenen Abhängigkeiten und Bibliotheken hat.


Ein virtuelle Umgebung in Python ist ein isolierter Bereich, in dem Python-Pakete installiert werden können, ohne das System-Python oder andere Projekte zu beeinflussen. Dies ermöglicht es, verschiedene Projekte mit unterschiedlichen Paketversionen zu entwickeln, ohne Konflikte zu verursachen.

Es diehnt außerdem zur verbesserung der Sicherheit, da es verhindert, dass Pakete auf Systemebene installiert werden, die möglicherweise das System beeinträchtigen könnten.


## Virtuelle Umgebung erstellen

1. **Neue virtuelle Umgebung erstellen**:
   ```bash
   python3 -m venv meine_venv
   ```
   - `meine_venv` ist der Name der Umgebung (kann beliebig gewählt werden).

2. **Inhalt der virtuellen Umgebung**:
   - `bin/` (oder `Scripts/` auf Windows): Enthält ausführbare Dateien.
   - `lib/`: Speichert installierte Pakete.

---

## Virtuelle Umgebung aktivieren

1. **Auf Linux/macOS**:
   ```bash
   source meine_venv/bin/activate
   ```
2. **Auf Windows**:
   ```cmd
   meine_venv\Scripts\activate
   ```

Nach der Aktivierung siehst du den Namen der Umgebung in deinem Terminal:
```
(meine_venv) $
```

---

## Pakete in der venv installieren

Installiere Abhängigkeiten nur innerhalb der virtuellen Umgebung:
```bash
pip install requests
```

Überprüfen der installierten Pakete:
```bash
pip list
```

---

## Virtuelle Umgebung deaktivieren

Um die virtuelle Umgebung zu verlassen:
```bash
deactivate
```


## Beispiel-Skript mit einer venv

1. **Virtuelle Umgebung erstellen und aktivieren**:
   ```bash
   python3 -m venv projekt_env
   source projekt_env/bin/activate
   ```

2. **Ein Paket installieren**:
   ```bash
   pip install flask
   ```

3. **Ein Python-Skript erstellen**:
   ```python
   # app.py
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Hello, venv!"

   if __name__ == '__main__':
       app.run(debug=True)
   ```

4. **Das Skript ausführen**:
   ```bash
   python app.py
   ```

5. **Virtuelle Umgebung deaktivieren**:
   ```bash
   deactivate
   ```
---

# Objektorientierte Programmierung (OOP) in Python

Die objektorientierte Programmierung (OOP) ist ein Paradigma, das Programme strukturiert, indem verwandte Eigenschaften und Verhaltensweisen in einzelnen Objekten gebündelt werden. In Python wird OOP durch Klassen und Objekte realisiert.

**Definition einer Klasse:**
Eine Klasse dient als Blaupause für Objekte. Sie definiert Attribute (Eigenschaften) und Methoden (Verhaltensweisen), die die Objekte besitzen. In Python wird eine Klasse mit dem Schlüsselwort `class` definiert:

```python
class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
```

Hierbei ist `__init__` eine spezielle Methode, die als Konstruktor dient und beim Erstellen eines neuen Objekts aufgerufen wird. Das `self`-Argument referenziert die Instanz des Objekts selbst.

**Instanziierung einer Klasse:**
Um ein Objekt (Instanz) einer Klasse zu erstellen, ruft man die Klasse wie eine Funktion auf:

```python
mein_hund = Hund("Bello", 3)
```

Nun kann auf die Attribute und Methoden des Objekts zugegriffen werden:

```python
print(mein_hund.name)  # Ausgabe: Bello
print(mein_hund.alter)  # Ausgabe: 3
```

### Vererbung:
Python unterstützt die Vererbung, wodurch eine neue Klasse (Kindklasse) Eigenschaften und Methoden einer bestehenden Klasse (Elternklasse) erben kann:

```python
class Schäferhund(Hund):
    def __init__(self, name, alter, trainingsstand):
        super().__init__(name, alter)
        self.trainingsstand = trainingsstand
```

Hierbei ruft `super().__init__(name, alter)` den Konstruktor der Elternklasse auf, um die geerbten Attribute zu initialisieren.

#### super() Funktion

Die `super()` Funktion wird verwendet, um auf die Methoden und Attribute der Elternklasse zuzugreifen. Sie wird häufig in der `__init__`-Methode der Kindklasse verwendet, um die Initialisierung der geerbten Attribute zu unterstützen. 

**WICHTIG:** `super()` ìst nur eine Referenz auf die Elternklasse und nicht die Elternklasse selbst.


## Einfach- und Mehrfachvererbung

In python kann man anders als in Java auch von mehreren Klassen erben. 

```python
class A:
    pass

class B(A):     # B erbt von A -> Einfachvererbung
    pass

class C(A, B):  # C erbt von A und B in einem schritt -> Mehrfachvererbung
    pass
```



## die Dunder Methoden

- **`__init__`:** Konstruktor, der beim Erstellen eines Objekts aufgerufen wird.
- **`__str__`:** Gibt eine lesbare Darstellung des Objekts zurück (z. B. für `print`).
- **`__repr__`:** Gibt eine unmissverständliche Darstellung des Objekts zurück. also so wie man es eingeben würde. z. B.:
```python 
objekt = Hund("Bello", 3)
print(__repr__) # Ausgabe: Hund("Bello", 3)
```
- **`__eq__`:** Definiert die Gleichheit von Objekten (verwendet `==`).
- **`__lt__`, `__gt__`, `__le__`, `__ge__`: Vergleichsoperatoren.
- **`__add__`, `__sub__`, `__mul__`, `__truediv__`: Arithmetische Operatoren.

**Zusammenfassung:**
Die objektorientierte Programmierung in Python ermöglicht es, Programme modular und übersichtlich zu gestalten, indem Daten und Funktionen, die auf diese Daten wirken, in Klassen und Objekten zusammengefasst werden. Dies fördert die Wiederverwendbarkeit und Wartbarkeit des Codes. 


## **MRO (Method Resolution Order)**

- **MRO** (Method Resolution Order) ist der Algorithmus, den Python verwendet, um die Reihenfolge zu bestimmen, in der Methoden und Attribute in einer Klassenhierarchie aufgelöst werden, insbesondere bei Mehrfachvererbung.
- Die MRO gibt an, welche Klasse zuerst durchsucht wird, wenn eine Methode oder ein Attribut angefordert wird.

### **Funktionsweise**
MRO definiert die Reihenfolge der Klassen, die durchsucht werden, wenn auf eine Methode oder ein Attribut zugegriffen wird. Python verwendet dazu den **C3-Linearisierungsalgorithmus**, um sicherzustellen, dass die Reihenfolge konsistent ist und Konflikte in Mehrfachvererbungen vermieden werden.

### **Beispiel: MRO in Aktion**

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# MRO anzeigen
print(D.mro())
```

In diesem Beispiel ist die **MRO** für die Klasse `D`:
```plaintext
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

Das bedeutet:
1. Zuerst wird in `D` gesucht.
2. Falls nicht gefunden, wird `B` durchsucht.
3. Danach wird `C` durchsucht.
4. Schließlich wird `A` und zuletzt die Basisklasse `object` durchsucht.

### **MRO und `super()`**
- Die Methode `super()` ruft die nächste Klasse in der MRO auf.
- Dadurch wird die Reihenfolge der MRO eingehalten, auch wenn Mehrfachvererbung verwendet wird.

### **Anzeige der MRO**
Die MRO einer Klasse kann auf zwei Arten angezeigt werden:
1. **Mit der Methode `mro()`:**
   ```python
   print(D.mro())
   ```
2. **Mit der Funktion `help()`:**
   ```python
   help(D)
   ```

---

## **Proxies**

Ein **Proxy** ist eine Zwischenschicht zwischen einem Client (z. B. einem Nutzer oder einer Anwendung) und einem Objekt. Der Proxy kann verwendet werden, um den Zugriff auf das Objekt zu kontrollieren oder zusätzliche Funktionalität hinzuzufügen.

### **Beispiel: Proxy-Klasse**

```python
class Proxy:
    def __init__(self, obj):
        self._obj = obj  # Referenz auf das echte Objekt

    def __getattr__(self, name):
        # Zugriff auf Attribute des echten Objekts
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):  # Schutz für interne Attribute
            super().__setattr__(name, value)
        else:
            # Setzen von Attributen des echten Objekts
            setattr(self._obj, name, value)
```

### **Erklärung des Codes**
1. **`__init__`**:
   - Speichert eine Referenz auf das "echte" Objekt im Proxy.

2. **`__getattr__`**:
   - Leitet alle Attributzugriffe, die nicht auf dem Proxy definiert sind, an das echte Objekt weiter.

3. **`__setattr__`**:
   - Kontrolliert, wie Attribute auf dem echten Objekt gesetzt werden:
     - Interne Attribute (`_obj`) werden direkt im Proxy gespeichert.
     - Andere Attribute werden auf dem echten Objekt gespeichert.

### **Anwendungsbeispiel**
```python
class RealObject:
    def __init__(self):
        self.value = 42

    def show_value(self):
        print(f"Value is {self.value}")

# Proxy verwenden
real = RealObject()
proxy = Proxy(real)

proxy.show_value()  # Zugriff über den Proxy
proxy.value = 100   # Ändert das Attribut im echten Objekt
proxy.show_value()
```

### **Anwendung von Proxies**
- **Zugriffskontrolle**: Einschränkung oder Erlaubnis des Zugriffs auf bestimmte Methoden oder Attribute.
- **Logging**: Protokollierung von Attributänderungen oder Methodenaufrufen.
- **Caching**: Zwischenspeicherung von häufig genutzten Daten, um die Leistung zu verbessern.
- **Lazy Initialization**: Verzögerte Initialisierung eines Objekts, bis es tatsächlich benötigt wird.

---

## **Zusammenfassung**

### **MRO**
- **Definition**: Reihenfolge, in der Python nach Methoden oder Attributen in einer Klassenhierarchie sucht.
- **Verwendung**: Bestimmt durch den C3-Linearisierungsalgorithmus.
- **Tools**: `mro()` oder `help()` zur Anzeige.

### **Proxies**
- **Definition**: Ein Proxy ist ein Wrapper für ein Objekt, der den Zugriff darauf kontrolliert.
- **Nutzen**:
  - Logging.
  - Zugriffskontrolle.
  - Zwischenspeicherung (Caching).
  - Lazy Initialization.
- **Beispiel**: Verwenden von `__getattr__` und `__setattr__`, um Attribute an das echte Objekt weiterzuleiten.


# Fehlerbehandlung

## Zwei arten von Strategien

### LBYL (Look Before You Leap)

Bei dieser Methode verwenden wir if else Bedingungen, um zu überprüfen, ob eine Operation sicher ausgeführt werden kann, bevor sie tatsächlich ausgeführt wird. Dies bedeutet, dass wir vor dem Ausführen einer Operation prüfen, ob sie erfolgreich sein wird.

### EAFP (Easier to Ask for Forgiveness than Permission)

Bei dieser Methode gehen wir davon aus, dass die Operation erfolgreich sein wird, und fangen Ausnahmen ab, wenn sie auftreten. Dies bedeutet, dass wir die Operation einfach ausführen und im Fehlerfall darauf reagieren.

## Zwei Arten von Fehlern

### neue errors

### hoch"geblubberte" errors





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

