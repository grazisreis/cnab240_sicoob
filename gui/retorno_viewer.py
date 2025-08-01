from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QMessageBox
from processor.retorno_reader import read_retorno_file

class RetornoViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.read_btn = QPushButton("Selecionar Arquivo de Retorno (.RET)")
        layout.addWidget(self.read_btn)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["Segmento", "Nosso Número", "Valor Pago", "Data Pagamento", "Ocorrência"])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.read_btn.clicked.connect(self.read_file)

    def read_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo de retorno", "", "Arquivos RET (*.RET *.txt)")
        if file_name:
            data = read_retorno_file(file_name)
            self.table.setRowCount(0)
            for item in data:
                row = self.table.rowCount()
                self.table.insertRow(row)
                self.table.setItem(row, 0, QTableWidgetItem(item["Segmento"]))
                self.table.setItem(row, 1, QTableWidgetItem(item["NossoNumero"]))
                self.table.setItem(row, 2, QTableWidgetItem(str(item["ValorPago"])))
                self.table.setItem(row, 3, QTableWidgetItem(item["DataPagamento"]))
                self.table.setItem(row, 4, QTableWidgetItem(item["DescricaoOcorrencia"]))
