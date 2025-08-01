def write_rem_file(file_path, registros):
    """
    Salva lista de linhas CNAB 240 em arquivo .REM
    """
    with open(file_path, "w", encoding="utf-8") as f:
        for linha in registros:
            f.write(linha)
