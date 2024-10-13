import json # Importeer de JSON om met JSON-bestanden te werken
from datetime import datetime # Importeer de datetime om de huidige datum te krijgen

# Functie word er aangemaakt om het dagboek uit het JSON-bestand te laden
def load_dagboek():
    try:
        with open('dagboek.json', 'r') as file: # Openen van het dagboekbestand en de inhoud te laten
            return json.load(file)
    except FileNotFoundError:
        return {}  # Als het bestand niet bestaat, retourneer een lege dictionary

# Functie om het dagboek op te slaan in het JSON bestand
def save_dagboek(dagboek):
    with open('dagboek.json', 'w') as file:  # Open het JSON bestand in schrijf modus en sla het dagboek op
        json.dump(dagboek, file, indent=4) # schrijf de dictionary naar het bestand met een spaties zodat het mooi is

# Functie om de gebruiker te vragen welke datum gebruikt moet worden
def vraag_datum():
    keuze = input("Wil je voor vandaag schrijven (ja/nee)? ").lower() # Vraagt de gebruikter of het voor vandaag is
    if keuze == 'ja': # Als de gebruiker 'ja' kiest, word de huidige datum gebruikt.
        return datetime.now().strftime('%Y-%m-%d')
    else:
        return input("Voer een andere datum in (YYYY-MM-DD): ") # vraagt de gebruiker om andere datum in te voeren

# Voeg of overschrijf een entry in het dagboek
def schrijf_dagboek(dagboek, datum):
    if datum in dagboek: # controleer of er al een entry bestaat voor de gegeven datum
        keuze = input(f"Er bestaat al een entry voor {datum}. Wil je deze overschrijven (ja/nee)? ").lower() # Vraag gebruiker om over te schrijven
        if keuze == 'nee':
            toevoeging = input("Voeg je nieuwe tekst toe: ") # Als de keuze nee is door de gebruiker, voeg een nieuwe tekst toe aan bestaande tekst
            dagboek[datum] += f"\n{toevoeging}"  # Voeg nieuwe tekst aan bestaande tekst
        else:
            nieuwe_tekst = input("Schrijf de nieuwe tekst: ") # Als de gebruiker wil overshcrijven, vervan de oude tekst
            dagboek[datum] = nieuwe_tekst
    else:
        nieuwe_tekst = input("Schrijf je dagboektekst: ") # Als er geen tekst was voor die datum, vraagt gebruiker om nieuwe tekst.
        dagboek[datum] = nieuwe_tekst # voeg de nieuwe tekst toe aan het dagboek

# Hoofdfunctie die alle logica van dit spel beheert
def main():
    dagboek = load_dagboek() # laad het dagboek
    datum = vraag_datum() # vraagt de gebruiker om een datum
    schrijf_dagboek(dagboek, datum) # Voeg of bewerkt de tekst voor de datum
    save_dagboek(dagboek) # Sla het dagboek op
    print(f"Dagboek voor {datum} is opgeslagen.") # Geeft een bevestiging aan de gebruiker dat de getypyte tekst is opgeslagen

# Voeg deze sectie toe om te voorkomen dat het direct start bij import
if __name__ == "__main__":
    main()  # Roep de juiste functie aan om het dagboek te starten
