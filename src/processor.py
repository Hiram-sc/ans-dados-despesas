from pathlib import Path

palavras_chave = ["despesa", "despesas", "eventos", "sinistros"]
extensoes = (".csv", ".txt", ".xlsx")

def encontrar_arquivos_despesas(pasta_base="data/extracted"):
    arquivos_despesas = []

    for caminho in Path(pasta_base).rglob("*"):
        if not caminho.is_file():
            continue
            
        nome = caminho.name.upper()

        if caminho.suffix in extensoes:
            if any(palavra.upper() in nome for palavra in palavras_chave):
                arquivos_despesas.append(caminho)

    return arquivos_despesas

if __name__ == "__main__":
    arquivos = encontrar_arquivos_despesas()
    for a in arquivos:
        print(a)