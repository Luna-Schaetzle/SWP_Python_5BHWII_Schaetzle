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

# Erste Aufgabe: Lottoziehung

## Aufgabenstellung

1. Algorithmus zur Lottoziehung -> keine doppelten Zahlen. Wird in einer Methode gemacht. Ziehe 6 Zahlen zwischen 1 und 45 und gib sie aus. Passendes Programm: `lotto_1.py`
2. Lottoziehung Statistik als Methode ->
    - Mache 1000 Ziehungen
    - Erstelle ein Dictionary, wie oft welche Zahl gezogen wurde
    - Rufe die Methode nach jeder Ziehung auf und inkrementiere den passenden Wert im Dictionary um 1
    - Gib das Dictionary am Ende aus
    - Passendes Programm: `lotto_2.py`

