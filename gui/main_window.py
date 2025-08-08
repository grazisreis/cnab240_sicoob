from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QTabWidget
)
from PyQt5.QtGui import QIcon
import os

from gui.payment_form import PaymentForm
from gui.retorno_viewer import RetornoViewer
from gui.config_window import ConfigWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CNAB 240 Sicoob – Pagamentos e Retornos")
        self.setGeometry(100, 100, 900, 600)

        # Ícone
        icon_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'icon.ico')
        self.setWindowIcon(QIcon(icon_path))

        self.init_ui()

    def init_ui(self):
        tabs = QTabWidget()

        # Aba de Pagamentos
        self.payment_tab = PaymentForm()
        tabs.addTab(self.payment_tab, "Gerar .REM")

        # Aba de Retornos
        self.retorno_tab = RetornoViewer()
        tabs.addTab(self.retorno_tab, "Ler .RET")

        # Aba de Configuração
        self.config_tab = ConfigWindow()
        tabs.addTab(self.config_tab, "Configuração")

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
