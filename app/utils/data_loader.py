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
    try:
        return _ler_csv_blob('produtos.csv')
    except FileNotFoundError:
        print("produtos.csv não encontrado, carregando lista vazia")
        return []


def carregar_supermercados():
    try:
        return _ler_csv_blob('supermercados.csv')
    except FileNotFoundError:
        print("supermercados.csv não encontrado, carregando lista vazia")
        return []

