import pickle, os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QPushButton, \
    QListWidget, QListWidgetItem, QMessageBox

from Gestione.GestoreEventi import GestoreEventi
from Viste.VistaNuovoOrdine import VistaNuovoOrdine


class VistaOrdini(QWidget):
    def __init__(self):
        super().__init__()

        gestore_eventi = GestoreEventi()
        self.layout = QHBoxLayout()
        self.lista_ordini = []

        # Layout per la lista degli ordini e l'importo totale
        ordini_layout = QVBoxLayout()
        self.list_view = QListWidget()
        ordini_layout.addWidget(self.list_view)
        self.label_importo_totale = QLabel("Importo totale: 0")
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
        self.vista_nuovo_ordine = VistaNuovoOrdine(evento_selezionato, callback=self.update_ui)
        self.vista_nuovo_ordine.show()

    def elimina_ordine(self):
        # Carica il file pickle corrispondente all'evento selezionato.
        if self.list_view.currentItem() is not None:
            ordine_selezionato = self.list_view.currentItem().text()
            self.list_view.takeItem(self.list_view.currentRow())  # Rimuovi l'ordine dalla list_view

        # Leggi gli ordini uno per uno e aggiungili a una nuova lista chiamata "ordini",escludendo l'ordine selezionato.
            evento_selezionato = self.combo_eventi.currentText()
            file_pickle = f'Dati/Ordini/ordini_{evento_selezionato}.pickle'
            if os.path.isfile(file_pickle):
                with open(file_pickle, 'rb') as file:
                    ordini = []
                    while True:
                        try:
                            ordine = pickle.load(file)
                            if isinstance(ordine, str) and ordine != ordine_selezionato:
                                ordini.append(ordine)
                            elif isinstance(ordine, QListWidgetItem) and ordine.text() != ordine_selezionato:
                                ordini.append(ordine.text())
                        except EOFError:
                            break

        # Sovrascrivi il file pickle corrispondente con la lista "ordini" aggiornata.
                with open(file_pickle, 'wb') as file:
                    for ordine in ordini:
                        pickle.dump(ordine, file)


    def stampa_ordine(self):
        if self.list_view.currentItem() is not None:
            ordine_selezionato = self.list_view.currentItem().text()
            nome_finestra = f"{ordine_selezionato}"
            msg_box = QMessageBox()
            msg_box.setWindowTitle(nome_finestra)
            msg_box.setWindowIcon(QIcon('Dati/DigitalDisco.png'))  # Impostazione dell'icona della finestra
            msg_box.setText(f"L'{ordine_selezionato} è stato stampato correttamente!")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.exec_()


    def aggiorna_list_view(self):
        self.list_view.clear()  # Pulisce la list_view

        for ordine in self.lista_ordini:
            self.list_view.addItem(ordine)  # Aggiunge gli ordini alla list_view

    def update_ui(self, ordine):
        self.lista_ordini.append(ordine)  # Aggiunge l'ordine alla lista degli ordini
        self.aggiorna_list_view()  # Aggiorna la list_view
        evento_selezionato = self.combo_eventi.currentText()
        with open(f'Dati/Ordini/ordini_{evento_selezionato}.pickle', 'wb') as file:
            for ordine in self.lista_ordini:
                pickle.dump(ordine, file)

    def carica_ordini(self, evento):
        self.lista_ordini.clear()
        file_pickle = f'Dati/Ordini/ordini_{evento}.pickle'
        if os.path.isfile(file_pickle):
            with open(file_pickle, 'rb') as file:
                while True:
                    try:
                        ordine = pickle.load(file)
                        if isinstance(ordine, str):
                            self.lista_ordini.append(ordine)
                        elif isinstance(ordine, QListWidgetItem):
                            self.lista_ordini.append(ordine.text())
                    except EOFError:
                        break

        self.aggiorna_list_view()  # Aggiorna la list_view

    def cambia_evento(self, index):
        evento_selezionato = self.combo_eventi.itemText(index)  # Viene chiamato quando viene selezionato un nuovo evento dalla combo box.
        self.carica_ordini(evento_selezionato)           # Questo metodo richiama la funzione carica_ordini passando il nome dell'evento
                                                     # selezionato, che a sua volta carica gli ordini corrispondenti da un file pickle specifico per quell'evento.