import random

class Node:
    def __init__(self, data: int):
        if not isinstance(data, int):
            raise TypeError("Nur Ganzahl-Werte sind erlaubt!")
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        """
        Hängt einen neuen Knoten mit dem gegebenen Ganzahlwert am Ende der Liste an.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def __iter__(self):
        """
        Implementiert das Iterator-Protokoll zum Durchlaufen der Liste.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        """
        Gibt die Länge (Anzahl der Elemente) der Liste zurück.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_all(self):
        """
        Gibt alle Elemente der Liste aus.
        """
        for data in self:
            print(data, end=" ")
        print()

def main():
    # Liste instanziieren
    linked_list = LinkedList()

    # Beispielliste mit zufälligen Ganzzahlen füllen (z.B. 10 Zahlen zwischen 0 und 100)
    for _ in range(10):
        num = random.randint(0, 100)
        linked_list.append(num)

    # Ausgabe der Länge der Liste
    print("Länge der Liste:", len(linked_list))

    # Ausgabe aller Elemente der Liste
    print("Elemente der Liste:")
    linked_list.print_all()

if __name__ == '__main__':
    main()