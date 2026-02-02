# Visão Geral

Este projeto tem como base a API pública de Dados Abertos da ANS, sendo utilizada com o objetivo de identificar e baixar arquivos de Demonstração Contábeis, com respectivos trimestres solicitados, extrair arquivos ZIP automaticamente, processar arquivos de Despesas com Eventos/Sinistros e, ao final, consolidar os dados em um único arquivo CSV. 

## Processamento de arquivos

Download dos arquivos ZIP dos trimestres identificados
O processo passa por requisição da url
Arquivo responsável:
- 'downloader.py'


Extração dos arquivos

O processo de extrair os arquivos se passa por data/raw como origem de arquivos e data/extracted como destino de arquivos
Arquivo responsável:
- 'extractor.py'


Identificação/verificação dos dados de Despesas (processamento ainda não é realizado)
Arquivo responsável:
- 'processor.py'

Processamento e consolidação dos dados em arquivo csv
Arquivo responsável:
- consolidator.py