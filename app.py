import pandas as pd
import numpy as np
import streamlit as st

def load_data(): # funcao responsavel por fazer a leitura do nosso arquivo
    return pd.read_csv('data/processed/bikes_completed.csv')

df = load_data()

st.dataframe(df)