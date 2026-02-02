import zipfile
from pathlib import Path

def zipar_arquivo_csv(arquivo_csv, arquivo_zip):
    arquivo_csv = Path(arquivo_csv)
    arquivo_zip = Path(arquivo_zip)

    with zipfile.ZipFile(arquivo_zip, "w", zipfile.ZIP_DEFLATED) as zip:
        zip.write(arquivo_csv, arcname=arquivo_csv.name) 

    print(f"{arquivo_csv} convertido para {arquivo_zip} com sucesso!")