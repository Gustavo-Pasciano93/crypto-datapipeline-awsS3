# Crypto Data Pipeline

Este projeto implementa um pipeline de dados para capturar, processar e gerar relatórios sobre o preço das criptomoedas.

## Funcionalidades

1. **Busca de Dados**: Coleta dados sobre criptomoedas de uma API pública (CoinGecko).
2. **Processamento de Dados**: Processa e limpa os dados, removendo colunas irrelevantes e formatando datas.
3. **Geração de Relatórios**: Cria gráficos e gera relatórios PDF com as estatísticas sobre os preços das criptomoedas.

## Dependências

- `requests`
- `pandas`
- `matplotlib`
- `reportlab`
- `boto3` (para integração com S3)

## Como Usar

1. **Instalar as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Buscar os dados da API**:

    Execute o script `scripts/fetch_data.py` para buscar os dados das criptomoedas.

    ```bash
    python scripts/fetch_data.py
    ```

3. **Processar os dados**:

    Execute o script `scripts/process_data.py` para processar os dados brutos.

    ```bash
    python scripts/process_data.py
    ```

4. **Gerar Relatório**:

    Execute o script `scripts/generate_report.py` para gerar um relatório com o gráfico e as métricas.

    ```bash
    python scripts/generate_report.py
    ```

## Deploy na AWS S3

- Os dados são carregados no S3 usando o AWS CLI.
- Relatórios finais são gerados e enviados para o S3.
