import streamlit as st
from utils.data_loader import carregar_dados

st.set_page_config(
    page_title="Conjunto de Dados", 
    page_icon="🎲",
    layout="wide"
)

st.title("Visualização do Conjunto de Dados")
st.markdown("---")

df = carregar_dados()

st.markdown("### Tabela de Dados Brutos")
st.dataframe(df)

st.markdown("---")

st.markdown("### Estatísticas Descritivas")
st.write("Abaixo estão as estatísticas descritivas para as colunas numéricas do dataset:")
st.write(df.describe())

st.markdown("---")

with st.expander("📖 Dicionário de Dados (Descrição das Colunas)"):
    st.markdown("""
    - **show_id**: Identificador único para cada título.
    - **type**: O tipo do título (Filme ou Série de TV).
    - **title**: O nome do título.
    - **director**: O(s) diretor(es) do título.
    - **cast**: O elenco principal.
    - **country**: O país ou países de produção.
    - **date_added**: A data em que o título foi adicionado à Netflix.
    - **release_year**: O ano em que o título foi lançado originalmente.
    - **rating**: A classificação indicativa (ex: TV-MA, PG-13).
    - **duration**: A duração do título (em minutos para filmes, em temporadas para séries).
    - **listed_in**: As categorias ou gêneros em que o título está listado.
    - **description**: Uma breve sinopse do título.
    - **year_added**: O ano em que o título foi adicionado (coluna extraída de 'date_added').
    """)
