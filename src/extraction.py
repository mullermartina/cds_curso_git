import pandas as pd

def load_data(): # funcao responsavel por fazer a leitura do nosso arquivo
    return pd.read_csv('data/processed/bikes_completed.csv')