class Servizio:
    def __init__(self, nome, prezzo, disponibilita):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibilita = disponibilita
        self.numero_prenotazioni = 0

    def aumenta_prenotazioni(self):
        self.numero_prenotazioni += 1

    def get_nome_servizio(self):
        return self.nome

    def get_prezzo_servizio(self):
        return self.prezzo

    def get_disponibilita_servizio(self):
        return self.disponibilita

    def get_numero_prenotazioni(self):
        return self.numero_prenotazioni





# inserisci_prenotazione, ad ogni prenotazione bisogna aumentare una variabile della classe Evento chiamata
# numero_prenotazioni relative a quel servizio ed il numero totale di prenotazioni dell'evento, e diminuire
# il numero di posti disponibili