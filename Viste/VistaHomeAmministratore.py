from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget,QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QSizePolicy

from Viste.VistaMagazzino import VistaMagazzino


class VistaHomeAmministratore(QWidget):
    def __init__(self, parent = None):
        super(VistaHomeAmministratore, self).__init__(parent)

        grid_layout = QGridLayout()
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_button("Calendario Eventi", "rgb(192,192,192)", self.go_calendario_eventi))
        v_layout.addWidget(self.get_generic_button("Ordini", "rgb(182,182,182)", self.go_ordini))
        v_layout.addWidget(self.get_generic_button("Magazzino", "rgb(172,172,172)", self.go_magazzino))
        v_layout.addWidget(self.get_generic_button("Statistiche", "rgb(162,162,162)", self.go_statistiche))

        label = QLabel()
        pixmap = QPixmap('Dati/DigitalDisco.png')
        pixmap.size()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        grid_layout.addWidget(label, 0, 0)
        grid_layout.addLayout(v_layout, 0, 1)

        self.setLayout(grid_layout)

        self.setWindowTitle("Home:Amministratore")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

        self.setLayout(grid_layout)
        self.setMaximumSize(1000, 650)
        self.resize(910, 650)
        self.move(0, 0)

        # Funzione che viene richiamata per creare un bottone.

    def get_generic_button(self, titolo, colore, on_click):
        button = QPushButton(titolo)
        button.setStyleSheet("background-color: {}".format(colore))
        button.setFont(QFont('Arial Nova Light', 18))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

        # Funzione che mostra la vista del calendario dei vaccini.

    def go_calendario_eventi(self):
        pass


        # Funzione che mostra la vista del calendario dei tamponi.

    def go_ordini(self):
        pass

        # Funzione che mostra la vista del magazzino.

    def go_magazzino(self):
        self.vista_magazzino = VistaMagazzino()
        self.vista_magazzino.show()

        # Funzione che mostra la vista delle statistiche.

    def go_statistiche(self):
        pass