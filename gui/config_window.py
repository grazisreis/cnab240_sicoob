from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QLineEdit, QPushButton, QMessageBox, QFormLayout)
from PyQt5.QtCore import Qt
import json
import os

CONFIG_FILE = "config.json"

class ConfigWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configurações da Empresa")
        self.setGeometry(200, 200, 500, 400)
        
        # Valores padrão
        self.default_values = {
            'codigo_banco': '756',
            'tipo_inscricao': '2',
            'cnpj': '15251164000169',
            'codigo_convenio': '123456789123456789',
            'agencia': '3292',
            'dv_agencia': '1',
            'conta': '19777',
            'dv_conta': '12',
            'nome_empresa': 'PARISH E ZENANDRO ADVOGADOS',
            'nome_banco': 'SICOOB'
        }
        
        self.init_ui()
        self.load_config()

    def init_ui(self):
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        # Campos de configuração
        self.fields = {}
        
        # Adicionando campos com labels descritivas
        self.fields['codigo_banco'] = self.create_field("Código do Banco", form_layout)
        self.fields['tipo_inscricao'] = self.create_field("Tipo de Inscrição (1-CPF/2-CNPJ)", form_layout)
        self.fields['cnpj'] = self.create_field("CNPJ da Empresa", form_layout)
        self.fields['codigo_convenio'] = self.create_field("Código do Convênio", form_layout)
        self.fields['agencia'] = self.create_field("Agência", form_layout)
        self.fields['dv_agencia'] = self.create_field("Dígito Verificador da Agência", form_layout)
        self.fields['conta'] = self.create_field("Número da Conta", form_layout)
        self.fields['dv_conta'] = self.create_field("Dígito Verificador da Conta", form_layout)
        self.fields['nome_empresa'] = self.create_field("Nome da Empresa", form_layout)
        self.fields['nome_banco'] = self.create_field("Nome do Banco", form_layout)
        
        main_layout.addLayout(form_layout)
        
        # Botões
        btn_layout = QHBoxLayout()
        
        self.save_btn = QPushButton("Salvar")
        self.save_btn.clicked.connect(self.save_config)
        btn_layout.addWidget(self.save_btn)
        
        self.reset_btn = QPushButton("Redefinir Padrões")
        self.reset_btn.clicked.connect(self.reset_to_default)
        btn_layout.addWidget(self.reset_btn)
        
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

    def create_field(self, label, layout):
        """Cria um campo de entrada com label e adiciona ao layout"""
        field = QLineEdit()
        layout.addRow(QLabel(label), field)
        return field

    def load_config(self):
        """Carrega configurações do arquivo ou usa os padrões"""
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    data = json.load(f)
                    for key, field in self.fields.items():
                        field.setText(data.get(key, self.default_values.get(key, '')))
            except Exception as e:
                QMessageBox.warning(self, "Erro", f"Erro ao ler configurações:\n{str(e)}")
                self.reset_to_default()
        else:
            self.reset_to_default()

    def save_config(self):
        """Salva as configurações no arquivo"""
        data = {key: field.text() for key, field in self.fields.items()}
        
        # Validação básica
        if not all(data.values()):
            QMessageBox.warning(self, "Aviso", "Todos os campos devem ser preenchidos!")
            return
            
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(data, f, indent=4)
            QMessageBox.information(self, "Sucesso", "Configurações salvas com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao salvar:\n{str(e)}")

    def reset_to_default(self):
        """Redefine todos os campos para os valores padrão"""
        for key, field in self.fields.items():
            field.setText(self.default_values.get(key, ''))
        
    def get_config(self):
        """Retorna as configurações atuais como dicionário"""
        return {key: field.text() for key, field in self.fields.items()}