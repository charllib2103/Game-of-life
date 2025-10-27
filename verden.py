from rutenett import Rutenett
# Lager klassen verden
class Verden:
    # Konstruktøren tar inn to paramtere og danner seg instansvariabler som definerer kolonner, rader og setter generasjonsnummeret til 0.
    def __init__(self, rader, kolonner):
        self._rader = int(rader)
        self._kolonner = int(kolonner)
        self._generasjonsnummer = 0

        self._rutenett = Rutenett(rader, kolonner) # Lager et rutenett objekt som tar inn rader og kolonner som argumenter
        #Kaller på tidligere metoder med rutenett objektet.
        self._rutenett.fyll_med_tilfeldige_celler() 
        self._rutenett.koble_celler()

    # Lager metoden tegn som kaller på tidligere metoder og tegner rutenettet, itillegg til at generasjonsnummer og antall levende
    #  celler oppdateres for hver gang.
    def tegn(self):
        self._rutenett.tegn_rutenett()
        print("Generasjonsnummer: ", self._generasjonsnummer)
        print("Antall levende celler: ", self._rutenett.antall_levende())

    # Lager metoden oppdatering som oppdaterer rutenettet for hver runde av spillet og øker generasjonsnummer med 1 per runde.
    def oppdatering(self):
        
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                celle = self._rutenett.hent_celle(rad, kolonne)

                if celle is not None:
                    celle.tell_levende_naboer()

        for rad in range(int(self._rader)):
            for kolonne in range(self._kolonner):
                celle = self._rutenett.hent_celle(rad, kolonne)
            
                if celle is not None:
                    celle.oppdater_status() 
            
        self._generasjonsnummer += 1

