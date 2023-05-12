from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QSizePolicy, \
    QHBoxLayout

class VistaHomeBarman(QWidget):
    def __init__(self, parent = None):
        super(VistaHomeBarman, self).__init__(parent)

        grid_layout = QGridLayout()
        v_layout = QHBoxLayout()

        v_layout.addWidget(self.get_generic_button("Preleva Prodotto", "rgb(254,254,254)", self.go_vista_lista_prodotti))
        v_layout.addSpacing(30)
        v_layout.addWidget(self.get_generic_button("Ordini", "rgb(254,254,254)", self.go_ordini))



        label = QLabel('Gestione Ordini')
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 30px;""color: white;")
        grid_layout.addWidget(label, 1, 1)
        grid_layout.addLayout(v_layout, 2, 1)

        self.setLayout(grid_layout)

        self.setWindowTitle("Home:Barman")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setStyleSheet("background-color: #484848;")

        self.setLayout(grid_layout)
        self.setMaximumSize(900, 250)
        self.resize(910, 650)
        self.move(0, 0)

        # Funzione che viene richiamata per creare un bottone.

    def get_generic_button(self, titolo, colore, on_click):
        button = QPushButton(titolo)
        button.setStyleSheet("background-color: {}".format(colore))
        button.setFont(QFont('Arial Nova Light', 14))
        button.setFixedSize(300, 150)
        #button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_vista_lista_prodotti(self):
        pass

    def go_ordini(self):
        pass