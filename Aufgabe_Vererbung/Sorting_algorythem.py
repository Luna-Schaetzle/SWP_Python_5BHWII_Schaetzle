import random

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
        n = len(self.data)
        for i in range(n):
            for j in range(n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
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
            print("Shuffling...")
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

# Main function to test all sorting algorithms
def main():
    data = [3, 2, 1, 5, 4]

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

if __name__ == "__main__":
    main()
    # BogoSortTest()