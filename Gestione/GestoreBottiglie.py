class GestoreBottiglie():

    def __init__(self, bottiglie):
        self.model = bottiglie

    def get_bottiglia(self):
        return self.model

    def set_bottiglia(self, bottiglia):
        self.model = bottiglia

    def get_nome_bottiglia(self):
        return self.model.nome

    def get_prezzo_bottiglia(self):
        return self.model.prezzo

    def get_disponibilta_bottiglia(self):
        return self.model.disponibilita

    def get_corridoio_bottiglia(self):
        return self.model.corridoio

    def get_scaffale_bottiglia(self):
            return self.model.scaffale

    def get_piano_bottiglia(self):
        return self.model.piano

