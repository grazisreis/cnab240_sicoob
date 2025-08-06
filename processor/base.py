import os
from datetime import datetime

SEQUENCE_FILE = 'last_sequence.txt'

class BaseCNAB240:
    def __init__(self):
        # Dados padrão da empresa (editáveis)
        self.codigo_banco = '756'
        self.tipo_inscricao = '2'
        self.cnpj = '15251164000169'
        self.codigo_convenio = '123456789123456789'
        self.agencia = '3292'
        self.dv_agencia = '1'
        self.conta = '19777'
        self.dv_conta = '7'
        self.dv = self.dv_conta
        self.nome_empresa = 'PARISH E ZENANDRO ADVOGADOS'
        self.nome_banco = 'SICOOB'

        self.numero_arquivo = self.get_next_sequence_number()
        self.data_hoje = datetime.now().strftime("%d%m%Y")
        self.hora_agora = datetime.now().strftime("%H%M%S")

    def get_next_sequence_number(self):
        try:
            if os.path.exists(SEQUENCE_FILE):
                with open(SEQUENCE_FILE, 'r') as f:
                    last_number = int(f.read().strip())
            else:
                last_number = 0
            next_number = last_number + 1
            with open(SEQUENCE_FILE, 'w') as f:
                f.write(str(next_number))
            return next_number
        except:
            return int(datetime.now().strftime("%Y%m%d%H%M"))

    def format_num(self, valor, tamanho):
        return str(valor).replace('.', '').replace(',', '').zfill(tamanho)
    
    def format_text(self, texto, tamanho):
        return str(texto)[:tamanho].ljust(tamanho, " ")

    def header_arquivo(self):
        return (
            self.codigo_banco +
            "0000" +
            "0" +
            " " * 9 +
            self.tipo_inscricao +
            self.format_num(self.cnpj, 14) +
            self.format_text(self.codigo_convenio, 20) +
            self.format_num(self.agencia,5) +
            self.dv_agencia +
            self.format_num(self.conta, 12) +
            self.dv_conta[0] +
            self.dv_conta[1] +
            self.format_text(self.nome_empresa,30) +
            self.format_text(self.nome_banco,30) +
            " " * 10 +
            "1" +
            self.data_hoje +
            self.hora_agora +
            str(self.numero_arquivo).zfill(6) +
            "087" +
            "00000" +
            " " * 20 +
            " " * 20 +
            " " * 29 +
            "\r\n"
        )

    def trailer_arquivo(self, lotes, registros):
        return (
            self.codigo_banco +
            "9999" +
            "9" +
            " " * 9 +
            str(len(lotes)).zfill(6) +
            str(len(registros) + 1).zfill(6) +
            str(len(lotes)).zfill(6) +
            " " * 205 +
            "\r\n"
        )
