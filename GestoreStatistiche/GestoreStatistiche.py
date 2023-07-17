from GestoreOrdini.Controller.GestoreOrdini import GestoreOrdini
from GestoreEventi.Controller.GestoreEventi import GestoreEventi
from datetime import datetime

class GestoreStatistiche():
    def __init__(self):
        self.controller_eventi = GestoreEventi()

    def calcola_incassi_mensili_biglietti(self, mese_scelto):
        totale_incassi_biglietti = 0
        totale_incassi_tavoli = 0
        totale_incassi_prive = 0

        for evento in self.controller_eventi.lista_eventi:
            giorno, mese, anno = map(int, evento.data.split('/'))
            data_evento = datetime(anno, mese, giorno)
            if data_evento.month == mese_scelto:
                prezzo_ingresso = evento.get_prezzo_ingresso()
                prezzo_tavolo = evento.get_prezzo_tavolo()
                prezzo_prive = evento.get_prezzo_prive()

                for prenotazione in evento.lista_prenotazioni:
                    servizio_scelto = prenotazione.servizio.get_nome_servizio()

                    if servizio_scelto == "Ingresso":
                        totale_incassi_biglietti += prezzo_ingresso
                    elif servizio_scelto == "Tavolo":
                        totale_incassi_tavoli += prezzo_tavolo
                    elif servizio_scelto == "Prive":
                        totale_incassi_prive += prezzo_prive

        totale_incassi = totale_incassi_biglietti + totale_incassi_tavoli + totale_incassi_prive
        return totale_incassi

    def calcola_incassi_annuali_biglietti(self):
        pass

    def calcola_incassi_mensili_ordini(self):
        pass

    def calcola_incassi_annuali_ordini(self):
        pass
