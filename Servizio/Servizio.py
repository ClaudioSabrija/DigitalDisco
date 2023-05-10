class Servizio:
    def __init__(self, 'Servizio', prezzo, disponibilita):
        self.nome_servizio = 'Servizio'
        self.prezzo = prezzo
        self.disponibilita = disponibilita

    def get__nome_servizio(self):
        return Servizio.nome

    def get_prezzo_servizio(self):
        return Servizio.prezzo

    def get_disponibilita_servizio(self):
        return Servizio.disponibilita

class Ingresso(Servizio):
    def __init__(self):
        super(Ingresso, self).__init__('Ingresso', prezzo, disponibilita)


class Tavolo(Servizio):
    def __init__(self):
        super(Ingresso, self).__init__('Tavolo', prezzo, disponibilita)


class Prive(Servizio):
    def __init__(self):
        super(Ingresso, self).__init__('Prive', prezzo, disponibilita)


# inserisci_prenotazione, ad ogni prenotazione bisogna aumentare una variabile della classe Evento chiamata
# numero_prenotazioni relative a quel servizio ed il numero totale di prenotazioni dell'evento, e diminuire
# il numero di posti disponibili