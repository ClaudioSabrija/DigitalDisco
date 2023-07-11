from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

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

        self.setLayout(self.layout)