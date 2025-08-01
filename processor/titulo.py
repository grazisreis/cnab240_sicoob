from .base import BaseCNAB240

class PagamentoTituloCNAB(BaseCNAB240):
    def gerar_lote(self, dados):
        registros = []

        header_lote = (
            self.codigo_banco +
            "0001" +
            "1" +
            "C" +
            "20" +  # Pagamento de Títulos como fornecedor
            " " * 100 +
            "\r\n"
        )
        registros.append(header_lote)

        for idx, linha in enumerate(dados, start=1):
            codigo_barras = self.format_num(linha.get("CodigoBarras",""),44)
            nome_cedente = self.format_text(linha.get("NomeFavorecido",""),30)
            valor = self.format_num(linha.get("Valor",0),15)
            data_pagto = "29072025"

            registro_j = (
                self.codigo_banco +
                "0001" +
                "3" +
                str(idx).zfill(5) +
                "J" +
                codigo_barras +
                valor +
                data_pagto +
                nome_cedente +
                " " * 110 +
                "\r\n"
            )
            registros.append(registro_j)

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
