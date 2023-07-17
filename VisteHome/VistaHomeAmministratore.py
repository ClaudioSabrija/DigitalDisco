from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout
from pyqt5_plugins.examplebuttonplugin import QtGui

from GestoreMagazzino.View.VistaMagazzino import VistaMagazzino
from GestoreEventi.View.VistaCalendarioEventi import VistaCalendarioEventi
from GestoreOrdini.View.VistaOrdini import VistaOrdini
from GestoreStatistiche.VistaStatistiche import VistaStatistiche

class VistaHomeAmministratore(QWidget):
    def __init__(self, parent = None):
        super(VistaHomeAmministratore, self).__init__(parent)

        grid_layout = QGridLayout()
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_button("Calendario Eventi", "rgb(254,254,254)", self.go_calendario_eventi))
        v_layout.addWidget(self.get_generic_button("Ordini", "rgb(254,254,254)", self.go_ordini))
        v_layout.addWidget(self.get_generic_button("Magazzino", "rgb(254,254,254)", self.go_magazzino))
        v_layout.addWidget(self.get_generic_button("Statistiche", "rgb(254,254,254)", self.go_statistiche))

        label = QLabel()
        pixmap = QtGui.QPixmap("Dati/DigitalDisco.png")
        scaled_pixmap = pixmap.scaled(700, 500)
        label.setPixmap(scaled_pixmap)
        label.setAlignment(Qt.AlignCenter)

        grid_layout.addWidget(label, 0, 0)
        grid_layout.addLayout(v_layout, 0, 1)

        self.setLayout(grid_layout)

        self.setWindowTitle("Home:Amministratore")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setStyleSheet("background-color: #484848;")

        self.setLayout(grid_layout)
        self.setMaximumSize(1000, 650)
        self.resize(910, 650)
        self.move(400, 150)

        # Funzione che viene richiamata per creare un bottone.

    def get_generic_button(self, titolo, colore, on_click):
        button = QPushButton(titolo)
        button.setStyleSheet("background-color: {}".format(colore))
        button.setFont(QFont('Arial Nova Light', 14))
        button.setFixedSize(300, 50)
        button.clicked.connect(on_click)
        return button

    def go_calendario_eventi(self):
        self.vista_calendario_eventi = VistaCalendarioEventi()
        self.vista_calendario_eventi.show()

    def go_ordini(self):
        self.vista_ordini= VistaOrdini()
        self.vista_ordini.show()

        # Funzione che mostra la vista del magazzino.

    def go_magazzino(self):
        self.vista_magazzino = VistaMagazzino()
        self.vista_magazzino.show()

        # Funzione che mostra la vista delle statistiche.

    def go_statistiche(self):
        self.vista_statistiche = VistaStatistiche()
        self.vista_statistiche.show()