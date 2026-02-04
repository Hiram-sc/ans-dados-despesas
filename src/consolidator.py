import csv
from pathlib import Path

def consolidar_arquivo(arquivos):
    pasta = Path("data")
    pasta.mkdir(exist_ok=True)
    saida = pasta / "consolidado_despesas.csv"

    with saida.open("w", newline="", encoding="utf-8") as csv_saida:
        csv_writer = csv.writer(csv_saida)
        csv_writer.writerow(["CNPJ", "RazaoSocial", "Trimestre", "Ano", "ValorDespesas"])

        for caminho in arquivos:
            if caminho.suffix.lower() != ".csv":
                continue

            with caminho.open(newline="", encoding="utf-8") as csv_entrada:
                dictreader = csv.DictReader(csv_entrada, delimiter=";")

                for linha in dictreader:
                    linha_normalizada = {
                        k.lower(): v for k, v in linha.items()
                    }

                    reg_ans = linha_normalizada.get("reg_ans")
                    valor_despesas = linha_normalizada.get("vl_saldo_final")

                    if not reg_ans or not valor_despesas:
                        continue

                    csv_writer.writerow([
                        reg_ans,
                        "",
                        extrair_trimestre(caminho.name),
                        extrair_ano(caminho.name),
                        valor_despesas
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
