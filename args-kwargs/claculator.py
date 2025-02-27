import argparse
import math

# Haupt-Taschenrechner Funktion mit inneren Funktionen und kwargs
def calculator(operation, *args, **kwargs):
    # Innere Funktion für Addition
    def add(*numbers, **kwargs):
        return sum(numbers)

    # Innere Funktion für Multiplikation
    def multiply(*numbers, **kwargs):
        result = 1
        for number in numbers:
            result *= number
        return result

    # Innere Funktion für Durchschnitt
    def average(*numbers, **kwargs):
        return sum(numbers) / len(numbers)

    # Innere Funktion für Potenzierung
    def power(*numbers, **kwargs):
        base = numbers[0]
        exponent = numbers[1] if len(numbers) > 1 else 2  # Standard: Exponent = 2
        return base ** exponent

    # Innere Funktion für Rundung
    def round_result(result, **kwargs):
        decimal_places = kwargs.get('round', 2)  # Standard auf 2 Dezimalstellen
        return round(result, decimal_places)

    # Dictionary, das alle Operationen verwaltet
    operations = {
        'add': add,
        'multiply': multiply,
        'average': average,
        'power': power
    }

    # Sicherstellen, dass die Operation existiert
    if operation not in operations:
        return f"Unbekannte Operation: {operation}"

    # Operation ausführen
    result = operations[operation](*args, **kwargs)

    # Falls Rundung gewünscht wird, anwenden
    if 'round' in kwargs:
        result = round_result(result, **kwargs)

    return result

# Hilfe-Funktion
def print_help():
    help_text = """
    Taschenrechner Hilfe:
    
    - Operationen:
      - add        : Addition
      - multiply   : Multiplikation
      - average    : Durchschnitt
      - power      : Potenzierung

    - Optionen:
      - --round    : Rundung auf eine bestimmte Anzahl von Dezimalstellen

    Beispielaufrufe:
      python calculator.py add 1 2 3 4 --round 2   -> Ergebnis: 10.0
      python calculator.py multiply 2 3 4           -> Ergebnis: 24
      python calculator.py average 5 10 15          -> Ergebnis: 10.0
      python calculator.py power 3 2                -> Ergebnis: 9
    """
    print(help_text)

# CLI-Funktion mit Endlosschleife
def main():
    print("Willkommen beim dynamischen Taschenrechner!")
    print("Geben Sie 'help' ein, um eine Hilfe-Anleitung zu erhalten.")
    
    while True:
        user_input = input("Berechnung (z.B. add 1 2 3): ").strip()
        
        # Hilfe anzeigen
        if user_input.lower() == "help":
            print_help()
            continue

        # Benutzereingaben verarbeiten
        try:
            parts = user_input.split()
            operation = parts[0]
            numbers = list(map(float, parts[1:]))
            round_value = None

            # Überprüfen, ob eine Rundung angegeben wurde
            if '--round' in parts:
                round_index = parts.index('--round')
                round_value = int(parts[round_index + 1])

            # Berechnung durchführen
            result = calculator(operation, *numbers, round=round_value)
            print(f"Ergebnis: {result}")

        except Exception as e:
            print(f"Fehler: {e}. Geben Sie 'help' ein, um Hilfe zu erhalten.")

# Programm ausführen
if __name__ == '__main__':
    main()
