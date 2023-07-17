from GestoreOrdini.Controller.GestoreOrdini import GestoreOrdini
from GestoreEventi.Controller.GestoreEventi import GestoreEventi
from datetime import datetime

class GestoreStatistiche():
    def __init__(self):
        self.controller_eventi = GestoreEventi()

    def calcola_incassi_mensili_biglietti(self, mese_scelto):
        totale_incassi = 0
        for evento in self.controller_eventi.lista_eventi:
            giorno, mese, anno = map(int, evento.data.split('/'))
            data_evento = datetime(anno, mese, giorno)
            if data_evento.month == mese_scelto:
                for prenotazione in evento.lista_prenotazioni:
                    totale_incassi += prenotazione.servizio.prezzo

        return totale_incassi

    def calcola_incassi_annuali_biglietti(self):
        pass

    def calcola_incassi_mensili_ordini(self):
        pass

    def calcola_incassi_annuali_ordini(self):
        pass
