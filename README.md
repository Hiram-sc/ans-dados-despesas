# Visão Geral

Este projeto tem como base a API pública de Dados Abertos da ANS, sendo utilizada com o objetivo de identificar e baixar arquivos de Demonstração Contábeis, com respectivos trimestres solicitados, extrair arquivos ZIP automaticamente, processar arquivos de Despesas com Eventos/Sinistros e, ao final, consolidar os dados em um único arquivo CSV. 

## Processamento de arquivos

### Download dos arquivos ZIP dos trimestres identificados

O módulo `downloader.py` é responsável por:

- acessar a API REST pública da ANS via url;
- identificar e baixar os arquivos de Demonstrações Contábeis últimos 3 trimestres disponíveis;
- realizar o download automático dos arquivos ZIP de Demonstrações Contábeis;
- após o download, os arquivos ZIP são armazenados em `data/raw`.

Arquivo responsável:
- 'downloader.py'


### Extração dos arquivos

O módulo `extractor.py` é responsável por:

- realizar a extração dos arquivos armazenados em `data/raw` para `data/extracted`
- O 
Arquivo responsável:
- 'extractor.py'


Identificação/verificação dos dados de Despesas (processamento ainda não é realizado)
Arquivo responsável:
- 'processor.py'

Processamento e consolidação dos dados em arquivo csv
Arquivo responsável:
- consolidator.py