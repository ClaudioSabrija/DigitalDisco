from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout

from Gestione.GestoreCocktail import GestoreCocktail

class VistaVisualizzaCocktail(QWidget):

    def __init__(self, cocktail, parent=None):
        super(VistaVisualizzaCocktail, self).__init__(parent)
        self.controller = GestoreCocktail(cocktail)

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

        label_nome = QLabel("Nome: {} ".format(self.controller.get_nome_cocktail()))
        font.setPointSize(15)
        label_nome.setFont(font)
        v_layout.addWidget(label_nome)

        label_prezzo = QLabel("Prezzo: {}€".format(self.controller.get_prezzo_cocktail()))
        font.setPointSize(15)
        label_prezzo.setFont(font)
        v_layout.addWidget(label_prezzo)

        pixmap = QPixmap('Dati/DigitalDisco/{}.png'.format(self.controller.get_nome_cocktail()))
        pixmap5 = pixmap.scaled(100, 30)
        pixmap.size()
        label_im = QLabel()
        label_im.setPixmap(pixmap5)
        label_im.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_im)

        v_layout.addLayout(self.grid_layout)
        self.setLayout(v_layout)
        self.setFont(QFont('Arial Nova Light', 14))
        self.setWindowTitle("Bottiglia: " + self.controller.get_nome_cocktail())
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

        self.setMaximumSize(300, 400)
        self.resize(300, 400)
        self.move(0, 0)
