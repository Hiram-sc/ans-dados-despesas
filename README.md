# Visão Geral

Este projeto tem como base a API pública de Dados Abertos da ANS, sendo utilizada com o objetivo de identificar e baixar arquivos de Demonstrações Contábeis, com respectivos trimestres solicitados, extrair arquivos ZIP automaticamente, processar arquivos de Despesas com Eventos/Sinistros e, ao final, consolidar os dados em um único arquivo CSV. 

## Processamento de arquivos


### Download dos arquivos ZIP dos trimestres identificados

O módulo `downloader.py` é responsável por:

- acessar a API REST pública da ANS por meio de requisições HTTP;
- identificar e baixar os arquivos de Demonstrações Contábeis últimos 3 trimestres disponíveis;
- realizar o download automático dos arquivos ZIP de Demonstrações Contábeis;
- após o download, os arquivos ZIP são armazenados em `data/raw`.

Arquivo responsável:
- 'downloader.py'

---

### Extração dos arquivos

O módulo `extractor.py` é responsável por:

- percorrer os arquivos ZIP armazenados em `data/raw`;
- extrair automaticamente o conteúdo dos arquivos ZIP para `data/extracted`;
- realizar tratamento de erro para arquivos ZIP inválidos ou corrompidos.

Arquivo responsável:
- 'extractor.py'

---

### Identificação/verificação dos dados de Despesas (processamento ainda não é realizado)

- percorrer os arquivos ZIP armazenados em `data/extracted`;
- identificar automaticamente arquivos que contém dados de Despesas com Eventos/Sinistros;
- retornar a lista de arquivos identificados.

Arquivo responsável:
- 'processor.py'

---

### Consolidação dos dados em arquivo csv

- processar os arquivos de Despesas com Eventos/Sinistros
- consolidar os dados em um único arquivo CSV;
- colunas produzidas: 
    - CNPJ
    - RazaoSocial
    - Trimestre
    - Ano
    - ValorDespesas
- salvar o arquivo consolidado em `data/consolidado_despesas.csv`.

Arquivo responsável:
- consolidator.py

---

### Compatação do arquivo CSV consolidado

- receber o arquivo CSV gerado ao final
- compatar o arquivo CSV em formato ZIP
- gerar o arquivo final em `data/consolidado_despesas.zip`

Arquivo responsável:
- converter.py

---

### Trade-Off Técnico - Processamento de Arquivos

- arquivos processados em abordagem de processamento incremental;
- decisão tomada considerando o volume do arquivo e pensando em controle de gerenciamento e consumo de memória.