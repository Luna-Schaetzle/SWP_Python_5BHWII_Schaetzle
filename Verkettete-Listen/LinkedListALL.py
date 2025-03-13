


class Node:
    def __init__(self, data=None):
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

    def __iter__(self): # Iterator-Protokoll eine DUNDER-Methode __iter__
        """
        Implementiert das Iterator-Protokoll zum Durchlaufen der Liste.
        Diese Funktion gibt alle die Elemente der Liste zurück.
        """
        current = self.head
        while current:
            yield current.data # yield gibt den Wert zurück und pausiert die Funktion
            current = current.next

    def __len__(self):  # DUNDER-Methode __len__
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
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)

    print("Alle Elemente in der Liste:")
    ll.print_all()

    print("Länge der Liste:", len(ll))

    print("Iterieren über die Liste:")
    for value in ll:
        print(value)

if __name__ == "__main__":
    main()
