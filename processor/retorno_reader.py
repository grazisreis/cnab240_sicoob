OCORRENCIAS = {
    "00": "Pagamento efetuado com sucesso",
    "01": "Insuficiência de fundos",
    "02": "Conta inexistente",
    "03": "Dados inválidos",
    "09": "Pagamento rejeitado"
}

def read_retorno_file(file_path):
    """
    Lê arquivo de retorno CNAB 240 e retorna lista de dicts com tradução
    """
    resultados = []
    with open(file_path, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.rstrip("\r\n")
            if len(linha) < 240:
                continue
            tipo_registro = linha[7]
            if tipo_registro == "3":
                segmento = linha[13]
                nosso_numero = linha[37:57].strip()
                valor_pago = float(linha[119:134]) / 100
                data_pagto = linha[93:101]
                cod_ocorrencia = linha[230:232]  # Exemplo de posição

                resultados.append({
                    "Segmento": segmento,
                    "NossoNumero": nosso_numero,
                    "ValorPago": valor_pago,
                    "DataPagamento": data_pagto,
                    "CodigoOcorrencia": cod_ocorrencia,
                    "DescricaoOcorrencia": OCORRENCIAS.get(cod_ocorrencia, "Desconhecida")
                })
    return resultados
