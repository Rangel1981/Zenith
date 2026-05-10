import json
from pathlib import Path

class RepositorioJSON:
    def __init__(self, nome_arquivo="gastos.json"):
        self.pasta_data = Path("data")
        self.caminho_arquivo = self.pasta_data / nome_arquivo
        self.pasta_data.mkdir(parents=True, exist_ok=True)

    def salvar(self, lista_de_gastos):
        with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            # Transformamos objetos em dicionários para o JSON entender
            dados = [vars(g) for g in lista_de_gastos]
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def carregar(self):
        if not self.caminho_arquivo.exists():
            return []
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)