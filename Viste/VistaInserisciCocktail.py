from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QComboBox, QDateTimeEdit, QMessageBox


class VistaInserisciCocktail(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaInserisciCocktail, self).__init__(parent)
        self.callback = callback
        # Creazione dei widget
        label_top = QLabel("Inserisci i dati del prodotto:", self)
        label_nome = QLabel("NOME:", self)
        label_prezzo = QLabel("PREZZO:", self)

        self.line_edit_nome = QLineEdit(self)
        self.line_edit_prezzo = QLineEdit(self)

        button_conferma = QPushButton("Conferma", self)
        button_conferma.clicked.connect(self.add_cocktail)

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Inserisci Cocktail')
        #self.setFixedSize(400, 600)  # Imposta la dimensione fissa della finestra di dialogo
        label_top.setFixedSize(300, 30)  # Imposta la dimensione fissa della label superiore

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(label_top)
        layout.addWidget(label_nome)
        layout.addWidget(self.line_edit_nome)
        layout.addWidget(label_prezzo)
        layout.addWidget(self.line_edit_prezzo)
        layout.addWidget(button_conferma)

        self.setLayout(layout)

    def add_cocktail(self):
        pass