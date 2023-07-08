from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QComboBox, QDateTimeEdit, QMessageBox

from Magazzino.Cocktail import Cocktail
from Magazzino.Magazzino import Magazzino


class VistaModificaCocktail(QWidget):
    def __init__(self, cocktail, callback, callback_modifica, parent=None):
        super(VistaModificaCocktail, self).__init__(parent)

        self.callback_modifica = callback_modifica
        self.callback = callback
        self.magazzino = Magazzino()
        self.cocktail = cocktail

        # Creazione dei widget
        label_top = QLabel("Modifica i dati del prodotto:", self)
        label_nome = QLabel("NOME:", self)
        label_prezzo = QLabel("PREZZO:", self)

        self.line_edit_nome = QLineEdit(self)
        self.line_edit_prezzo = QLineEdit(self)

        button_conferma = QPushButton("Conferma", self)
        button_conferma.clicked.connect(self.modifica_cocktail)

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Modifica Cocktail')
        #self.setFixedSize(400, 600)  # Imposta la dimensione fissa della finestra di dialogo
        label_top.setFixedSize(300, 30)  # Imposta la dimensione fissa della label superiore

        # Inizializza i campi con i valori attuali del cocktail
        self.line_edit_nome.setText(self.cocktail.nome)
        self.line_edit_prezzo.setText(str(self.cocktail.prezzo))

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(label_top)
        layout.addWidget(label_nome)
        layout.addWidget(self.line_edit_nome)
        layout.addWidget(label_prezzo)
        layout.addWidget(self.line_edit_prezzo)
        layout.addWidget(button_conferma)

        self.setLayout(layout)

    def modifica_cocktail(self):
        # Ottenere i valori inseriti dall'utente
        nome = self.line_edit_nome.text().strip()
        prezzo = self.line_edit_prezzo.text().strip()

        if not nome or not prezzo:
            QMessageBox.warning(self, "Errore", "Tutti i campi devono essere compilati.")
            return

        try:
            prezzo = int(prezzo)
        except ValueError:
            QMessageBox.warning(self, "Errore", "Il prezzo dev'essere scritto in numero.")
            return

        self.cocktail.nome = nome
        self.cocktail.prezzo = prezzo

        cocktail_modificato = Cocktail(nome, prezzo)

        self.callback_modifica(cocktail_modificato)
        self.callback(self.cocktail, cocktail_modificato)
        self.close()
