import os
import json
import requests

class CryptoDataPipeline:
    """
    Classe responsável por buscar dados da API CoinGecko
    e salvá-los em um arquivo JSON.
    """
    
    def __init__(self, url, output_filename="dados_brutos.json"):
        self.url = url
        self.output_filename = output_filename
        self.dados_brutos = None
    
    def fetch_data(self):
        """Faz a requisição à API e armazena os dados na variável de classe."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Levanta exceções para códigos de erro HTTP
            self.dados_brutos = response.json()
            print("Dados buscados com sucesso!")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API: {e}")
            raise
    
    def save_data_to_file(self):
        """Salva os dados coletados em um arquivo JSON."""
        if self.dados_brutos is None:
            raise ValueError("Nenhum dado foi buscado. Execute 'fetch_data' primeiro.")
        
        caminho_arquivo = os.path.join(os.getcwd(), self.output_filename)
        
        try:
            with open(caminho_arquivo, 'w') as arquivo:
                json.dump(self.dados_brutos, arquivo, indent=4)
            print(f"Dados salvos com sucesso em: {caminho_arquivo}")
        except IOError as e:
            print(f"Erro ao salvar os dados: {e}")
            raise


# Script principal
if __name__ == "__main__":
    # URL da API
    API_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
    
    # Inicializa o pipeline
    pipeline = CryptoDataPipeline(url=API_URL)
    
    # Busca os dados e salva no arquivo
    pipeline.fetch_data()
    pipeline.save_data_to_file()
