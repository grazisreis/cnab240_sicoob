from .base import BaseCNAB240

class TransferenciaCNAB(BaseCNAB240):
    def gerar_lote(self, dados):
        registros = []

        header_lote = (
            self.codigo_banco +
            "0001" +
            "1" +
            "C" +
            "20" +  # G025 Pagamento Fornecedor
            " " * 100 +
            "\r\n"
        )
        registros.append(header_lote)

        for idx, linha in enumerate(dados, start=1):
            nome = self.format_text(linha.get("NomeFavorecido",""),30)
            valor = self.format_num(linha.get("Valor",0),15)
            data_pagto = "29072025"  # Pode ser parametrizado
            registro = (
                self.codigo_banco +
                "0001" +
                "3" +
                str(idx).zfill(5) +
                "A" +
                nome +
                valor +
                data_pagto +
                " " * 150 +
                "\r\n"
            )
            registros.append(registro)

        trailer_lote = (
            self.codigo_banco +
            "0001" +
            "5" +
            str(len(registros)+2).zfill(6) +
            " " * 225 +
            "\r\n"
        )
        registros.append(trailer_lote)
        return registros
