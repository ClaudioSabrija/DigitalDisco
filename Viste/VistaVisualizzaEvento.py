from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, \
    QComboBox, QDateTimeEdit, QMessageBox, QHBoxLayout

from Viste import VistaInserisciEvento
from Evento.Evento import Evento
from Gestione.GestoreEventi import GestoreEventi



class VistaVisualizzaEvento(QWidget):
    def __init__(self, evento, elimina_callback, parent=None):
        super(VistaVisualizzaEvento, self).__init__(parent)
        self.controller = GestoreEventi()
        self.elimina_callback = elimina_callback


        info_evento_layout = QHBoxLayout()
        scelte_evento_layout = QVBoxLayout()
        dati_evento_layout = QVBoxLayout()

        #font = QFont('Arial Nova Light', 14)


        nome = self.controller.get_nome()
        tipo = self.controller.get_tipo()
        data = self.controller.get_data()
        prezzo_ingresso = self.controller.get_prezzo_ingresso()
        prezzo_tavolo = self.controller.get_prezzo_tavolo()
        prezzo_prive = self.controller.get_prezzo_prive()

        # Creazione dei widget
        label_nome = QLabel(f"NOME: {nome}", self)
        label_tipo = QLabel(f"TIPO: {tipo}", self)
        label_data = QLabel(f"DATA: {data}", self)
        label_ingresso = QLabel(f"INGRESSO: {prezzo_ingresso}", self)
        label_tavolo = QLabel(f"TAVOLO: {prezzo_tavolo}", self)
        label_prive = QLabel(f"PRIVE: {prezzo_prive}", self)

        # Aggiunta delle label al layout delle informazioni

        info_evento_layout.addWidget(label_nome)
        info_evento_layout.addWidget(label_tipo)
        info_evento_layout.addWidget(label_data)

        dati_evento_layout.addWidget(label_ingresso)
        dati_evento_layout.addWidget(label_tavolo)
        dati_evento_layout.addWidget(label_prive)

        # Creazione del layout principale
        layout_principale = QHBoxLayout()
        layout_principale.addLayout(info_evento_layout)
        layout_principale.addLayout(dati_evento_layout)
        layout_principale.addLayout(scelte_evento_layout)

        # Impostazione del layout principale per il widget
        self.setLayout(layout_principale)


        button_modifica_evento = QPushButton("MODIFICA EVENTO", self)
        button_modifica_evento.clicked.connect(self.go_modifica_evento)
        scelte_evento_layout.addWidget(button_modifica_evento)

        button_elimina_evento = QPushButton('ELIMINA EVENTO')
        button_elimina_evento.clicked.connect(lambda: self.elimina_evento_click(evento))
        scelte_evento_layout.addWidget(button_elimina_evento)

        button_prenotazioni = QPushButton('PRENOTAZIONI')
        button_prenotazioni.clicked.connect(self.go_prenotazioni)
        scelte_evento_layout.addWidget(button_prenotazioni)

        button_ordini = QPushButton('ORDINI')
        button_ordini.clicked.connect(self.go_ordini)
        scelte_evento_layout.addWidget(button_ordini)


        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Visualizza Evento')
            # self.setFixedSize(800, 300)  # Imposta la dimensione fissa della finestra di dialogo


    def elimina_evento_click(self, evento):
        if isinstance(evento, Evento):
            evento.rimuovi_evento()
        self.elimina_callback()
        self.close()

    def go_modifica_evento(self):
        pass

    def go_prenotazioni(self):
        pass

    def go_ordini(self):
        pass