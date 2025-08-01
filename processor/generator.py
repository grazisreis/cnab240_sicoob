from .transferencia import TransferenciaCNAB
from .titulo import PagamentoTituloCNAB
from .tributo import PagamentoTributoCNAB

def generate_cnab240(pagamentos):
    """
    Recebe lista de dicionários com pagamentos e gera registros CNAB 240
    """
    registros = []
    lotes = []

    # Header do arquivo
    base = TransferenciaCNAB()
    registros.append(base.header_arquivo())

    # Agrupa por tipo de pagamento
    tipos = ["TRANSFERENCIA", "TED", "PIX", "TITULO", "TRIBUTO"]
    for tipo in tipos:
        grupo = [p for p in pagamentos if p["TipoPagamento"].upper() == tipo]
        if not grupo:
            continue

        if tipo in ["TRANSFERENCIA", "TED", "PIX"]:
            lote = TransferenciaCNAB().gerar_lote(grupo)
        elif tipo in ["TITULO"]:
            lote = PagamentoTituloCNAB().gerar_lote(grupo)
        elif tipo in ["TRIBUTO"]:
            lote = PagamentoTributoCNAB().gerar_lote(grupo)
        else:
            continue

        registros.extend(lote)
        lotes.append(lote)

    # Trailer do arquivo
    registros.append(base.trailer_arquivo(lotes, registros))
    return registros
