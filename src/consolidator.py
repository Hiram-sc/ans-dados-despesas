import csv
from pathlib import Path

def consolidar_arquivo(arquivos):
    pasta = Path("data")
    pasta.mkdir(exist_ok=True)
    saida = pasta / "consolidado_despesas.csv"

    with saida.open("w", encoding="utf-8") as csv_saida:
        csv_writer = csv.writer(csv_saida)
        csv_writer.writerow(["CNPJ", "RazaoSocial", "Trimestre", "Ano", "ValorDespesas"])

        for caminho in arquivos:
            if caminho.suffix.lower() != ".csv":
                continue

            with caminho.open(newline="", encoding="utf-8") as csv_entrada:
                dictreader = csv.DictReader(csv_entrada)

                for linha in dictreader:
                    csv_writer.writerow([
                        linha.get("CNPJ"),
                        linha.get("RazaoSocial") or linha.get("Razao Social"),
                        extrair_trimestre(caminho.name),
                        extrair_ano(caminho.name),
                        linha.get("ValorDespesas") or linha.get("Valor Despesas")
                    ])

    print(f"Arquivo CSV consolidado e criado com sucesso em {saida}")



def extrair_trimestre(nome_arquivo):
    nome = nome_arquivo.lower()
    if "1t" in nome:
        return "1"
    if "2t" in nome:
        return "2"
    if "3t" in nome:
        return "3"
    return ""

def extrair_ano(nome_arquivo):
    if "2025" in nome_arquivo:
        return "2025"
    return ""
