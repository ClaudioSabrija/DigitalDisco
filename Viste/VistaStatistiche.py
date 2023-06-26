from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QWidget
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter


class VistaStatistiche(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Statistiche")
        self.setGeometry(100, 100, 800, 600)

        # Dati di esempio per il grafico
        self.dati_annuali = {
            'Biglietti venduti': [100, 200, 300, 400, 500],
            'Drink-Bottiglie': [50, 150, 250, 350, 450]
        }

        self.dati_mensili = {
            'Gennaio': [50, 100],
            'Febbraio': [75, 125],
            'Marzo': [100, 150],
            'Aprile': [125, 175],
            'Maggio': [150, 200]
        }

        # Creazione della casella combinata (combobox)
        self.combo_box = QComboBox()
        self.combo_box.addItem("Anno")
        self.combo_box.addItem("Mese")
        self.combo_box.currentIndexChanged.connect(self.update_chart)

        # Creazione dei grafici a istogramma
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Layout principale
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.combo_box)
        main_layout.addWidget(self.chart_view)

        # Widget principale
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Inizializzazione del grafico
        self.update_chart()

    def update_chart(self):
        chart = QChart()

        # Selezione dei dati da utilizzare
        if self.combo_box.currentIndex() == 0:  # Anno
            dati = self.dati_annuali
            categories = dati.keys()
        else:  # Mese
            dati = self.dati_mensili
            categories = dati.keys()

        for label, values in dati.items():
            bar_set = QBarSet(label)
            bar_set.append(values)
            series = QBarSeries()
            series.append(bar_set)
            chart.addSeries(series)

        # Impostazione delle categorie sull'asse X
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        for series in chart.series():
            chart.setAxisX(axis_x, series)

        # Aggiornamento del grafico
        self.chart_view.setChart(chart)