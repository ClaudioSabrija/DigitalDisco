from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from Gestione.GestoreEventi import GestoreEventi
from Viste.VistaModificaEvento import VistaModificaEvento
from Viste.VistaOrdini import VistaOrdini


class VistaVisualizzaEvento(QWidget):
    def __init__(self, evento, elimina_evento_callback=None, parent=None):
        super(VistaVisualizzaEvento, self).__init__(parent)

        self.evento1 = evento
        self.elimina_evento_callback = elimina_evento_callback
        self.controller = GestoreEventi()

        info_evento_layout = QHBoxLayout()
        scelte_evento_layout = QVBoxLayout()
        dati_evento_layout = QVBoxLayout()

        # Creazione dei widget

        self.label_nome = QLabel(f"{self.evento1.get_nome()}")
        self.label_data = QLabel(f"DATA: {self.evento1.get_data()}")
        self.label_tipo = QLabel(f"TIPO: {self.evento1.get_tipo()}")
        self.label_ingresso = QLabel(f"INGRESSO: {self.evento1.get_prezzo_ingresso()}")
        self.label_tavolo = QLabel(f"TAVOLO: {self.evento1.get_prezzo_tavolo()}")
        self.label_prive = QLabel(f"PRIVE: {self.evento1.get_prezzo_prive()}")

        # Impostazione del Font
        font = QFont('Arial Nova Light')
        font_nome = QFont('Arial Nova Light')
        font_nome.setBold(True)
        font_nome.setUnderline(True)
        font.setPointSize(15)
        font_nome.setPointSize(20)

        self.label_nome.setFont(font_nome)
        self.label_nome.setAlignment(Qt.AlignCenter)

        # Aggiungo tutte le tue label a questa lista
        labels = [self.label_data, self.label_tipo, self.label_ingresso, self.label_tavolo, self.label_prive]

        for label in labels:
            label.setFont(font)
            label.setAlignment(Qt.AlignLeft)

        # Aggiunta delle label al layout delle informazioni
        info_evento_layout.addWidget(self.label_nome)

        dati_evento_layout.addWidget(self.label_data)
        dati_evento_layout.addWidget(self.label_tipo)
        dati_evento_layout.addWidget(self.label_ingresso)
        dati_evento_layout.addWidget(self.label_tavolo)
        dati_evento_layout.addWidget(self.label_prive)

        # Creazione del layout principale
        layout_principale = QVBoxLayout()
        layout_principale.addLayout(info_evento_layout)
        layout_principale.addSpacing(50)    # Distanzio di 50 pixel i layout tra di loro

        # Creazione del layout orizzontale per contenere dati_evento_layout e scelte_evento_layout
        layout_secondario = QHBoxLayout()
        layout_secondario.addLayout(dati_evento_layout)
        layout_secondario.addSpacing(20)    # Distanzio di 20 pixel i layout tra di loro
        layout_secondario.addLayout(scelte_evento_layout)

        layout_principale.addLayout(layout_secondario)

        # Impostazione del layout principale per il widget
        self.setLayout(layout_principale)   # cioè tutti i widget di self hanno come layout il layout principale

        button_modifica_evento = QPushButton("MODIFICA EVENTO", self)
        button_modifica_evento.clicked.connect(self.go_modifica_evento)
        scelte_evento_layout.addWidget(button_modifica_evento)

        button_elimina_evento = QPushButton('ELIMINA EVENTO')
        button_elimina_evento.clicked.connect(self.elimina_evento_callback)
        scelte_evento_layout.addWidget(button_elimina_evento)

        button_prenotazioni = QPushButton('PRENOTAZIONI')
        button_prenotazioni.clicked.connect(self.go_prenotazioni)
        scelte_evento_layout.addWidget(button_prenotazioni)

        button_ordini = QPushButton('ORDINI')
        button_ordini.clicked.connect(self.go_ordini)
        scelte_evento_layout.addWidget(button_ordini)

        self.setMaximumSize(800, 300)  # Fisso la dimensione massima della finestra
        self.resize(800, 300)  # Fisso la dimensione iniziale della finestra

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Visualizza Evento')

    def go_modifica_evento(self):
        self.vista_modifica_evento = VistaModificaEvento(self.evento1, callback=self.aggiorna_dati_evento)
        self.vista_modifica_evento.show()

    def go_prenotazioni(self):
        pass

    def go_ordini(self):
        self.vista_ordine = VistaOrdini()
        self.vista_ordine.set_evento_selezionato(self.evento1)
        self.vista_ordine.show()

    def aggiorna_dati_evento(self):
        # Aggiorna i widget della vista con i nuovi dati dell'evento
        self.label_nome.setText(f"{self.evento1.get_nome()}")
        self.label_data.setText(f"DATA: {self.evento1.get_data()}")
        self.label_tipo.setText(f"TIPO: {self.evento1.get_tipo()}")
        self.label_ingresso.setText(f"INGRESSO: {self.evento1.get_prezzo_ingresso()}")
        self.label_tavolo.setText(f"TAVOLO: {self.evento1.get_prezzo_tavolo()}")
        self.label_prive.setText(f"PRIVE: {self.evento1.get_prezzo_prive()}")

    def update_evento(self, evento):
        self.controller.set_evento(evento)
        self.evento1 = evento
        self.aggiorna_dati_evento()