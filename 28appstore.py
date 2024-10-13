import python_dagboek
import python_game
import python_xl
def menu():
    print("\nWelkom bij 28 app store!")
    print("Kies een app om te starten:")
    print("1. Dagboek")
    print("2. Raad het nummer")
    print("3. Python XL")
    print("4. Afsluiten")

    keuze = input("Voer je keuze in (1-4): ")

    if keuze == "1":
        # Direct gebruik maken van functies in python_dagboek.py
        dagboek = python_dagboek.load_dagboek()  # Laad het dagboek
        datum = python_dagboek.vraag_datum()  # Vraag de gebruiker om een datum
        python_dagboek.schrijf_dagboek(dagboek, datum)  # Voeg of bewerk de tekst voor de datum
        python_dagboek.save_dagboek(dagboek)  # Sla het dagboek op
        print(f"Dagboek voor {datum} is opgeslagen.")  # Bevestig aan de gebruiker dat de tekst is opgeslagen
    elif keuze == "2":
        # Start het raadnummer spel vanuit python_game
        python_game.start_game()  # Roep de start_game functie uit python_game aan om het spel te starten
    elif keuze == "3":
        # Start je Python XL spel (voorheen boter-kaas-en-eieren)
        python_xl.speel_spel()  # Roep de speel_spel functie aan vanuit python_xl
    elif keuze == "4":
        print("Afsluiten...")
        return
    else:
        print("Ongeldige keuze. Probeer opnieuw.")  # Als de keuze niet geldig is, probeer opnieuw

# Start het programma
if __name__ == "__main__":
    menu()  # Roept het menu aan om het programma te starten