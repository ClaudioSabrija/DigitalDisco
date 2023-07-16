import sys
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from VisteHome.VistaLogin import VistaLogin

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    splash = QSplashScreen(QPixmap('Dati/DigitalDisco.png').scaled(700, 500))
    splash.show()
    QTimer.singleShot(1000, splash.close)

    time.sleep(1)

    vista_login = VistaLogin()
    vista_login.show()
    sys.exit(app.exec())


