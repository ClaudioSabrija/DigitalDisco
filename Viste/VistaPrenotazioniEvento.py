import os.path, pickle

from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListView, QPushButton, QInputDialog, QLabel, QLineEdit, QMessageBox

from Attività.Prenotazione import Prenotazione
from Viste.VistaInserisciPrenotazione import VistaInserisciPrenotazione
from Viste.VistaVisualizzaPrenotazione import VistaVisualizzaPrenotazione
from Viste.VistaModificaPrenotazione import VistaModificaPrenotazione
from Gestione.GestorePrenotazioni import GestorePrenotazioni

from Evento.Evento import Evento


class VistaPrenotazioniEvento(QWidget):
    def __init__(self, evento_selezionato, parent=None):
        super().__init__(parent)
        self.evento = evento_selezionato
        self.controller = GestorePrenotazioni()

        self.layout = QVBoxLayout()

        # Barra di ricerca
        ricerca_layout = QHBoxLayout()
        ricerca_label = QLabel("Ricerca:")
        self.ricerca_line_edit = QLineEdit()
        self.ricerca_line_edit.textChanged.connect(self.ricerca_prenotazione)
        ricerca_layout.addWidget(ricerca_label)
        ricerca_layout.addWidget(self.ricerca_line_edit)
        self.layout.addLayout(ricerca_layout)

        # ListView per i prodotti selezionati
        self.list_view_prenotazioni = QListView()
        self.layout.addWidget(self.list_view_prenotazioni)

        # Layout per i bottoni
        buttons_layout = QVBoxLayout()

        # Bottone "Inserisci Prenotazione"
        self.button_inserisci_prenotazione = QPushButton("Inserisci Prenotazione")
        buttons_layout.addWidget(self.button_inserisci_prenotazione)
        self.button_inserisci_prenotazione.clicked.connect(self.show_vista_inserisci_prenotazione)

        # Bottone "Visualizza Prenotazione"
        self.button_visualizza_prenotazione = QPushButton("Visualizza Prenotazione")
        buttons_layout.addWidget(self.button_visualizza_prenotazione)
        self.button_visualizza_prenotazione.clicked.connect(self.show_vista_visualizza_prenotazione)

        self.layout.addLayout(buttons_layout)

        self.setLayout(self.layout)
        self.resize(650, 550)
        self.setWindowTitle("Prenotazioni Evento")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

        self.load_prenotazioni(self.evento)
        self.update_ui_prenotazioni(self.evento)


    def ricerca_prenotazione(self):
        if os.path.isfile(f'Dati/Prenotazioni/prenotazioni_{self.evento.nome}.pickle'):
            with open(f'Dati/Prenotazioni/prenotazioni_{self.evento.nome}.pickle', 'rb') as f:
                self.evento.lista_prenotazioni = pickle.load(f)
                self.prenotazioni = self.evento.lista_prenotazioni

        ricerca_text = self.ricerca_line_edit.text().lower()
        self.list_view_model = QStandardItemModel(self.list_view_prenotazioni)

        # Popola il modello con tutte le prenotazioni
        for prenotazione in self.evento.lista_prenotazioni:
            item = QStandardItem()
            nome = f"{prenotazione.nome}"
            cognome = f"{prenotazione.cognome}"
            codice_fiscale = f"{prenotazione.codice_fiscale}"
            testo = f"{nome} {cognome} {codice_fiscale}"
            item.setText(testo)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.list_view_model.appendRow(item)

        # Esegui la ricerca sul modello
        for row in range(self.list_view_model.rowCount()):
            codice_fiscale_prenotazione = self.list_view_model.item(row).text().lower()

            if ricerca_text and ricerca_text in codice_fiscale_prenotazione:
                self.list_view_prenotazioni.setRowHidden(row, False)
            else:
                self.list_view_prenotazioni.setRowHidden(row, ricerca_text != "")


    def show_vista_inserisci_prenotazione(self):
        self.vista_inserisci_prenotazione = VistaInserisciPrenotazione(self.evento, self.load_prenotazioni, self.update_ui_prenotazioni)
        self.vista_inserisci_prenotazione.show()

    def show_vista_visualizza_prenotazione(self):
        if self.list_view_prenotazioni.selectedIndexes():
            indice_selezionato = self.list_view_prenotazioni.selectedIndexes()[0].row()
            prenotazione_selezionata = self.controller.get_prenotazione_by_index(self.evento, indice_selezionato)

            self.vista_prenotazione = VistaVisualizzaPrenotazione(self.evento, prenotazione_selezionata, self.update_ui_prenotazioni, self.elimina_prenotazione, self.show_vista_modifica_prenotazione, self.show_vista_visualizza_pdf)
            self.vista_prenotazione.show()

    def show_vista_modifica_prenotazione(self):
        if self.list_view_prenotazioni.selectedIndexes():
            indice_selezionato = self.list_view_prenotazioni.selectedIndexes()[0].row()
            prenotazione_selezionata = self.controller.get_prenotazione_by_index(self.evento, indice_selezionato)

            self.vista_modifica_prenotazione = VistaModificaPrenotazione(self.evento, prenotazione_selezionata, self.controller.aggiorna_prenotazione, self.vista_prenotazione.update_ui_prenotazione)
            self.vista_modifica_prenotazione.show()
            self.vista_prenotazione.close()


    def show_vista_visualizza_pdf(self):
        pass


    def load_prenotazioni(self, evento):
        if os.path.isfile(f'Dati/Prenotazioni/prenotazioni_{evento.nome}.pickle'):
            with open(f'Dati/Prenotazioni/prenotazioni_{evento.nome}.pickle', 'rb') as f:
                self.evento.lista_prenotazioni = pickle.load(f)
            # Dopo aver caricato le prenotazioni, salva la lista nel file pickle


        # Funzione che popola le liste delle prenotazioni
    def update_ui_prenotazioni(self, evento):
        self.load_prenotazioni(evento)
        list_view_model = QStandardItemModel(self.list_view_prenotazioni)
        for prenotazioni in evento.lista_prenotazioni:
            item = QStandardItem()
            nome = f"{prenotazioni.nome}"  # il type ci restituisce il nome della classe
            cognome = f"{prenotazioni.cognome}"
            codice_fiscale = f"{prenotazioni.codice_fiscale}"
            testo = f"{nome} {cognome} {codice_fiscale}"
            item.setText(testo)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            list_view_model.appendRow(item)

        self.list_view_prenotazioni.setModel(list_view_model)


    def elimina_prenotazione(self):
        if self.list_view_prenotazioni.selectedIndexes():
            selected_index = self.list_view_prenotazioni.selectedIndexes()[0]
            row = selected_index.row()
            prenotazione_selezionata = self.controller.get_prenotazione_by_index(self.evento, row)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Sei sicuro di voler eliminare la prenotazione?")
            msg.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
            msg.setInformativeText("La decisione è irreversibile!")
            msg.setDetailedText("N.B. Verrà eliminata ogni informazione relativa alla prenotazione.")
            msg.setWindowTitle("Conferma eliminazione")
            msg.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)


            if msg.exec() == QMessageBox.Ok: #La funzione exec() blocca l'esecuzione del codice fino a quando l'utente non chiude la finestra di dialogo. Quando l'utente interagisce con la finestra di dialogo e preme un pulsante, exec() restituisce il valore corrispondente al pulsante premuto.

                self.controller.rimuovi_prenotazione(self.evento, prenotazione_selezionata)
                self.update_ui_prenotazioni(self.evento)
                self.vista_prenotazione.close()
                msg.close()

