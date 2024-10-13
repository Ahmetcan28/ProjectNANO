import random

# Word twee keer de gebruiker wat gevraagd, de maximum getal en hoeveel keer ze mogen radden
def start_game():
    maximumgetal = int(input("Voer het maximum getal in: "))
    maximumkeren = int(input("Hoeveel keer mag je raden? "))

    # Laat de computer een random integer bepalen
    random_number = random.randint(1, maximumgetal)

    # Communiceer aan de gebruiker hoe vaak ze mogen raden door middel met f string
    print(f"Je mag {maximumkeren} keer raden om het getal tussen 1 en {maximumgetal} te raden.")

    # Gebruik een for-loop om de gebruiker een x aantal keer te laten raden
    for gok in range(1, maximumkeren + 1):
        guess = int(input(f"Poging {gok}: Raad het getal: "))

        if guess == random_number:
            print(f"Gefeliciteerd! Je hebt het juiste getal {random_number} geraden in {gok} pogingen.")
            break

        # Feedback of het getal groter of kleiner is
        if guess < random_number:
            print("Fout! Het getal is groter.")

        if guess > random_number:
            print("Fout! Het getal is kleiner.")

        # Als het aantal pogingen op is
        if gok == maximumkeren:
            print(f"Helaas, je hebt al je {maximumkeren} pogingen gebruikt. Het juiste getal was {random_number}.")

# Voeg deze sectie toe om te voorkomen dat het direct start bij import
if __name__ == "__main__":
    start_game()  # Dit zorgt ervoor dat dit spel alleen wordt gestart als dit bestand direct wordt uitgevoerd
