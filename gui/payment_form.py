from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox
)
from processor.generator import generate_cnab240
from processor.file_writer import write_rem_file

class PaymentForm(QWidget):
    def __init__(self):
        super().__init__()
        self.pagamentos = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Tipo de Pagamento
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Tipo de Pagamento:"))
        self.payment_type = QComboBox()
        self.payment_type.addItems(["TRANSFERÊNCIA", "TED", "PIX", "PAGAMENTO DE TÍTULOS", "PAGAMENTO DE TRIBUTOS"])
        type_layout.addWidget(self.payment_type)
        layout.addLayout(type_layout)

        # Campos dinâmicos (simplificados)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nome do Favorecido")
        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("Valor (ex: 1000,50)")
        layout.addWidget(self.name_input)
        layout.addWidget(self.value_input)

        # Botões
        button_layout = QHBoxLayout()
        self.add_btn = QPushButton("Adicionar Pagamento")
        self.gen_btn = QPushButton("Gerar Arquivo .REM")
        self.ext_btn = QPushButton("Extrair Dados de Planilha")
        self.edit_btn = QPushButton("Editar Linha")
        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.gen_btn)
        button_layout.addWidget(self.ext_btn)
        layout.addLayout(button_layout)

        # Tabela de pagamentos
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Tipo", "Favorecido", "Valor"])
        layout.addWidget(self.table)

        self.setLayout(layout)

        # Conexões
        self.add_btn.clicked.connect(self.add_payment)
        self.gen_btn.clicked.connect(self.generate_file)

    def add_payment(self):
        tipo = self.payment_type.currentText()
        nome = self.name_input.text()
        valor = self.value_input.text().replace(",", ".")

        if not nome or not valor:
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")
            return

        self.pagamentos.append({"TipoPagamento": tipo, "NomeFavorecido": nome, "Valor": float(valor)})

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(tipo))
        self.table.setItem(row, 1, QTableWidgetItem(nome))
        self.table.setItem(row, 2, QTableWidgetItem(valor))

        self.name_input.clear()
        self.value_input.clear()

    def generate_file(self):
        if not self.pagamentos:
            QMessageBox.warning(self, "Aviso", "Nenhum pagamento adicionado!")
            return

        cnab_data = generate_cnab240(self.pagamentos)
        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo .REM", "", "Arquivos REM (*.REM)")
        
        if file_path:
            if not file_path.upper().endswith(".REM"):
                file_path += ".REM"
            write_rem_file(file_path, cnab_data)
            QMessageBox.information(self, "Sucesso", f"Arquivo gerado em:\n{file_path}")
