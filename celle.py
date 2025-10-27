# Lager klassen Celle.
class Celle:
    # Konstruktøren inneholder 3 instansvariabler; status på cellen, en liste og antall levende
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0
   # Metode som setter cellen til død og returnerer status. 
    def sett_doed(self):
        self._status = "doed"
        return self._status
    # Metode som setter cellen til levende og returnerer status. 
    def sett_levende(self):
        self._status = "levende"
        return self._status
    # Metode som sjekker om cellen er levende og returnerer en boolsk verdi.
    def er_levende(self):
        if self._status == "levende":   
            return True
        return False
    # Metode som returnerer tegn til rutenettet basert på hvor mange som er levende og døde.
    def hent_status_tegn(self):
        if self._status == "levende":
            return "O"
        return "."
    # Metoden legger inn argumentet fra parametere nabo inn i listen over naboer.
    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    # Teller antall levende naboer og sjekker om den er levende ved bruk av metoden er_levende fra tidligere i programmet.
    def tell_levende_naboer(self):
        self._ant_levende_naboer = 0

        for nabo in self._naboer:
            if nabo.er_levende():
                self._ant_levende_naboer +=1

    # Metode som oppdaterer status.
    def oppdater_status(self):

    # Teller levende naboer først
        self.tell_levende_naboer()
        
    # Bruker antall levende naboer for å bestemme ny status
        if self.er_levende():
            if self._ant_levende_naboer < 2 or self._ant_levende_naboer > 3:
                self.sett_doed()  # Dør på grunn av under- eller overbefolkning
        else:
            if self._ant_levende_naboer == 3:
                self.sett_levende()  # Blir levende på grunn av reproduksjon


