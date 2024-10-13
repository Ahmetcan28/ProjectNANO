import random

# Hier maak ik een lijst van 9 elementen, die dan het bord is voor het spel. Elk element is een spatie met ""
bord = [' ' for _ in range(9)]

# Functie om het bord op het scherm te tonen
def toon_bord():
    # Splits het bord in 3 rijen bijvoorbeekd [0:3], [3,6], [6:9]
    for rij in [bord[i*3:(i+1)*3] for i in range(3)]:
        # De rij wordt geprint met |
        print('| ' + ' | '.join(rij) + ' |')

# Functie om te controleren of een speler heeft gewonnen
def controleer_winnaar(speler):
    # Wincondities zijn de mogelijke winnende combinaties op het bord
    win_condities = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Drie rijen
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Drie kolommen
        [0, 4, 8], [2, 4, 6]  # Twee diagonalen
    ]
    # Voor elke winnende conditie controleren we of alle drie de posities op het bord bezet zijn door de speler (X of O)
    for conditie in win_condities:
        # Als alle plekken in een winconditie door dezelfde speler bezet zijn, dan is die speler de winnaar
        if all(bord[i] == speler for i in conditie):
            return True
    # Als geen enkele winnende conditie is bereikt, is er nog geen winnaar
    return False

# Functie voor de speler om een zet te doen
def speler_zet():
    # De speler kiest een plek (tussen 1 en 9) en deze wordt omgezet naar een index (0-8)
    zet = int(input("Kies een positie (1-9): ")) - 1
    # Als de gekozen positie nog leeg is (' '), wordt de zet op het bord geplaatst als 'X'
    if bord[zet] == ' ':
        bord[zet] = 'X'
    else:
        # Als de positie al bezet is, krijgt de speler een melding en moet hij opnieuw kiezen
        print("Deze plek is al bezet!")
        speler_zet()  # De speler mag opnieuw een zet kiezen

# Functie voor de computer om willekeurig een zet te doen
def computer_zet():
    # Bepaal de beschikbare zetten door met enumerate() te iteren door het bord waarbiij de i de index is en x het element op jhet bord
    beschikbare_zetten = [i for i, x in enumerate(bord) if x == ' ']
    # Kies willekeurig een van de beschikbare zetten en plaats 'O' op die positie
    zet = random.choice(beschikbare_zetten)
    bord[zet] = 'O'

# Functie om te controleren of het bord vol is
def is_bord_vol():
    # Als er geen lege plekken meer zijn, retourneer True, anders False
    return ' ' not in bord

# Hoofdspel
def speel_spel():
    toon_bord()  # Toon het lege bord aan het begin van het spel
    # De game loopt oneindig totdat er een winnaar is of het bord vol is
    while True:
        # De speler doet eerst een zet
        speler_zet()
        # Controleer of de speler heeft gewonnen
        if controleer_winnaar('X'):
            toon_bord()  # Toon het bord nog een keer om de winnende zet te laten zien
            print("Gefeliciteerd! Je hebt gewonnen!")  # Meld de speler dat ze hebben gewonnen
            break  # Het spel stopt
        # Als het bord vol is, is het een gelijkspel
        if is_bord_vol():
            toon_bord()
            print("Het is een gelijkspel!")  # Meld een gelijkspel
            break

        # Nu is de computer aan de beurt
        computer_zet()
        # Controleer of de computer heeft gewonnen
        if controleer_winnaar('O'):
            toon_bord()  # Toon het bord met de winnende zet van de computer
            print("De computer heeft gewonnen!")  # Meld dat de computer heeft gewonnen
            break
        # Als het bord vol is na de zet van de computer, is het een gelijkspel
        if is_bord_vol():
            toon_bord()
            print("Het is een gelijkspel!")  # Meld een gelijkspel
            break

        toon_bord()  # Toon het bijgewerkte bord na elke zet van zowel de speler als de computer

# Voeg deze sectie toe om te voorkomen dat het direct start bij import
if __name__ == "__main__":
    speel_spel()  # Dit zorgt ervoor dat het spel alleen wordt gestart als dit bestand direct wordt uitgevoerd