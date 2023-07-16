from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QPushButton, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QIcon


class VistaVisualizzaOrdine(QWidget):
    def __init__(self, ordine):
        super().__init__()

        self.layout = QVBoxLayout()

        # Codice ordine
        codice_label = QLabel(f"Codice ordine: {ordine.get_codice()}")
        self.layout.addWidget(codice_label)

        # ListView per i prodotti dell'ordine
        prodotti_list_view = QListView()
        self.layout.addWidget(prodotti_list_view)

        # Modello per i prodotti dell'ordine
        prodotti_model = QStandardItemModel(prodotti_list_view)
        for prodotto, quantita, prezzo in ordine.prodotti:
            item = QStandardItem(f"{prodotto.get_nome()} - Quantità: {quantita} - Prezzo: {prezzo}\u20AC")
            prodotti_model.appendRow(item)

        prodotti_list_view.setModel(prodotti_model)

        self.btn_stampa_ordine = QPushButton("STAMPA ORDINE")
        self.layout.addWidget(self.btn_stampa_ordine)
        self.btn_stampa_ordine.clicked.connect(self.stampa_ordine)

        self.setLayout(self.layout)
        self.setFont(QFont('Arial Nova Light'))
        self.setWindowTitle("Visualizza Ordine")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setFixedSize(500, 300)

    def stampa_ordine(self):
        QMessageBox.information(self, "Stampa Ordine",
                                f"L'ordine è stato stampato correttamente.")
        self.close()
