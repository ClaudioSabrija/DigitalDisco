from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
     QComboBox, QDateTimeEdit


class VistaInserisciEvento(QWidget):
    def __init__(self, parent=None):
        super(VistaInserisciEvento, self).__init__(parent)

        # Creazione dei widget
        label_top = QLabel("Inserisci i dati dell'evento:", self)
        label_nome = QLabel("NOME:", self)
        label_tipo = QLabel("TIPO:", self)
        label_data = QLabel("DATA:", self)
        label_prezzi = QLabel("Inserisci i prezzi dei servizi:", self)
        label_ingresso = QLabel("INGRESSO:", self)
        label_tavolo = QLabel("TAVOLO:", self)
        label_prive = QLabel("PRIVE:", self)

        line_edit_nome = QLineEdit(self)
        combo_box_tipo = QComboBox(self)
        date_edit_data = QDateTimeEdit(self)

        line_edit_ingresso = QLineEdit(self)
        line_edit_tavolo = QLineEdit(self)
        line_edit_prive = QLineEdit(self)

        button_conferma = QPushButton("Conferma", self)
        button_conferma.clicked.connect(self.add_evento)

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Inserisci Evento')
        self.setFixedSize(400, 600)  # Imposta la dimensione fissa della finestra di dialogo
        label_top.setFixedSize(300, 30)  # Imposta la dimensione fissa della label superiore
        label_prezzi.setFixedSize(300, 30)  # Imposta la dimensione fissa della label "Inserisci i prezzi dei servizi"

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(label_top)
        layout.addWidget(label_nome)
        layout.addWidget(line_edit_nome)
        layout.addWidget(label_tipo)
        layout.addWidget(combo_box_tipo)
        layout.addWidget(label_data)
        layout.addWidget(date_edit_data)
        layout.addWidget(label_prezzi)
        layout.addWidget(label_ingresso)
        layout.addWidget(line_edit_ingresso)
        layout.addWidget(label_tavolo)
        layout.addWidget(line_edit_tavolo)
        layout.addWidget(label_prive)
        layout.addWidget(line_edit_prive)
        layout.addWidget(button_conferma)

        self.setLayout(layout)

    def add_evento(self):
        nome = self.info["Nome*"].text()
        cognome = self.info["Cognome*"].text()
        data_nascita = self.info["Data di nascita (dd/mm/YYYY)*"].text()
        cf = self.info["Codice Fiscale*"].text()
        indirizzo = self.info["Indirizzo*"].text()
        telefono = self.info["Telefono*"].text()
        preferenze = self.preferenza.currentText()
        categoria_speciale = self.categorie_speciali.currentText()
        is_a_domicilio = False
        if self.domicilio.isChecked():
            is_a_domicilio = True

        ok = True

        if nome == "" or cognome == "" or data_nascita == "" or cf == "" or indirizzo == "" or telefono == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, completa tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
            ok = False

        if ok is True:
            try:
                data_inserita = datetime.strptime(self.info["Data di nascita (dd/mm/YYYY)*"].text(), '%d/%m/%Y')
            except:
                QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

            if ok is True and date.today().year - data_inserita.year < 0:
                QMessageBox.critical(self, 'Errore', 'La data inserita non è valida',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

            if ok is True and date.today().year - data_inserita.year < 18:
                QMessageBox.critical(self, 'Errore',
                                     'Per i minori di 18 anni non è prevista la possibilità di prenotarsi per la vaccinazione',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

            '''if ok is True and categoria_speciale == ' ' and date.today().year - data_inserita.year < 50:
                QMessageBox.critical(self, 'Errore', 'Attualmente le direttive nazionali non permettono la prenotazione a coloro che hanno '
                                                     'un\'età inferiore ai 50 anni e non rientrano in una delle categorie con priorità', QMessageBox.Ok, QMessageBox.Ok)
                ok = False'''

        if ok is True:
            if not bool(self.vista_inserisci_anamnesi.anamnesi):
                QMessageBox.critical(self, 'Errore', 'Non è stata compilato il questionario anamnestico!',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True and (self.consenso1.isChecked() is False or self.consenso2.isChecked() is False):
            ok = False
            QMessageBox.critical(self, 'Errore', 'Se non viene fornito il consenso non è possibile procedere '
                                                 'con la prenotazione', QMessageBox.Ok, QMessageBox.Ok)

        if ok is True:
            if self.vista_inserisci_anamnesi.anamnesi['Pfizer'] == 'Sì' and self.vista_inserisci_anamnesi.anamnesi[
                'Moderna'] == 'Sì' and self.vista_inserisci_anamnesi.anamnesi['Astrazeneca'] == "Sì":
                ok = False
                QMessageBox.critical(self, 'Attenzione', 'Ci dispiace ma al momento non sono disponibili'
                                                         ' vaccini che non le provichino reazioni allergiche. Non è possibile procedere con la prenotazione!',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False
            elif self.vista_inserisci_anamnesi.anamnesi['Contatto'] == 'Sì' or self.vista_inserisci_anamnesi.anamnesi[
                'Sintomi'] == 'Sì':
                ok = False
                QMessageBox.critical(self, 'Attenzione', 'Ci dispiace ma non è possibile prenotare '
                                                         'l\'appuntamento se si presentano sintomi ricondubili ad un\'infezione da Covid19 o se si è stati a contatto con persone positive.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True:
            if self.vista_inserisci_anamnesi.anamnesi['Positivo COVID-19'] == 'meno di 3 mesi':
                QMessageBox.critical(self, 'Attenzione', 'Ci dispiace ma non è possibile prenotare '
                                                         'l\'appuntamento se non è passato un periodo superiore ai 3 mesi dall\'infezione.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True:
            if self.vista_mostra_date.data_scelta == "" or self.vista_mostra_date.orario_selezionato == "":
                QMessageBox.critical(self, 'Errore', 'Non è stata scelta una data per l\'appuntamento!', QMessageBox.Ok,
                                     QMessageBox.Ok)
                ok = False

        if ok is True:
            cartella_paziente = CartellaPaziente(nome, cognome, data_nascita, cf, indirizzo, telefono,
                                                 categoria_speciale, preferenze, self.vista_inserisci_anamnesi.anamnesi)
            appuntamento_vaccino = AppuntamentoVaccino('Prima Dose', cartella_paziente,
                                                       self.vista_mostra_date.data_scelta,
                                                       self.vista_mostra_date.orario_selezionato, is_a_domicilio)

            if categoria_speciale == " ":
                if date.today() < date(2021, 3, 21):
                    if cartella_paziente.categoria != 'over 80' or cartella_paziente.categoria != 'categoria 70-79':
                        QMessageBox.critical(self, 'Errore',
                                             'Secondo il calendario regionale, non è ancora possibile prenotare la vaccinazione per la ' + cartella_paziente.categoria,
                                             QMessageBox.Ok,
                                             QMessageBox.Ok)
                        ok = False

                elif date.today() < date(2021, 4, 17):
                    if cartella_paziente.categoria != 'over 80' or cartella_paziente.categoria != 'categoria 70-79' or cartella_paziente.categoria != 'categoria 60-69':
                        QMessageBox.critical(self, 'Errore',
                                             'Secondo il calendario regionale, non è ancora possibile prenotare la vaccinazione per la ' + cartella_paziente.categoria,
                                             QMessageBox.Ok,
                                             QMessageBox.Ok)
                        ok = False

                elif date.today() < date(2021, 5, 15):
                    if cartella_paziente.categoria != 'over 80' or cartella_paziente.categoria != 'categoria 70-79' or cartella_paziente.categoria != 'categoria 60-69' or cartella_paziente.categoria != 'categoria 50-59':
                        QMessageBox.critical(self, 'Errore',
                                             'Secondo il calendario regionale, non è ancora possibile prenotare la vaccinazione per la ' + cartella_paziente.categoria,
                                             QMessageBox.Ok,
                                             QMessageBox.Ok)
                        ok = False

                elif date.today() < date(2021, 5, 19):
                    if cartella_paziente.categoria != 'over 80' or cartella_paziente.categoria != 'categoria 70-79' or cartella_paziente.categoria != 'categoria 60-69' or cartella_paziente.categoria != 'categoria 50-59' or cartella_paziente.categoria != 'categoria 40-49':
                        QMessageBox.critical(self, 'Errore',
                                             'Secondo il calendario regionale, non è ancora possibile prenotare la vaccinazione per la ' + cartella_paziente.categoria,
                                             QMessageBox.Ok,
                                             QMessageBox.Ok)
                        ok = False
                elif date.today() < date(2021, 6, 5):
                    if cartella_paziente.categoria == 'categoria 30-39' or cartella_paziente.categoria == 'under 30':
                        QMessageBox.critical(self, 'Errore',
                                             'Secondo il calendario regionale, non è ancora possibile prenotare la vaccinazione per la categoria del paziente',
                                             QMessageBox.Ok,
                                             QMessageBox.Ok)
                        ok = False

            if ok:
                if appuntamento_vaccino.vaccino is not None:
                    self.controller.aggiungi_appuntamento(appuntamento_vaccino)

                    if self.vista_inserisci_anamnesi.anamnesi['Positivo COVID-19'] != 'tra i 3 e i 6 mesi':
                        data_prima_dose = datetime.strptime(self.vista_mostra_date.data_scelta, '%d-%m-%Y')
                        if appuntamento_vaccino.vaccino == "Pfizer":
                            data_seconda_dose = str((data_prima_dose + timedelta(days=21)).strftime('%d-%m-%Y'))
                        elif appuntamento_vaccino.vaccino == "Moderna":
                            data_seconda_dose = str((data_prima_dose + timedelta(days=28)).strftime('%d-%m-%Y'))
                        elif appuntamento_vaccino.vaccino == "Astrazeneca":
                            data_seconda_dose = str((data_prima_dose + timedelta(days=60)).strftime('%d-%m-%Y'))

                        appuntamento_seconda_dose = AppuntamentoVaccino('Seconda Dose', cartella_paziente,
                                                                        data_seconda_dose,
                                                                        self.vista_mostra_date.orario_selezionato,
                                                                        is_a_domicilio)
                        self.controller.aggiungi_appuntamento(appuntamento_seconda_dose)
                        if not appuntamento_seconda_dose.vaccino == appuntamento_vaccino.vaccino:
                            QMessageBox.warning(self, 'Attenzione',
                                                'Le scorte al momento non garantiscono che al paziente venga somministrato lo stesso vaccino per entrambe le dosi. Vi invitiamo a modificare l\'appuntamento per la seconda dose dopo che il magazzino verrà rifornito.',
                                                QMessageBox.Ok, QMessageBox.Ok)
                        self.vista_riepilogo_2 = VistaAppuntamentoVaccino(appuntamento_seconda_dose)
                        self.vista_riepilogo_2.show()

                    self.vista_riepilogo = VistaAppuntamentoVaccino(appuntamento_vaccino)
                    self.vista_riepilogo.show()
                else:
                    QMessageBox.critical(self, 'Errore', 'Ci dispiace ma non è possibile prenotare '
                                                         'l\'appuntamento a causa di una mancanza di vaccini che possono essere somministrati al paziente.',
                                         QMessageBox.Ok, QMessageBox.Ok)
                self.close()


