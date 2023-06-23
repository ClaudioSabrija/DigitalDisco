from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton, QHBoxLayout

from Gestione.GestoreCocktail import GestoreCocktail
from Viste.VistaModificaCocktail import VistaModificaCocktail


class VistaVisualizzaCocktail(QWidget):

    def __init__(self, cocktail, parent=None):
        super(VistaVisualizzaCocktail, self).__init__(parent)
        self.controller = GestoreCocktail(cocktail)

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

        self.label_nome = QLabel("Nome: {} ".format(self.controller.get_nome_cocktail()))
        font.setPointSize(15)
        self.label_nome.setFont(font)
        v_layout.addWidget(self.label_nome)

        self.label_prezzo = QLabel("Prezzo: {}€".format(self.controller.get_prezzo_cocktail()))
        font.setPointSize(15)
        self.label_prezzo.setFont(font)
        v_layout.addWidget(self.label_prezzo)

        button_modifica_cocktail = QPushButton("MODIFICA")
        button_modifica_cocktail.setFixedSize(90, 30)
        button_modifica_cocktail.setFont(QFont("Arial", 10))
        button_modifica_cocktail.clicked.connect(self.edit_cocktail)

        button_elimina_cocktail = QPushButton("ELIMINA")
        button_elimina_cocktail.setFixedSize(90, 30)
        button_elimina_cocktail.setFont(QFont("Arial", 10))
        button_elimina_cocktail.clicked.connect(self.delete_cocktail)

        button_layout.addWidget(button_modifica_cocktail)
        button_layout.addWidget(button_elimina_cocktail)

        v_layout.addLayout(button_layout)

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
        self.setWindowTitle("Cocktail: " + self.controller.get_nome_cocktail())
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

        self.setMaximumSize(300, 400)
        self.resize(300, 400)
        self.move(0, 0)

    def update_ui(self):
        # Aggiorna le informazioni visualizzate con i nuovi valori del cocktail
        self.label_nome.setText("Nome: {}".format(self.controller.get_nome_cocktail()))
        self.label_prezzo.setText("Prezzo: {}€".format(self.controller.get_prezzo_cocktail()))

    def edit_cocktail(self):
        self.vista_modifica_cocktail = VistaModificaCocktail(self.controller.get_cocktail(), self.update_cocktail)
        self.vista_modifica_cocktail.show()

    def delete_cocktail(self):
        pass

    def update_cocktail(self, cocktail):
        self.controller.set_cocktail(cocktail)
        self.update_ui()

