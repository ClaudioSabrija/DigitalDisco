import pickle
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QPushButton, \
     QMessageBox, QListView

from Attività.Ordine import Ordine
from Gestione.GestoreEventi import GestoreEventi
from Viste.VistaNuovoOrdine import VistaNuovoOrdine


class VistaOrdini(QWidget):
    def __init__(self):
        super().__init__()

        gestore_eventi = GestoreEventi()
        self.layout = QHBoxLayout()
        self.ordine = Ordine()

        # Layout per la lista degli ordini e l'importo totale
        ordini_layout = QVBoxLayout()
        self.list_view = QListView()
        ordini_layout.addWidget(self.list_view)
        self.label_importo_totale = QLabel()
        ordini_layout.addWidget(self.label_importo_totale)

        self.layout.addLayout(ordini_layout)

        # Layout per la combo eventi e i pulsanti
        bottoni_layout = QVBoxLayout()

        self.combo_eventi = QComboBox()
        bottoni_layout.addWidget(self.combo_eventi)

        self.load_eventi()

        bottoni_layout.addLayout(bottoni_layout)

        self.btn_nuovo_ordine = QPushButton("NUOVO ORDINE")
        bottoni_layout.addWidget(self.btn_nuovo_ordine)
        self.btn_nuovo_ordine.clicked.connect(self.nuovo_ordine)

        self.btn_elimina_ordine = QPushButton("ELIMINA ORDINE")
        bottoni_layout.addWidget(self.btn_elimina_ordine)
        self.btn_elimina_ordine.clicked.connect(self.elimina_ordine)

        self.btn_stampa_ordine = QPushButton("STAMPA ORDINE")
        bottoni_layout.addWidget(self.btn_stampa_ordine)
        self.btn_stampa_ordine.clicked.connect(self.stampa_ordine)

        bottoni_layout.setSpacing(0)

        self.layout.addLayout(bottoni_layout)

        self.setLayout(self.layout)

        self.resize(500, 450)
        self.setWindowTitle("Lista Ordini")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

    def load_eventi(self):
        # Apri il file pickle
        with open('Dati/lista_eventi.pickle', 'rb') as file:
            self.gestore_eventi = pickle.load(file)

        # Ottieni i nomi degli eventi come lista di stringhe
        nomi_eventi = [evento.nome for evento in self.gestore_eventi]

        # Aggiungi i nomi degli eventi alla combo box
        self.combo_eventi.addItems(nomi_eventi)
        self.combo_eventi.currentIndexChanged.connect(self.cambia_evento)  # Aggiungi il segnale per il cambio evento

        # Imposta il primo evento come selezionato di default
        if self.combo_eventi.count() > 0:
            self.combo_eventi.setCurrentIndex(0)
            evento_selezionato = self.combo_eventi.currentText()
            self.carica_ordini(evento_selezionato)

    def nuovo_ordine(self):
        evento_selezionato = self.combo_eventi.currentText()
        ordine = Ordine()
        self.vista_nuovo_ordine = VistaNuovoOrdine(evento_selezionato, ordine, callback=self.update_ui)
        self.vista_nuovo_ordine.show()

    def elimina_ordine(self):
        # Ottieni l'indice dell'elemento selezionato nella list_view
        index = self.list_view.currentIndex()
        if index.isValid():
            # Ottieni il testo dell'ordine selezionato dalla list_view
            ordine_selezionato = self.list_view.model().itemData(index)[Qt.DisplayRole]
            #  Viene utilizzata per accedere al valore di visualizzazione di un elemento all'interno di un modello
            #  Qui serve per ottenere il testo dell'ordine selezionato dalla list_view.

            # Mostra un messaggio informativo
            QMessageBox.information(self, "Elimina Ordine", f"L'ordine {ordine_selezionato} è stato eliminato.")

            # Rimuovi l'ordine dalla lista degli ordini
            ordine = self.ordine.get_lista_ordini().pop(index.row())
            # Aggiorna la list_view
            self.aggiorna_list_view()

            # Rimuovi l'ordine dal file pickle corrispondente all'evento selezionato
            evento_selezionato = self.combo_eventi.currentText()
            file_pickle = f'Dati/Ordini/ordini_{evento_selezionato}.pickle'

            with open(file_pickle, 'wb') as file:
                # Scrivi nuovamente gli ordini rimanenti nel file pickle
                for ordine_in_lista in self.ordine.get_lista_ordini():
                    pickle.dump(ordine_in_lista, file)

    def stampa_ordine(self):
        index = self.list_view.currentIndex()
        if index.isValid():
            ordine_selezionato = self.list_view.model().itemData(index)[Qt.DisplayRole]
            QMessageBox.information(self, "Stampa Ordine",
                                    f"L'ordine {ordine_selezionato} è stato stampato correttamente.")

    def aggiorna_list_view(self):
        list_view_model = QStandardItemModel(self.list_view)
        for ordine in self.ordine.get_lista_ordini():
            item = QStandardItem()
            codice = f"Ordine: {ordine.codice}"
            item.setText(codice)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(13)
            item.setFont(font)
            list_view_model.appendRow(item)

        self.list_view.setModel(list_view_model)
        self.calcola_importo_totale()

    def update_ui(self, ordine):
        self.calcola_importo_totale()
        self.ordine.get_lista_ordini().append(ordine)
        self.aggiorna_list_view()  # Aggiorna la list_view
        # Aggiunge l'ordine alla lista degli ordini
        evento_selezionato = self.combo_eventi.currentText()

        with open(f'Dati/Ordini/ordini_{evento_selezionato}.pickle', 'wb') as file:
            for ordine in self.ordine.get_lista_ordini():
                pickle.dump(ordine, file)


    def carica_ordini(self, evento):
        self.ordine.get_lista_ordini().clear()
        file_pickle = f'Dati/Ordini/ordini_{evento}.pickle'
        if os.path.isfile(file_pickle):
            with open(file_pickle, 'rb') as file:
                while True:
                    try:
                        ordine = pickle.load(file)
                        if isinstance(ordine, Ordine):
                            self.ordine.get_lista_ordini().append(ordine)
                    except EOFError:
                        break
        self.aggiorna_list_view()  # Aggiorna la list_view

    def cambia_evento(self, index):
        evento_selezionato = self.combo_eventi.itemText(index)  # Viene chiamato quando viene selezionato un nuovo evento dalla combo box.
        self.carica_ordini(evento_selezionato)           # Questo metodo richiama la funzione carica_ordini passando il nome dell'evento
                                                     # selezionato, che a sua volta carica gli ordini corrispondenti da un file pickle specifico per quell'evento.

    def set_evento_selezionato(self, evento):
        index = self.combo_eventi.findText(evento.get_nome())
        self.combo_eventi.setCurrentIndex(index)

    def calcola_importo_totale(self):
        importo_totale = sum(ordine.prezzo_totale for ordine in self.ordine.get_lista_ordini())
        self.label_importo_totale.setText(f"Importo Totale: {importo_totale}\u20AC")
