from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout

from Gestione.GestoreBottiglie import GestoreBottiglie


class VistaVisualizzaBottiglia(QWidget):

    def __init__(self, bottiglia, parent=None):
        super(VistaVisualizzaBottiglia, self).__init__(parent)
        self.controller = GestoreBottiglie(bottiglia)

        self.grid_layout = QGridLayout()
        v_layout = QVBoxLayout()

        font = QFont('Arial Nova Light')
        font_bold = QFont()

        label_didascalia = QLabel("Dettagli Prodotto:")
        label_didascalia.setFont(font)
        font_bold.setBold(True)
        label_didascalia.setFont(font_bold)
        label_didascalia.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_didascalia)

        label_nome = QLabel("Nome: {} ".format(self.controller.get_nome_bottiglia()))
        font.setPointSize(15)
        label_nome.setFont(font)
        v_layout.addWidget(label_nome)

        label_prezzo = QLabel("Prezzo: {} ".format(self.controller.get_prezzo_bottiglia()))
        font.setPointSize(15)
        label_prezzo.setFont(font)
        v_layout.addWidget(label_prezzo)

        label_disponibilita = QLabel("Disponibilità: {}".format(self.controller.get_disponibilta_bottiglia()))
        font.setPointSize(15)
        label_disponibilita.setFont(font)
        v_layout.addWidget(label_disponibilita)

        #v_layout.addItem(QSpacerItem(2, 2, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_didascalia1 = QLabel("Posizione:")
        label_didascalia1.setFont(font)
        font_bold.setBold(True)
        label_didascalia1.setFont(font_bold)
        label_didascalia1.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_didascalia1)

        label_corridoio = QLabel("Corridoio: {}".format(self.controller.get_corridoio_bottiglia()))
        font.setPointSize(15)
        label_corridoio.setFont(font)
        v_layout.addWidget(label_corridoio)

        label_scaffale = QLabel("Scaffale: {}".format(self.controller.get_scaffale_bottiglia()))
        font.setPointSize(15)
        label_scaffale.setFont(font)
        v_layout.addWidget(label_scaffale)

        label_piano = QLabel("Piano: {}".format(self.controller.get_piano_bottiglia()))
        font.setPointSize(15)
        label_piano.setFont(font)
        v_layout.addWidget(label_piano)

        pixmap = QPixmap('Dati/DigitalDisco/{}.png'.format(self.controller.get_nome_bottiglia()))
        pixmap5 = pixmap.scaled(100, 30)
        pixmap.size()
        label_im = QLabel()
        label_im.setPixmap(pixmap5)
        label_im.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_im)

        v_layout.addLayout(self.grid_layout)
        self.setLayout(v_layout)
        self.setFont(QFont('Arial Nova Light', 14))
        self.setWindowTitle("Bottiglia: " + self.controller.get_nome_bottiglia())
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

        self.setMaximumSize(800, 700)
        self.resize(500, 600)
        self.move(0, 0)