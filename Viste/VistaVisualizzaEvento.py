from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, \
    QComboBox, QDateTimeEdit, QMessageBox, QHBoxLayout

from Viste import VistaInserisciEvento
from Evento.Evento import Evento
from Gestione.GestoreEventi import GestoreEventi
from Viste import VistaCalendarioEventi


class VistaVisualizzaEvento(QWidget):
    def __init__(self, evento, elimina_evento_callback=None, parent=None):
        super(VistaVisualizzaEvento, self).__init__(parent)
        self.evento1 = evento
        self.elimina_evento_callback = elimina_evento_callback

        info_evento_layout = QHBoxLayout()
        scelte_evento_layout = QVBoxLayout()
        dati_evento_layout = QVBoxLayout()

        # Creazione dei widget

        label_nome = QLabel(f"{self.evento1.get_nome()}", self)
        label_data = QLabel(f"DATA: {self.evento1.get_data()}", self)
        label_tipo = QLabel(f"TIPO: {self.evento1.get_tipo()}", self)
        label_ingresso = QLabel(f"INGRESSO: {self.evento1.get_prezzo_ingresso()}", self)
        label_tavolo = QLabel(f"TAVOLO: {self.evento1.get_prezzo_tavolo()}", self)
        label_prive = QLabel(f"PRIVE: {self.evento1.get_prezzo_prive()}", self)

        #Impostazione del Font
        font = QFont('Arial Nova Light')
        font_nome = QFont('Arial Nova Light')
        font_nome.setBold(True)
        font_nome.setUnderline(True)
        font.setPointSize(15)
        font_nome.setPointSize(20)


        label_nome.setFont(font_nome)
        label_nome.setAlignment(Qt.AlignCenter)


        labels = [label_data, label_tipo, label_ingresso, label_tavolo, label_prive]  # Aggiungo tutte le tue label a questa lista

        for label in labels:
            label.setFont(font)
            label.setAlignment(Qt.AlignLeft)

        #Aggiunta delle label al layout delle informazioni

        info_evento_layout.addWidget(label_nome)

        dati_evento_layout.addWidget(label_data)
        dati_evento_layout.addWidget(label_tipo)
        dati_evento_layout.addWidget(label_ingresso)
        dati_evento_layout.addWidget(label_tavolo)
        dati_evento_layout.addWidget(label_prive)

        # Creazione del layout principale
        layout_principale = QVBoxLayout()
        layout_principale.addLayout(info_evento_layout)
        layout_principale.addSpacing(50)    #Distanzio di 50 pixel i layout tra di loro

        # Creazione del layout orizzontale per contenere dati_evento_layout e scelte_evento_layout
        layout_secondario = QHBoxLayout()
        layout_secondario.addLayout(dati_evento_layout)
        layout_secondario.addSpacing(20)    #Distanzio di 20 pixel i layout tra di loro
        layout_secondario.addLayout(scelte_evento_layout)

        layout_principale.addLayout(layout_secondario)

        # Impostazione del layout principale per il widget
        self.setLayout(layout_principale)   #cioè tutti i widget di self hanno come layout il layout principale



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


        self.setMaximumSize(800,300)  #Fisso la dimensione massima della finestra
        self.resize(800, 300)  #Fisso la dimensione iniziale della finestra


        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Visualizza Evento')


    def elimina_evento_click(self, evento_da_eliminare):
        pass

    def go_modifica_evento(self):
        pass

    def go_prenotazioni(self):
        pass

    def go_ordini(self):
        pass