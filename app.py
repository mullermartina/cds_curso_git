import streamlit as st
from src.extraction import load_data

st.set_page_config(layout = 'wide')

def main():
    df_raw = load_data()

    st.dataframe(df)

if __name__ == 'main': # "se esse arq foi executado e for o ppal, vamos fazer o carregamento dos dados"
    main()