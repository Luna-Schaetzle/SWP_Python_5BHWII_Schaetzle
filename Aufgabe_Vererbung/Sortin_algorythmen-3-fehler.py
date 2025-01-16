import random
import ollama
import time
import threading
import json
import sys


# Base class for sorting algorithms
class SortingAlgorithm:
    """Basisklasse für Sortieralgorithmen."""
    
    def __init__(self, data):
        # Initialize with data to be sorted
        self.data = data

    def sort(self):
        """Sortiermethode, die in Unterklassen implementiert wird."""
        # Method to be implemented in subclasses
        raise NotImplementedError("Die Sortiermethode muss in der Unterklasse implementiert werden!")

    def print_data(self):
        """Gibt die sortierten Daten aus."""
        # Print the sorted data
        print(self.data)

    def is_sorted(self):
        """Überprüft, ob die Daten sortiert sind."""
        # Check if the data is sorted
        return all(self.data[i] <= self.data[i + 1] for i in range(len(self.data) - 1))

    def sort_and_check(self):
        """Sortiert die Daten und überprüft, ob sie korrekt sortiert sind."""
        # Sort the data and check if it is sorted
        sorted_data = self.sort()
        if not self.is_sorted():
            print("Sorting failed")
        else:
            print("Sorting successful")
        return sorted_data

# Implementation of Stalin Sort
class StalinSort(SortingAlgorithm):
    """Implementierung von Stalin Sort."""
    
    def __init__(self, data):
        super().__init__(data)

    def sort(self): # Stalin Sort takes the first element and then checks if the next element is greater than the previous one. If it is, it is added to the sorted list. If not, it is removed. 
        if not self.data:
            return []
        sorted_data = [self.data[0]]
        for element in self.data[1:]:
            if element >= sorted_data[-1]:
                sorted_data.append(element)
            else:
                print(f"Stalin decided that {element} is not needed!")
        self.data = sorted_data
        return self.data

# Implementation of Bubble Sort
class BubbleSort(SortingAlgorithm):
    """Implementierung von Bubble Sort."""
    
    def sort(self):
        try:
            n = len(self.data)
            for i in range(n):
                for j in range(n - i - 1):
                    if self.data[j] > self.data[j + 1]:
                        self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
            return self.data
        except Exception as e:
            print(f"An error occurred during Bubble Sort: {e}")
            return self.data


# Implementation of Quick Sort
class QuickSort(SortingAlgorithm):
    """Implementierung von Quick Sort."""
    
    def sort(self):
        self.data = self.quick_sort(self.data)
        return self.data

    def quick_sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

# Implementation of Bogo Sort
class BogoSort(SortingAlgorithm):
    """Implementierung von Bogo Sort."""
    iterations = 0

    def sort(self):
        while not self.is_sorted():
            random.shuffle(self.data)
            #print("Shuffling...")
            self.iterations += 1
        print(f"Sorting took {self.iterations} iterations")
        return self.data

# Test function for BogoSort
def BogoSortTest():
    data = [3, 2, 1, 5, 4]
    # The mission is to find how many times you need to execute the BogoSort to get the sorted list by the first time
    times = 0
    while True:
        bogo_sort = BogoSort(data.copy())
        bogo_sort.sort_and_check()
        times += 1
        if bogo_sort.iterations == 1:
            break
    print(f"Sorting took {times} times to get the sorted list by the first time")

# Mirecal sort
# The mission is to implement a sorting algorithm that only relies on the power of beliving that the list is sorted or somhow gets sorted by itself by the power of the universe
class MirecalSort(SortingAlgorithm):
    """Implementierung von Mirecal Sort."""
    
    def __init__(self, data):
        super().__init__(data)

    def sort(self):
        sorted_data = self.data
        return sorted_data

import json  # Zum Parsen der API-Antwort

class AISort(SortingAlgorithm):
    """Implementierung von AI Sort mit externer AI."""

    def __init__(self, data):
        super().__init__(data)

    def sort(self):
        try:
            # Anfrage an die AI-API
            response = ollama.chat(model='qwen2.5-coder:0.5b', messages=[
                {'role': 'user', 'content': (
                    'Only Reply With the Sorted List NOT WITH MORE INFORMATION ONLY THE SORTED LIST '
                    '(Gib die Liste in Folgendem Format [1, 2, 3]) Sort the list: ' + str(self.data)
                )}
            ])
            
            # Antwort der AI lesen
            sorted_data = response['message']['content']
            print(f"AI Sort Response (Raw): {sorted_data}")

            # Entfernen von unerwünschten Zeichen oder Text (falls AI mehr Informationen liefert)
            sorted_data_cleaned = ''.join(filter(lambda x: x in '0123456789[], ', sorted_data))
            print(f"AI Sort Response (Cleaned): {sorted_data_cleaned}")
            
            # Versuch, die bereinigte Antwort in eine Liste umzuwandeln
            sorted_data = json.loads(sorted_data_cleaned)
            
            # Validierung der sortierten Liste
            if isinstance(sorted_data, list) and sorted(sorted_data) == sorted_data:
                return sorted_data
            else:
                raise ValueError("AI returned an invalid or incorrectly sorted list.")
        
        except json.JSONDecodeError:
            print("AI Sort Error: Could not parse AI response as a list.")
            return self.data  # Rückgabe der unsortierten Liste im Fehlerfall
        except Exception as e:
            print(f"AI Sort Error: {e}")
            return self.data  # Rückgabe der unsortierten Liste im Fehlerfall


# Sleep sort
# The mission is to implement a sorting algorithm that uses the power of sleep to sort the list 
# It sleeps for the time of the element and then adds it to the sorted list
class SleepSort:
    """Implementierung von Sleep Sort mit Threads."""

    def __init__(self, data):
        self.data = data
        self.sorted_data = []  # Synchronisierte Liste für das Ergebnis
        self.lock = threading.Lock()  # Lock für den Thread-Safe-Zugriff

    def _sleep_and_append(self, value):
        """Hilfsfunktion: Schlafen und Wert zur Liste hinzufügen."""
        # Skalierung der Schlafzeit, um zu lange Wartezeiten zu vermeiden
        # Hier multiplizieren wir mit 0.01, um die Schlafzeit in Sekunden zu halten
        scaled_sleep_time = value * 0.01  
        time.sleep(scaled_sleep_time)  # Zeit basiert auf dem Wert
        with self.lock:  # Zugriff auf die Liste sichern
            self.sorted_data.append(value)

    def sort(self):
        threads = []
        for element in self.data:
            if element < 0:
                raise ValueError("Sleep Sort funktioniert nur mit positiven Zahlen.")
            thread = threading.Thread(target=self._sleep_and_append, args=(element,))
            threads.append(thread)
            thread.start()

        # Warten auf alle Threads
        for thread in threads:
            thread.join()

        # Liste sollte jetzt sortiert sein
        return self.sorted_data
    

# Main function to test all sorting algorithms
def main():
    data = [3, 2, 1, 5, 4, 10, 30]

    print("\nStalin Sort")
    stalin_sort = StalinSort(data.copy())
    stalin_sort.sort_and_check()
    stalin_sort.print_data()

    print("\nBubble Sort")
    bubble_sort = BubbleSort(data.copy())
    bubble_sort.sort_and_check()
    bubble_sort.print_data()

    print("\nQuick Sort")
    quick_sort = QuickSort(data.copy())
    quick_sort.sort_and_check()
    quick_sort.print_data()

    print("\nBogo Sort")
    bogo_sort = BogoSort(data.copy())
    bogo_sort.sort_and_check()
    bogo_sort.print_data()

    print("\nMirecal Sort")
    mirecal_sort = MirecalSort(data.copy())
    mirecal_sort.sort_and_check()
    mirecal_sort.print_data()

    print("\nAI Sort")
    ai_sort = AISort(data.copy())
    sorted_data = ai_sort.sort()
    print(f"Final Sorted Data: {sorted_data}")
    print(f"AI might have sorted the list by the power of the universe, it also might have dreamed of electric sheeps")


    print("\nSleepSort")
    sorter = SleepSort(data.copy())
    sorted_list = sorter.sort()
    print("Sortiert:", sorted_list)

def main_with_error_handling():
    data = [3, 2, 1, 5, 4, 10, 30, -1]

    print("\nDemonstration der Fehlerarten")

    # a) Neuer Fehler und behebbar (LBYL)
    print("\nA: Neuer Fehler und behebbar")
    try:
        print("Daten vor Fehlerbehebung:", data)
        if any(x < 0 for x in data):
            print("Negative Werte gefunden! Negative Werte werden auf 0 gesetzt.")
            data = [max(0, x) for x in data]  # Negative Werte durch 0 ersetzen
        print("Daten nach Fehlerbehebung:", data)
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")

    # b) Hochgeblubberter Fehler und behebbar (EAFP)
    print("\nB: Hochgeblubberter Fehler und behebbar")
    try:
        print("Daten sortieren mit BubbleSort:")
        bubble_sort = BubbleSort(data.copy())
        sorted_data = bubble_sort.sort()
        print("Erfolgreich sortiert:", sorted_data)
    except ValueError as e:
        print(f"Behandelter Fehler: {e}")
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")

    data = [3, 2, 1, 5, 4, 10, 30, -1]
    # c) Neuer Fehler und NICHT behebbar
    print("\nC: Neuer Fehler und NICHT behebbar")
    try:
        print("Daten sortieren mit SleepSort:")
        sleep_sort = SleepSort(data.copy())
        sorted_data = sleep_sort.sort()  # Erwarteter Fehler wegen negativen Werten
        print("Erfolgreich sortiert:", sorted_data)
    except ValueError as e:
        print(f"Nicht behebbarer Fehler erkannt: {e}")

    # d) Hochgeblubberter Fehler und NICHT behebbar
    print("\nD: Hochgeblubberter Fehler und NICHT behebbar")
    try:
        print("Sortieren mit AI Sort:")
        ai_sort = AISort(data.copy())
        sorted_data = ai_sort.sort()
        print("Ergebnis der Sortierung durch AI:", sorted_data)
    except Exception as e:
        print(f"Unerwarteter Fehler beim Hochblubbern: {e}")
        print("Dieser Fehler ist nicht behebbar und wird an die Aufruferfunktion weitergegeben.")

if __name__ == "__main__":
    try:
        main_with_error_handling()
    except Exception as e:
        print(f"Die Anwendung ist unerwartet mit einem Fehler beendet: {e}")
        sys.exit(1)
