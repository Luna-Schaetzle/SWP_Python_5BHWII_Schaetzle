# Mitschrift

# Inhaltsverzeichnis

## 1. Einführung in Python
1.1. Eigenschaften von Python  
1.2. Plattformunabhängigkeit  
1.3. Interpretierte Sprache  
1.4. Hochsprache  
1.5. Bytecode in Python  
1.6. Standardbibliotheken und Module  
1.7. Rapid Prototyping  
1.8. Verschiedene Arten von Python-Interpretern
   - 1.8.1. CPython
   - 1.8.2. Jython
   - 1.8.3. IronPython

## 2. Python-Installation und -Umgebung
2.1. Installation von Python  
2.2. Python-Umgebungen einrichten  
2.3. Programmendung `.py`
   - 2.3.1. Shebang
   - 2.3.2. Unterschiedliche Dateitypen
   - 2.3.3. Bedeutung von Tabs in Python
   - 2.3.4. Kommentare
2.4. Python Interaktiver Modus  
2.5. Entwicklungswerkzeuge und IDEs

## 3. Grundlegende Syntax und Datentypen
3.1. Datentypen in Python
   - 3.1.1. Ganze Zahlen (`int`)
   - 3.1.2. Division zweier ganzer Zahlen
   - 3.1.3. Floor Division in Python
3.2. Immutable vs. Mutable Datentypen
   - 3.2.1. Immutable Datentypen
   - 3.2.2. Mutable Datentypen
   - 3.2.3. Copy und Deepcopy
3.3. Sequenzielle Datentypen
   - 3.3.1. Listen
   - 3.3.2. Tupel
   - 3.3.3. Dictionary
   - 3.3.4. Sets
   - 3.3.5. List Comprehension
   - 3.3.6. Dictionary Comprehension
   - 3.3.7. Range
3.4. Auswertungsreihenfolge der Operatoren

## 4. Variablen und Referenzen
4.1. Instanzen und Referenzen  
4.2. Referenz / Instanz (Identität, Wert und Typ)
   - 4.2.1. Identität
   - 4.2.2. Problem des Seiteneffekts
4.3. Python `isinstance()` Funktion

## 5. Kontrollstrukturen
5.1. Bedingungen und Verzweigungen (`if`, `elif`, `else`)  
5.2. Iteration
   - 5.2.1. Best Practices bei `for`-Schleifen
5.3. Rekursion

## 6. Funktionen und Module
6.1. Funktionen definieren und verwenden  
6.2. DUNDER (Double Under) Methoden  
6.3. Programm einfügen `__name__ == "__main__"`  
6.4. Module importieren und verwenden

## 7. Datenstrukturen und Algorithmen
7.1. Arrays und Listen
   - 7.1.1. Arrays
   - 7.1.2. Linked Lists
   - 7.1.3. Array Lists
7.2. Zeitkomplexität
   - 7.2.1. Big-O-Notation
   - 7.2.2. Analyse der Zeitkomplexität in Python
   - 7.2.3. Beispiele für Zeitkomplexität in Python
   - 7.2.4. Bedeutung der Zeitkomplexität

## 8. Vergleich Python und Java
8.1. Typisierung  
8.2. Programmierparadigmen  
8.3. Speicherverwaltung und Garbage Collection  
8.4. Speicherfreigabe  

## 9. Fortgeschrittene Konzepte
9.1. Unterschied zwischen Prozess und Thread  
9.2. Unterschied zwischen Immutable und Mutable Datentypen  
9.3. DUNDER (Double Under) Methoden  
9.4. Exception Handling in Python
   - 9.4.1. Raise Exception  

## 10. Objektorientierte Programmierung
10.1. Klassen und Objekte  
10.2. Vererbung und Polymorphismus  
10.3. Encapsulation und Abstraktion  

## 11. Laufzeitmodell und Performance
11.1. Laufzeitenmodell in Python  
11.2. Time Complexity
   - 11.2.1. Big-O-Notation
   - 11.2.2. Analyse der Zeitkomplexität in Python
   - 11.2.3. Beispiele für Zeitkomplexität in Python
   - 11.2.4. Bedeutung der Zeitkomplexität

## 12. Python-Interpreter und Implementierungen
12.1. Verschiedene Arten von Python-Interpretern
   - 12.1.1. CPython
   - 12.1.2. Jython
   - 12.1.3. IronPython

## 13. Best Practices und Weiterführendes
13.1. Best Practices beim Programmieren mit Python  
13.2. Python `isinstance()` Funktion  
13.3. Sequenzielle Datentypen Zusammenfassung  
13.4. Schlüsselwörter in Python  

## 14. Anhang und Ergänzungen
14.1. Glossar  
14.2. Referenzen und weiterführende Literatur  
14.3. Beispiele und Übungen  

# 1. Einführung in Python

Python ist eine plattformunabhängige, interpretierte und hochabstrakte Programmiersprache. Diese Eigenschaften machen Python vielseitig und leicht zugänglich für Entwickler.

## 1.1. Eigenschaften von Python

Python ist eine vielseitige Programmiersprache, die für verschiedene Anwendungsbereiche geeignet ist. Die wichtigsten Eigenschaften von Python sind:
    - Einfachheit und Lesbarkeit
    - Vielseitigkeit und Flexibilität
    - Plattformunabhängigkeit
    - Interpretiertheit
    - Hochsprachigkeit
    - Modularität und Wiederverwendbarkeit
    - Objektorientierung
    - Dynamische Typisierung
    - Automatische Speicherverwaltung

## 1.2. Plattformunabhängigkeit
**Plattformunabhängig** bedeutet, dass Python auf allen gängigen Betriebssystemen (Windows, Linux, macOS) läuft. Einmal geschriebener Code kann ohne Anpassungen auf verschiedenen Systemen ausgeführt werden.

## 1.3. Interpretierte Sprache
Python ist eine **interpretierte Sprache**, d.h. der Code wird zur Laufzeit direkt interpretiert, anstatt vorab in Maschinencode (wie bei kompilierte Sprachen) übersetzt zu werden. Dies ermöglicht eine direkte Ausführung des Codes ohne Zwischenschritte.


**Beispiele für Interpreter Sprachen:**
- Python
- php 
- Ruby

**Unterschied zwischen interpretierten und kompilierten Sprachen**
- **Kompilierte Sprachen:** Der Code wird vor dem Ausführen in Maschinencode übersetzt, was zu einer schnelleren Ausführung führen kann. Beispiele: C, C++, Java.
- **Interpretierte Sprachen:** Der Code wird zur Laufzeit interpretiert, was eine flexiblere und dynamischere Entwicklung ermöglicht. Beispiele: Python, JavaScript, Ruby.



## 1.4. Hochsprache
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


## 1.5. Bytecode in Python

Obwohl Python interpretiert wird, gibt es sogenannte **Bytecode-Dateien** (mit der Endung `.pyc`), die beim Speichern von Python-Dateien erstellt werden. Diese Dateien enthalten eine kompilierte Version des Codes, die bei späteren Ausführungen die Startzeit verkürzen kann. Python kann den Code jedoch auch ohne diese Bytecode-Dateien ausführen.

**Beispiel
```python
# Beispiel für Bytecode in Python
def add(a, b):
    return a + b

# Erstellen einer Bytecode-Datei
# python -m py_compile script.py
```

## 1.6. Standardbibliotheken und Module

**Umfangreiche Standardbibliotheken:** Python bietet eine Vielzahl vorinstallierter Module, die häufige Programmieraufgaben abdecken (z.B. für Dateioperationen, Netzwerke, Webentwicklung). Im Vergleich zu Sprachen wie Java oder C# ist die Installation und Nutzung von Bibliotheken in Python besonders einfach.
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

## 1.7. Rapid Prototyping

Python eignet sich sehr gut für **Rapid Prototyping**, da es in der Regel weniger Code benötigt, um eine Lösung zu implementieren, verglichen mit Sprachen wie Java. Dies macht Python besonders nützlich für schnelle Entwicklungszyklen.

## 1.8. Verschiedene Arten von Python-Interpretern


Es gibt verschiedene Arten von Python-Interpretern, die für unterschiedliche Zwecke und Anwendungen entwickelt wurden. Hier sind einige der bekanntesten Python-Interpretern:

### 1.8.1. CPython
   - CPython ist der Standard-Interpreter für Python und wird von der Python-Software-Stiftung entwickelt. Er ist in C geschrieben und implementiert die offizielle Python-Spezifikation. CPython ist die am weitesten verbreitete Implementierung von Python und wird für die meisten Anwendungen verwendet.
### 1.8.2. Jython
   - Jython ist eine Implementierung von Python, die in Java geschrieben ist und auf der Java Virtual Machine (JVM) ausgeführt wird. Jython ermöglicht die nahtlose Integration von Python-Code in Java-Anwendungen und umgekehrt.
### 1.8.3. IronPython
   - IronPython ist eine Implementierung von Python, die in C# geschrieben ist und auf der .NET-Plattform ausgeführt wird. IronPython ermöglicht die Integration von Python-Code in .NET-Anwendungen und umgekehrt.


# 2. Python-Installation und -Umgebung

Python kann auf verschiedenen Betriebssystemen installiert werden, darunter Windows, Linux und macOS. Die Installation von Python ist in der Regel einfach und erfordert nur wenige Schritte. Unter manchen Linux Distributionen ist Python bereits vorinstalliert.

## 2.1. Installation von Python

Python kann von der offiziellen Python-Website heruntergeladen und installiert werden. Es wird empfohlen, die neueste Version von Python zu verwenden, um von den neuesten Funktionen und Verbesserungen zu profitieren.

**Schritte zur Installation von Python:**
1. **Herunterladen von Python:**  
   - Python kann von der offiziellen Python-Website heruntergeladen werden: [python.org](https://www.python.org/downloads/).
2. **Installation von Python:**
    - Windows: Doppelklicken Sie auf die heruntergeladene Installationsdatei und folgen Sie den Anweisungen des Installationsassistenten.
    - Linux: Python kann über den Paketmanager der Linux-Distribution installiert werden (z.B. `apt-get install python3`).
    - macOS: Python kann über Homebrew oder MacPorts installiert werden.
3. **Überprüfen der Installation:**
    - Öffnen Sie ein Terminal oder eine Eingabeaufforderung und geben Sie `python --version` ein, um die installierte Python-Version anzuzeigen.
    ```bash
    python --version
    Python 3.9.7
    ```

## 2.2. Python-Umgebungen einrichten

In python wird empfohlen, eine **virtuelle Umgebung** für jedes Projekt zu erstellen, um Abhängigkeiten und Pakete zu isolieren. Dies verhindert Konflikte zwischen verschiedenen Projekten und erleichtert die Verwaltung von Abhängigkeiten. Es gibt verschiedene Tools, um virtuelle Umgebungen in Python zu erstellen, darunter `venv`, `virtualenv` und `conda`.

Es wird empfohlen, `venv` zu verwenden, da es in Python 3 integriert ist und eine einfache Möglichkeit bietet, virtuelle Umgebungen zu erstellen.

**Schritte zur Erstellung einer virtuellen Umgebung mit `venv`:**

1. **Erstellen einer virtuellen Umgebung:**
    - Öffnen Sie ein Terminal oder eine Eingabeaufforderung und navigieren Sie zum Projektordner.
    - Erstellen Sie eine virtuelle Umgebung mit dem Befehl `python -m venv <env_name>`.
    ```bash
    python -m venv myenv
    ```
2. **Aktivieren der virtuellen Umgebung:**
    - Aktivieren Sie die virtuelle Umgebung mit dem Befehl `source <env_name>/bin/activate` (Linux/macOS) oder `<env_name>\Scripts\activate` (Windows).
    ```bash
    source myenv/bin/activate
    ```
3. **Deaktivieren der virtuellen Umgebung:**
    - Deaktivieren Sie die virtuelle Umgebung mit dem Befehl `deactivate`.
    ```bash
    deactivate
    ```
4. **Installieren von Paketen in der virtuellen Umgebung:**
    - Installieren Sie Pakete in der virtuellen Umgebung mit `pip install <package>`.
    ```bash
    pip install requests
    ```

## 2.3. Programmendung `.py`

Dateiendungen sind in der Informatik wichtig, da sie anzeigen, um welchen Dateityp es sich handelt und welches Programm verwendet werden soll, um die Datei zu öffnen. In Python haben Dateien mit der Endung `.py` eine besondere Bedeutung, da sie Python-Skripte enthalten. Python-Skripte sind Textdateien, die Python-Code enthalten und mit dem Python-Interpreter ausgeführt werden können. 

### 2.3.1. Shebang


Der Shebang ist eine spezielle Zeile am Anfang einer Datei, die dem Betriebssystem mitteilt, welcher Interpreter verwendet werden soll, um die Datei auszuführen. In Python-Skripten wird oft der Shebang `#!/usr/bin/env python3` verwendet, um den Python-Interpreter zu starten.

Damit weiß das Betriebssystem, dass es den Python-Interpreter verwenden soll, um das Skript auszuführen. Der Shebang ist optional, aber empfohlen, da er die Ausführung des Skripts erleichtert. 

Nach dem `#!` wird der Pfad zum Python-Interpreter angegeben, in diesem Fall `python3`. Das `env`-Programm sucht nach dem Python-Interpreter im System und verwendet die Version, die standardmäßig installiert ist.

### 2.3.2. Unterschiedliche Dateitypen


In einer **.exe** steht für eine ausführbare Datei. Diese Dateien können direkt ausgeführt werden, ohne dass ein spezielles Programm benötigt wird. Da dort Maschienen Code drinnen ist.

In einer **.txt** steht für eine Textdatei. Diese Dateien enthalten Text und können mit einem Texteditor geöffnet und bearbeitet werden. Da stehen nur Text drinnen.
Es gibt auch andere Textdateien wie .docx oder .pdf die aber nicht so einfach zu öffnen sind, aber auch Programmdateien sind textdateien wie .py oder .java. Diese müssen erst Interpretiert werden. 

### 2.3.3. Bedeutung von Tabs in Python


In manchen Programmiersprachen sind Tabs nicht wichtig, aber in Python sind sie sehr wichtig. Tabs werden in Python verwendet, um Blöcke von Code zu definieren, z.B. in Schleifen oder Funktionen. Wenn die Einrückung nicht korrekt ist, wird ein IndentationError ausgelöst.

In Python 3 ist ein Tab als 4 Leerzeichen definiert. Das bedeutet, dass ein Tab durch 4 Leerzeichen ersetzt wird. Es ist wichtig, konsistent zu sein und entweder Tabs oder Leerzeichen zu verwenden, aber nicht beides gemischt.

### 2.3.4. Kommentare


Kommentare macht man mit einem `#` in Python. Kommentare sind nützlich, um den Code zu dokumentieren und zu erklären, was er tut. Kommentare werden vom Interpreter ignoriert und haben keinen Einfluss auf die Ausführung des Codes.

```python
# Dies ist ein Kommentar
print("Hallo Welt")  # Dies ist auch ein Kommentar
```

## 2.4. Python Interaktiver Modus

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

## 2.5. Entwicklungswerkzeuge und IDEs

Es gibt viele Entwicklungswerkzeuge und integrierte Entwicklungsumgebungen (IDEs), die die Arbeit mit Python erleichtern. Zu den beliebtesten gehören:

- **PyCharm:** Eine leistungsstarke IDE von JetBrains, die viele Funktionen wie Code-Vervollständigung, Debugging, und Versionskontrolle bietet.
- **Visual Studio Code:** Ein leichtgewichtiger, aber funktionsreicher Editor von Microsoft, der durch Erweiterungen an die Bedürfnisse von Python-Entwicklern angepasst werden kann.
- **Jupyter Notebook:** Ein interaktives Web-Tool, das besonders für Datenanalyse und maschinelles Lernen nützlich ist.
- **Spyder:** Eine IDE, die speziell für wissenschaftliches und datenwissenschaftliches Arbeiten mit Python entwickelt wurde.
- **IDLE:** Die integrierte Entwicklungsumgebung, die mit Python ausgeliefert wird und sich gut für Einsteiger eignet.

Die Wahl des richtigen Werkzeugs hängt von den individuellen Anforderungen und Vorlieben ab. Es ist oft hilfreich, mehrere Tools auszuprobieren, um dasjenige zu finden, das am besten zu den eigenen Arbeitsabläufen passt.

# 3. Grundlegende Syntax und Datentypen

Die Syntax von Python ist einfach und leicht zu erlernen, was es zu einer beliebten Programmiersprache für Anfänger macht. Python verwendet Einrückungen, um Blöcke von Code zu definieren, und hat eine klare und konsistente Syntax. In diesem Abschnitt werden die grundlegenden Datentypen und ihre Verwendung in Python behandelt.

## 3.1. Datentypen in Python

Python ist eine dynamisch typisierte Sprache, was bedeutet, dass der Typ einer Variablen automatisch erkannt wird. Es gibt verschiedene Datentypen in Python, darunter:
- **Ganze Zahlen (`int`)**: Repräsentieren ganze Zahlen ohne Dezimalstellen.
- **Gleitkommazahlen (`float`)**: Repräsentieren Zahlen mit Dezimalstellen.
- **Zeichenketten (`str`)**: Repräsentieren Textdaten.
- **Boolesche Werte (`bool`)**: Repräsentieren Wahrheitswerte (`True` oder `False`).
- **Listen (`list`)**: Repräsentieren geordnete Sammlungen von Elementen.
- **Tupel (`tuple`)**: Repräsentieren geordnete, unveränderliche Sammlungen von Elementen.
- **Wörterbücher (`dict`)**: Repräsentieren Sammlungen von Schlüssel-Wert-Paaren.
- **Mengen (`set`)**: Repräsentieren ungeordnete Sammlungen von eindeutigen Elementen.

## 3.2 Division zweier ganzer Zahlen & Floor Division in Python

In Python gibt es zwei Arten der Division: die normale Division (`/`) und die Ganzzahldivision (`//`). Die normale Division gibt das Ergebnis als Gleitkommazahl zurück, während die Ganzzahldivision das Ergebnis auf die nächstkleinere ganze Zahl abrundet.

```python
# Normale Division
result1 = 7 / 2  # Ergebnis: 3.5
result2 = 10 / 3  # Ergebnis: 3.3333333333333335

# Ganzzahldivision
result3 = 7 // 2  # Ergebnis: 3
result4 = 10 // 3  # Ergebnis: 3
```

Es wird also bei der Ganzzahldivision immer abgerundet. Diesen vorgang nennen wir auch **Floor Division**.

## 3.3. Immutable vs. Mutable Datentypen

### 3.3.1 Immutable Datentypen

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

### 3.3.2 Mutable Datentypen

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


### 3.3.3. Copy und Deepcopy

In Python gibt es zwei Möglichkeiten, Kopien von Datenstrukturen zu erstellen: `copy` und `deepcopy`. Beide Methoden ermöglichen es, eine Kopie einer Datenstruktur zu erstellen, aber es gibt einen wichtigen Unterschied zwischen ihnen.

#### 3.3.3.1. Copy

```python
import copy

liste = [1, 2, 3]
liste2 = copy.copy(liste)
liste2.append(4)
print(liste)  # Ausgabe: [1, 2, 3], die Liste wurde nicht verändert
```

Somit wird der seiten Effekt umgangen.

#### 3.3.3.2. Deepcopy

```python
import copy

liste = [1, 2, 3, [4, 5]]
liste2 = copy.deepcopy(liste)
liste2[4] = 6
print(liste)  # Ausgabe: [1, 2, 3, [4, 5]], die Liste wurde nicht verändert
```
Wenn wir nur copy angewändet hätten, dann wäre die Liste verändert worden.

## 3.4. Sequenzielle Datentypen

Sequenzielle Datentypen sind Datentypen, die eine geordnete Sammlung von Elementen enthalten. In Python gibt es mehrere sequenzielle Datentypen, darunter Listen, Tupel, Strings und Sets.

### 3.3.1. Listen

Listen sind veränderbare, geordnete Sammlungen von Elementen. Sie können Elemente beliebigen Typs enthalten und ihre Größe dynamisch ändern. Listen werden mit eckigen Klammern `[]` definiert.

```python
# Beispiel für eine Liste
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Ausgabe: ['apple', 'banana', 'cherry']

# Hinzufügen eines Elements
fruits.append("orange")
print(fruits)  # Ausgabe: ['apple', 'banana', 'cherry', 'orange']

# Entfernen eines Elements
fruits.remove("banana")
print(fruits)  # Ausgabe: ['apple', 'cherry', 'orange']
```

### 3.3.2. Tupel

Tupel sind unveränderliche, geordnete Sammlungen von Elementen. Einmal erstellt, können ihre Elemente nicht mehr geändert werden. Tupel werden mit runden Klammern `()` definiert.

```python
# Beispiel für ein Tupel
coordinates = (10.0, 20.0)
print(coordinates)  # Ausgabe: (10.0, 20.0)

# Zugriff auf Elemente
print(coordinates[0])  # Ausgabe: 10.0
```

### 3.3.3. Dictionary

Dictionaries sind veränderbare, ungeordnete Sammlungen von Schlüssel-Wert-Paaren. Sie ermöglichen den schnellen Zugriff auf Werte anhand ihrer Schlüssel. Dictionaries werden mit geschweiften Klammern `{}` definiert.

```python
# Beispiel für ein Dictionary
person = {"name": "Alice", "age": 30}
print(person)  # Ausgabe: {'name': 'Alice', 'age': 30}

# Hinzufügen eines Schlüssel-Wert-Paares
person["city"] = "New York"
print(person)  # Ausgabe: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Zugriff auf einen Wert
print(person["name"])  # Ausgabe: Alice
```

### 3.3.4. Sets

Sets sind veränderbare, ungeordnete Sammlungen von eindeutigen Elementen. Sie werden mit geschweiften Klammern `{}` definiert.

```python
# Beispiel für ein Set
numbers = {1, 2, 3, 4}
print(numbers)  # Ausgabe: {1, 2, 3, 4}

# Hinzufügen eines Elements
numbers.add(5)
print(numbers)  # Ausgabe: {1, 2, 3, 4, 5}

# Entfernen eines Elements
numbers.remove(3)
print(numbers)  # Ausgabe: {1, 2, 4, 5}
```

### 3.3.5. List Comprehension

List Comprehensions sind eine kompakte Möglichkeit, Listen zu erstellen. Sie ermöglichen es, Listen auf Basis bestehender Listen zu erstellen und dabei Bedingungen und Schleifen zu verwenden.

```python
# Beispiel für List Comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Ausgabe: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 3.3.6. Dictionary Comprehension

Dictionary Comprehensions sind eine kompakte Möglichkeit, Dictionaries zu erstellen. Sie ermöglichen es, Dictionaries auf Basis bestehender Listen oder Dictionaries zu erstellen und dabei Bedingungen und Schleifen zu verwenden.

```python
# Beispiel für Dictionary Comprehension
squares = {x: x**2 for x in range(10)}
print(squares)  # Ausgabe: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

### 3.3.7. Range

Der `range()`-Funktion wird verwendet, um eine Sequenz von Zahlen zu erzeugen. Sie wird häufig in Schleifen verwendet, um eine bestimmte Anzahl von Iterationen zu durchlaufen.

```python
# Beispiel für range()
for i in range(5):
    print(i)
# Ausgabe:
# 0
# 1
# 2
# 3
# 4
```

## 3.4. Auswertungsreihenfolge der Operatoren


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

# 4. Variablen und Referenzen

## 4.1. Instanzen und Referenzen

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

## 4.2. Referenz / Instanz (Identität, Wert und Typ) 

### 4.2.1. Identität

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


### 4.2.2. Problem des Seiteneffekts

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

#### Es ergibt sich folgendes:

Bei Datenstruckturen werden eigentlich nur Referenzen auf die Daten gespeichert. Das bedeutet das keine Daten gespeichert werden sondern nur die Referenzen auf die Daten. Das bedeutet das wenn wir eine Liste auf eine andere Liste setzen, dann haben sie die gleiche Identität. Das führt dazu das wenn wir eine Liste ändern, dann ändert sich auch die andere L


## 4.3. Python `isinstance()` Funktion


[Python isinstance() Funktion Beschreibung](https://www.programiz.com/python-programming/methods/built-in/isinstance)

Die `isinstance()` Funktion wird verwendet, um zu überprüfen, ob ein Objekt einer bestimmten Klasse oder einem bestimmten Datentyp entspricht. Die Funktion gibt `True` zurück, wenn das Objekt der angegebenen Klasse oder dem angegebenen Datentyp entspricht, andernfalls gibt sie `False` zurück.

**Syntax**

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

**Praktische Anwendung**

Da wir in Pyhton listen gemischt verwenden können, ist es manchmal nützlich zu überprüfen, ob ein Objekt einer bestimmten Klasse oder einem bestimmten Datentyp entspricht. Das kann uns helfen, Fehler zu vermeiden und sicherzustellen, dass wir mit den richtigen Daten arbeiten.

**Beispiel:**

```python
liste = [1, 2, 3, "vier", "fünf"]
#wir saubern die liste in einer Zeile
liste_clean = [x for x in liste if isinstance(x, int)]
print(liste_clean)  # Ausgabe: [1, 2, 3]
```

## 4.4. Python `type()` Funktion

Die `type()` Funktion wird verwendet, um den Datentyp eines Objekts zu ermitteln. Sie gibt den Typ des Objekts zurück.

**Syntax**

```python
type(object)
```

**Beispiel:**

```python
x = 5
print(type(x))  # Ausgabe: <class 'int'>
y = "Hello"
print(type(y))  # Ausgabe: <class 'str'>
z = [1, 2, 3]
print(type(z))  # Ausgabe: <class 'list'>
```

**Praktische Anwendung**

Die `type()` Funktion ist nützlich, um den Datentyp eines Objekts zu überprüfen, insbesondere wenn der Typ zur Laufzeit unbekannt ist. Dies kann helfen, Fehler zu vermeiden und sicherzustellen, dass der Code mit den richtigen Datentypen arbeitet.

**Beispiel:**

```python
def check_type(value):
    if type(value) == int:
        print("Es ist eine ganze Zahl.")
    elif type(value) == str:
        print("Es ist eine Zeichenkette.")
    else:
        print("Es ist ein anderer Typ.")

check_type(10)  # Ausgabe: Es ist eine ganze Zahl.
check_type("Hallo")  # Ausgabe: Es ist eine Zeichenkette.
check_type([1, 2, 3])  # Ausgabe: Es ist ein anderer Typ.
```

# 5. Kontrollstrukturen

Kontrollstrukturen sind essenziell, um den Ablauf eines Programms zu steuern. In Python umfassen sie bedingte Anweisungen, Schleifen und rekursive Aufrufe. Dieses Kapitel behandelt die verschiedenen Kontrollstrukturen in Python, ihre Anwendung und Best Practices.

## 5.1. Bedingungen und Verzweigungen (`if`, `elif`, `else`)

Bedingte Anweisungen ermöglichen es einem Programm, Entscheidungen zu treffen und verschiedene Pfade basierend auf Bedingungen zu verfolgen.

### 5.1.1. Die `if`-Anweisung

Die `if`-Anweisung überprüft eine Bedingung und führt einen Codeblock aus, wenn die Bedingung wahr ist.

**Syntax:**
```python
if Bedingung:
    # Codeblock, der ausgeführt wird, wenn die Bedingung wahr ist
```

**Beispiel:**
```python
alter = 20
if alter >= 18:
    print("Du bist volljährig.")
```

**Ausgabe:**
```
Du bist volljährig.
```

### 5.1.2. Die `elif`-Anweisung

Die `elif`-Anweisung (kurz für "else if") ermöglicht zusätzliche Bedingungen, die geprüft werden, wenn die vorherigen Bedingungen falsch sind.

**Syntax:**
```python
if Bedingung1:
    # Codeblock 1
elif Bedingung2:
    # Codeblock 2
```

**Beispiel:**
```python
note = 85

if note >= 90:
    print("Ausgezeichnet")
elif note >= 80:
    print("Gut")
else:
    print("Verbesserung nötig")
```

**Ausgabe:**
```
Gut
```

### 5.1.3. Die `else`-Anweisung

Die `else`-Anweisung wird ausgeführt, wenn keine der vorherigen Bedingungen wahr ist.

**Syntax:**
```python
if Bedingung:
    # Codeblock 1
else:
    # Codeblock 2
```

**Beispiel:**
```python
temperatur = 25

if temperatur > 30:
    print("Es ist heiß.")
else:
    print("Das Wetter ist angenehm.")
```

**Ausgabe:**
```
Das Wetter ist angenehm.
```

### 5.1.4. Verschachtelte Bedingungen

Bedingungen können innerhalb anderer Bedingungen verschachtelt werden, um komplexere Entscheidungsstrukturen zu erstellen.

**Beispiel:**
```python
alter = 25
student = True

if alter < 30:
    if student:
        print("Ermäßigter Preis für Studenten unter 30.")
    else:
        print("Normaler Preis für Erwachsene unter 30.")
else:
    print("Normaler Preis für Erwachsene 30 oder älter.")
```

**Ausgabe:**
```
Ermäßigter Preis für Studenten unter 30.
```

## 5.2. Iteration

Iteration ermöglicht das wiederholte Ausführen eines Codeblocks. Python unterstützt hauptsächlich `for`- und `while`-Schleifen.

### 5.2.1. `for`-Schleifen

`for`-Schleifen werden verwendet, um über eine Sequenz (wie eine Liste, ein Tuple, ein Dictionary, eine Menge oder eine Zeichenkette) zu iterieren.

**Syntax:**
```python
for Element in Sequenz:
    # Codeblock
```

**Beispiel:**
```python
früchte = ["Apfel", "Banane", "Kirsche"]

for frucht in früchte:
    print(frucht)
```

**Ausgabe:**
```
Apfel
Banane
Kirsche
```

#### Best Practices bei `for`-Schleifen

- **Verwenden von `enumerate()`:** Wenn du sowohl den Index als auch das Element benötigst.
  
  ```python
  for index, frucht in enumerate(früchte):
      print(f"{index}: {frucht}")
  ```

- **Vermeiden unnötiger Schleifen:** Nutze List Comprehensions oder Generatoren, wenn passend, um den Code effizienter und lesbarer zu gestalten.

- **Schleifen frühzeitig beenden:** Verwende `break`, um eine Schleife vorzeitig zu beenden, wenn eine bestimmte Bedingung erfüllt ist.

  ```python
  for frucht in früchte:
      if frucht == "Banane":
          print("Banane gefunden!")
          break
  ```

### 5.2.2. `while`-Schleifen

`while`-Schleifen führen einen Codeblock aus, solange eine Bedingung wahr ist.

**Syntax:**
```python
while Bedingung:
    # Codeblock
```

**Beispiel:**
```python
count = 0

while count < 5:
    print(count)
    count += 1
```

**Ausgabe:**
```
0
1
2
3
4
```

**Hinweis:** Achte darauf, dass die Bedingung irgendwann falsch wird, um eine Endlosschleife zu vermeiden.

### 5.2.3. Verschachtelte Schleifen

Schleifen können innerhalb anderer Schleifen verschachtelt werden, um über mehrdimensionale Datenstrukturen zu iterieren.

**Beispiel:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for reihe in matrix:
    for zahl in reihe:
        print(zahl, end=' ')
    print()  # Neue Zeile nach jeder Reihe
```

**Ausgabe:**
```
1 2 3 
4 5 6 
7 8 9 
```

## 5.3. Rekursion

Rekursion ist eine Methode, bei der eine Funktion sich selbst aufruft, um ein Problem zu lösen. Sie eignet sich besonders für Probleme, die sich in kleinere, ähnliche Teilprobleme zerlegen lassen.

### 5.3.1. Grundlagen der Rekursion

Jede rekursive Funktion muss eine **Basisbedingung** haben, die den rekursiven Aufruf stoppt, um Endlosschleifen zu vermeiden.

**Beispiel: Fakultätsberechnung**

```python
def fakultaet(n):
    if n == 0:
        return 1  # Basisbedingung
    else:
        return n * fakultaet(n - 1)  # Rekursiver Aufruf

print(fakultaet(5))  # Ausgabe: 120
```

### 5.3.2. Vorteile der Rekursion

- **Einfachere Implementierung:** Manche Probleme lassen sich rekursiv leichter und verständlicher lösen.
- **Natürliche Darstellung:** Probleme wie Baumdurchlauf oder die Traversierung von Datenstrukturen sind intuitiv rekursiv.

### 5.3.3. Nachteile der Rekursion

- **Leistungsüberhead:** Jeder Funktionsaufruf benötigt zusätzlichen Speicher für den Aufrufstapel.
- **Begrenzte Tiefe:** Python hat eine maximale Rekursionstiefe (standardmäßig etwa 1000), die überschritten werden kann und zu einem `RecursionError` führt.

### 5.3.4. Rekursion vs. Iteration

Obwohl viele rekursive Lösungen auch iterativ implementiert werden können, ist die Wahl zwischen beiden Ansätzen oft eine Frage der Lesbarkeit und der Effizienz.

**Beispiel: Fibonacci-Folge**

*Rekursive Implementierung:*
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Ausgabe: 8
```

*Iterative Implementierung:*
```python
def fibonacci_iterativ(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci_iterativ(6))  # Ausgabe: 8
```

**Hinweis:** Die iterative Version ist in diesem Fall effizienter, da die rekursive Version exponentielle Laufzeit hat.

### 5.3.5. Tail Recursion Optimierung

Python unterstützt keine Tail Recursion Optimierung, was bedeutet, dass selbst bei tail-rekursiven Funktionen der Aufrufstapel weiter wächst. Daher sollte in Python Iteration bevorzugt werden, wenn möglich.


# 6. Funktionen

In Python gibt es verschiedene Funktionen die uns helfen, den Code zu strukturieren und zu organisieren. Funktionen sind wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe erfüllen. In diesem Kapitel werden die Grundlagen von Funktionen in Python behandelt.

