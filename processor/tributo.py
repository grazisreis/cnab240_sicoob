from .base import BaseCNAB240

class PagamentoTributoCNAB(BaseCNAB240):
    def gerar_lote(self, dados):
        registros = []

        header_lote = (
            self.codigo_banco +
            "0001" +
            "1" +
            "C" +
            "22" +  # G025 Pagamento de Tributos
            " " * 100 +
            "\r\n"
        )
        registros.append(header_lote)

        for idx, linha in enumerate(dados, start=1):
            valor = self.format_num(linha.get("Valor",0),15)
            data_pagto = "29072025"
            codigo_barras = self.format_num(linha.get("CodigoBarrasTributo",""),44)

            registro_o = (
                self.codigo_banco +
                "0001" +
                "3" +
                str(idx).zfill(5) +
                "O" +
                codigo_barras +
                valor +
                data_pagto +
                " " * 130 +
                "\r\n"
            )
            registros.append(registro_o)

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
