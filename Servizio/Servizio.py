class Servizio:
    def __init__(self, 'Servizio', prezzo, disponibilita):
        self.nome_servizio = 'Servizio'
        self.prezzo = prezzo
        self.disponibilita = disponibilita
        self.numero_prenotazioni = 0

    def aumenta_prenotazioni(self):
        self.numero_prenotazioni += 1

    def get__nome_servizio(self):
        return Servizio.nome

    def get_prezzo_servizio(self):
        return Servizio.prezzo

    def get_disponibilita_servizio(self):
        return Servizio.disponibilita

    def get_numero_prenotazioni(self):
        return Servizio.numero_prenotazioni




# inserisci_prenotazione, ad ogni prenotazione bisogna aumentare una variabile della classe Evento chiamata
# numero_prenotazioni relative a quel servizio ed il numero totale di prenotazioni dell'evento, e diminuire
# il numero di posti disponibili