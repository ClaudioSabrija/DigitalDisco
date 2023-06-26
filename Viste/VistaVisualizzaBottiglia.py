from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QHBoxLayout, QPushButton

from Gestione.GestoreBottiglie import GestoreBottiglie
from Viste.VistaModificaBottiglia import VistaModificaBottiglia


class VistaVisualizzaBottiglia(QWidget):

    def __init__(self, bottiglia, parent=None):
        super(VistaVisualizzaBottiglia, self).__init__(parent)

        self.controller = GestoreBottiglie(bottiglia)

        self.grid_layout = QGridLayout()
        v_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        font = QFont('Arial Nova Light')
        font_bold = QFont()

        label_didascalia = QLabel("Dettagli Prodotto:")
        label_didascalia.setFont(font)
        font_bold.setBold(True)
        label_didascalia.setFont(font_bold)
        label_didascalia.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_didascalia)

        self.label_nome = QLabel("Nome: {} ".format(self.controller.get_nome_bottiglia()))
        font.setPointSize(15)
        self.label_nome.setFont(font)
        v_layout.addWidget(self.label_nome)

        self.label_prezzo = QLabel("Prezzo: {}€ ".format(self.controller.get_prezzo_bottiglia()))
        font.setPointSize(15)
        self.label_prezzo.setFont(font)
        v_layout.addWidget(self.label_prezzo)

        self.label_disponibilita = QLabel("Disponibilità: {}".format(self.controller.get_disponibilta_bottiglia()))
        font.setPointSize(15)
        self.label_disponibilita.setFont(font)
        v_layout.addWidget(self.label_disponibilita)

        self.label_didascalia1 = QLabel("Posizione:")
        self.label_didascalia1.setFont(font)
        font_bold.setBold(True)
        self.label_didascalia1.setFont(font_bold)
        self.label_didascalia1.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(self.label_didascalia1)

        self.label_corridoio = QLabel("Corridoio: {}".format(self.controller.get_corridoio_bottiglia()))
        font.setPointSize(15)
        self.label_corridoio.setFont(font)
        v_layout.addWidget(self.label_corridoio)

        self.label_scaffale = QLabel("Scaffale: {}".format(self.controller.get_scaffale_bottiglia()))
        font.setPointSize(15)
        self.label_scaffale.setFont(font)
        v_layout.addWidget(self.label_scaffale)

        self.label_piano = QLabel("Piano: {}".format(self.controller.get_piano_bottiglia()))
        font.setPointSize(15)
        self.label_piano.setFont(font)
        v_layout.addWidget(self.label_piano)

        button_modifica_bottiglia = QPushButton("MODIFICA")
        button_modifica_bottiglia.setFixedSize(90, 30)
        button_modifica_bottiglia.setFont(QFont("Arial", 10))
        button_modifica_bottiglia.clicked.connect(self.edit_bottiglia)

        button_elimina_bottiglia = QPushButton("ELIMINA")
        button_elimina_bottiglia.setFixedSize(90, 30)
        button_elimina_bottiglia.setFont(QFont("Arial", 10))
        button_elimina_bottiglia.clicked.connect(self.delete_bottiglia)

        button_layout.addWidget(button_modifica_bottiglia)
        button_layout.addWidget(button_elimina_bottiglia)

        v_layout.addLayout(button_layout)

        v_layout.addLayout(self.grid_layout)
        self.setLayout(v_layout)
        self.setFont(QFont('Arial Nova Light', 14))
        self.setWindowTitle("Bottiglia: " + self.controller.get_nome_bottiglia())
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

        self.setMaximumSize(400, 600)
        self.resize(400, 600)
        self.move(0, 0)

    def update_ui(self):
        # Aggiorna le informazioni visualizzate con i nuovi valori della bottiglia
        self.label_nome.setText("Nome: {}".format(self.controller.get_nome_bottiglia()))
        self.label_prezzo.setText("Prezzo: {}€".format(self.controller.get_prezzo_bottiglia()))
        self.label_disponibilita.setText("Disponibilità: {}".format(self.controller.get_disponibilta_bottiglia()))

        self.label_corridoio.setText("Corridoio: {}".format(self.controller.get_corridoio_bottiglia()))
        self.label_scaffale.setText("Scaffale: {}".format(self.controller.get_scaffale_bottiglia()))
        self.label_piano.setText("Piano: {}".format(self.controller.get_piano_bottiglia()))

    def edit_bottiglia(self):
        self.vista_modifica_bottiglia = VistaModificaBottiglia(self.controller.get_bottiglia(), self.update_bottiglia)
        self.vista_modifica_bottiglia.show()

    def delete_bottiglia(self):
        pass

    def update_bottiglia(self, bottiglia):
        self.controller.set_bottiglia(bottiglia)
        self.update_ui()

