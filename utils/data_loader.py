# --- INÍCIO DA MODIFICAÇÃO ---
import pandas as pd
import streamlit as st

@st.cache_data 
def carregar_dados():
    """
    Carrega os dados do dataset da Netflix, realiza uma limpeza básica
    e retorna um DataFrame do Pandas.
    """
    caminho_arquivo = './dataset/netflix_titles_CLEANED.csv'
    
    df = pd.read_csv(caminho_arquivo)
    
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # --- CORREÇÃO APLICADA AQUI ---
    # Normaliza a data para meia-noite, removendo a precisão de tempo que causa o erro do Arrow.
    df['date_added'] = df['date_added'].dt.normalize()
    
    df.dropna(subset=['date_added'], inplace=True)

    df['year_added'] = df['date_added'].dt.year
    df['year_added'] = df['year_added'].astype(int)

    return df
# --- FIM DA MODIFICAÇÃO ---