import zipfile
from pathlib import Path

def extrair_zips():
    pasta_origem = Path("data/raw")
    pasta_destino = Path("data/extracted")
    pasta_destino.mkdir(parents=True, exist_ok=True)

    for arquivo in pasta_origem.iterdir():
        if arquivo.suffix == ".zip":
            try:
                with zipfile.ZipFile(arquivo, 'r') as arquivo_zip:
                    arquivo_zip.extractall(pasta_destino)
                print(f"{arquivo.name} extraido para {pasta_destino}")
            except zipfile.BadZipFile:
                print(f"{arquivo.name} não é ZIP válido ou está corrompido")                