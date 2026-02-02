import requests
from pathlib import Path

url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis"

def ultimos_trimestres():
    return [
        ("2025", "1T2025.zip"),
        ("2025", "2T2025.zip"),
        ("2025", "3T2025.zip")
    ]

def baixar_zip(ano, nome_arquivo):
    url_completa = f"{url}/{ano}/{nome_arquivo}"

    print(f"Baixando: {url_completa}")
    response = requests.get(url_completa)

    if response.status_code == 200:
        pasta_origem = Path("data/raw")
        pasta_origem.mkdir(parents=True, exist_ok=True)

        arquivo_path = pasta_origem / nome_arquivo
        with open(arquivo_path, "wb") as f:
            f.write(response.content)
        print(f"{nome_arquivo} baixado com sucesso")
    else:
        print(f"Erro ao baixar {nome_arquivo}: {response.status_code}")