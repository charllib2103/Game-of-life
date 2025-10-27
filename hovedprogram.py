from verden import Verden
from rutenett import Rutenett

# Lager et hovedprogram for å teste alle klassene sammen.
def hovedprogram():
    rader = input("Hvor mange rader vil du ha? ")
    kolonner = input("Hvor mange kolonner vil du ha? ")
    verden = Verden(rader, kolonner) #Opretter et verden-objekt og putter svarene fra bruker inn som argumenter.

    verden.tegn() # Tegner rutenettet.

# Lager en while løkke for om bruker ønsker å fortsette spillet.
    svar = input("Skriv 'enter' for å gå videre, eller q for å avslutte: ").lower()
# Oppdaterer rutenettet for hver gang bruker vil fortsette.
    while svar!= "q":
        verden.oppdatering()
        verden.tegn()
        svar = input("Skriv 'enter' for å gå videre, eller q for å avslutte: ").lower()

# starte hovedprogrammet
hovedprogram()


