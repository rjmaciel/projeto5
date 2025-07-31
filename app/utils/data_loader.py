import os

def _ler_csv_blob(nome_arquivo):
    # Em vez de usar o Azure, simplesmente leia um arquivo local
    caminho_arquivo = os.path.join(os.path.dirname(__file__), nome_arquivo)

    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo {nome_arquivo} não foi encontrado.")

    with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
        import csv
        reader = csv.DictReader(file)
        return [row for row in reader]

def carregar_produtos():
    return _ler_csv_blob('produtos.csv')

def carregar_supermercados():
    return _ler_csv_blob('supermercados.csv')
