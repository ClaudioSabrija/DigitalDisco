import pickle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QPushButton, QListWidget

from Gestione.GestoreEventi import GestoreEventi
from Viste.VistaNuovoOrdine import VistaNuovoOrdine


class VistaOrdini(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        # Layout per la lista degli ordini e l'importo totale
        ordini_layout = QVBoxLayout()
        self.list_view = QListWidget()
        ordini_layout.addWidget(self.list_view)
        self.label_importo_totale = QLabel("Importo totale: 0")
        ordini_layout.addWidget(self.label_importo_totale)

        self.layout.addLayout(ordini_layout)

        # Layout per la combo eventi e i pulsanti
        bottoni_layout = QVBoxLayout()

        self.combo_eventi = QComboBox()
        bottoni_layout.addWidget(self.combo_eventi)

        self.load_eventi()

        bottoni_layout.addLayout(bottoni_layout)

        self.btn_nuovo_ordine = QPushButton("NUOVO ORDINE")
        bottoni_layout.addWidget(self.btn_nuovo_ordine)
        self.btn_nuovo_ordine.clicked.connect(self.nuovo_ordine)

        self.btn_elimina_ordine = QPushButton("ELIMINA ORDINE")
        bottoni_layout.addWidget(self.btn_elimina_ordine)
        self.btn_elimina_ordine.clicked.connect(self.elimina_ordine)

        self.btn_visualizza_ordine = QPushButton("VISUALIZZA ORDINE")
        bottoni_layout.addWidget(self.btn_visualizza_ordine)
        self.btn_visualizza_ordine.clicked.connect(self.visualizza_ordine)

        bottoni_layout.setSpacing(0)

        self.layout.addLayout(bottoni_layout)

        self.setLayout(self.layout)

        self.resize(500, 450)
        self.setWindowTitle("Lista Ordini")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

    def load_eventi(self):

        gestore_eventi = GestoreEventi()

        # Apri il file pickle
        with open('Dati/lista_eventi.pickle', 'rb') as file:
            gestore_eventi = pickle.load(file)

        # Ottieni i nomi degli eventi come lista di stringhe
        nomi_eventi = [evento.nome for evento in gestore_eventi]

        # Aggiungi i nomi degli eventi alla combo box
        self.combo_eventi.addItems(nomi_eventi)

    def nuovo_ordine(self):
        self.vista_nuovo_ordine = VistaNuovoOrdine()
        self.vista_nuovo_ordine.show()

    def elimina_ordine(self):
        pass

    def visualizza_ordine(self):
        pass


