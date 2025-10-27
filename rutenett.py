from random import randint
from celle import Celle

# Lager klassen Celle.
class Rutenett:
    # Konstruktøren tar inn to paramtere og danner seg tre instansvariabler som definerer kolonner, rader og lager rutenettet.
    def __init__(self, rader, kolonner):
        self._ant_rader = int(rader)
        self._ant_kolonner = int(kolonner)
        self._rutenett = self._lag_tomt_rutenett()

    # Metoden lager et tomt rutenett og returnerer det.
    def _lag_tomt_rutenett(self):
        rutenett = []
        for i in range(self._ant_rader):
            rutenett.append(self._lag_tom_rad())
        
        return rutenett
    
    # Metoden lager en tom rad og legger den inn i en liste fordi rutenettet består av en nøstet liste. 
    def _lag_tom_rad(self):
        liste = []

        for i in range(self._ant_kolonner):
            liste.append(None)
        
        return liste

    # Metoden fyller rutenettet med tilfeldige celler.
    def fyll_med_tilfeldige_celler(self):

        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                self.lag_celle(i, j) 

    # Metoden lager en celle og setter inn et random tall fra 0-2, og tallet definerer cellen sin status.
    def lag_celle(self, rad, kol):
        celle = Celle() 

        tall = randint(0, 2)

        if tall == 0:
            celle.sett_levende()
        else:
            celle.sett_doed()
        
        self._rutenett[rad][kol] = celle
        
    # Metoden henter cellen og returnerer None hvis if beslutningene stemmer, om de ikke stemmer blir de lagt inn i rutenettet.
    def hent_celle(self, rad, kol):
        if rad < 0 or rad >= self._ant_rader:
            return None
        
        if kol < 0 or kol >= self._ant_kolonner:
            return None

        # Returnerer cellen hvis koordinatene er gyldige
        return self._rutenett[rad][kol]
    
    # Metoden tegner rutenettet ved å itere gjennom den nøstede listen og printer ut status.
    def tegn_rutenett(self):
        for linje in self._rutenett:
            for celle in linje:
                print(celle.hent_status_tegn(), end = "") 
            print()

    # Metoden setter naboer i rutenettet, den tar inn to parametere. Lager if beslutninger for å sikre oss at vi ikke vurderer to like celler.
    def _sett_naboer(self, rad, kol):
        naboer = []
        
        for i in range(rad-1,rad+2):
            for j in range(kol-1,kol+2): 
                nabo = self.hent_celle(i, j)
                if i == rad and j == kol:
                    nabo = None

                if nabo is not None:
                    naboer.append(nabo)
                    
        celle = self.hent_celle(rad, kol)

        for nabo in naboer:
            celle.legg_til_nabo(nabo) 

    # Metoden kobler cellene sammen ved å hente en celle fra kolonnen og raden og sette de som naboer.
    def koble_celler(self):
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                self._sett_naboer(i, j)

    # Metoden henter alle cellene fra self._rutenett og returnerer en liste med de.
    def hent_alle_celler(self):
        liste = []

        for rad in self._rutenett:
            for celle in rad: 
                liste.append(celle)
        
        return liste
    
    # Metoden sjekker antall levende celler i rutenettet ved å itere gjennom den nøstede listen og telle, og til slutt returnere antallet.
    def antall_levende(self):
        antall = 0

        for rad in self._rutenett:
            for celle in rad:
                if celle.er_levende():
                    antall += 1
        return antall
