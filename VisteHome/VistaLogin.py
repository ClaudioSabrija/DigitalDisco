from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QMessageBox, QLineEdit

from VisteHome.VistaHomeAmministratore import VistaHomeAmministratore
from VisteHome.VistaHomeBarman import VistaHomeBarman


class VistaLogin(QWidget):
    def __init__(self, parent = None):
        super(VistaLogin, self).__init__(parent)

        layout = QGridLayout()
        label1 = QLabel('Nome Utente:')
        self.user_name = QLineEdit()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.user_name, 0, 1)

        label2 = QLabel('Password:')
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.password, 1, 1)

        button_login = QPushButton('Accedi')
        button_login.clicked.connect(self.controllo_accesso)
        layout.addWidget(button_login, 2, 0, 2, 2, alignment=Qt.AlignBottom)


        self.setLayout(layout)
        self.setWindowTitle('Login')

        self.setFont(QFont('Arial Nova Light', 14))
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.resize(650, 170)
        self.move(600, 350)



    def controllo_accesso(self):
        if self.user_name.text() == 'amministratore' and self.password.text() == 'password':
            self.vista_home = VistaHomeAmministratore()
            self.vista_home.show()
            self.close()
        elif self.user_name.text() == 'barman' and self.password.text() == 'password':
            self.vista_home_barman = VistaHomeBarman()
            self.vista_home_barman.show()
            self.close()
        else:
            QMessageBox.critical(self, 'Accesso Negato', 'Le credenziali inserite sono errate', QMessageBox.Ok, QMessageBox.Ok)

