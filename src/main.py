from downloader import ultimos_trimestres, baixar_zip
from extractor import extrair_zips
from processor import encontrar_arquivos_despesas
from consolidator import consolidar_arquivo

def main():

    print ("Iniciando Etapa 1 - Integração com API da ANS")

    ultimos = ultimos_trimestres()
    print("Identificando os últimos 3 trimestres...", ultimos)

    for ano, arquivo in ultimos_trimestres():
        baixar_zip(ano, arquivo)

    print("Extraindo arquivos ZIP...")
    extrair_zips()
    
    print("Processando arquivos de despesas...")
    arquivos_despesas = encontrar_arquivos_despesas()

    print("Consolidando dados em um CSV...")
    consolidar_arquivo(arquivos_despesas)

    print("Etapa 1 finalizada com sucesso!")

if __name__ == "__main__":
    main()