import streamlit as st

st.set_page_config(
    page_title="Home | Dashboard Netflix",
    page_icon="🏠",
    layout="wide"
)

st.title("Dashboard de Análise de Títulos da Netflix")

st.sidebar.success("Navegue pelas páginas no menu acima.")

st.markdown("---")

st.markdown(
    """
    ### 🎯 Objetivo do Dashboard
    Este dashboard foi desenvolvido para explorar visualmente o catálogo de filmes e séries da Netflix,
    utilizando um conjunto de dados público. O objetivo é facilitar a descoberta de
    padrões, tendências e insights sobre o conteúdo da plataforma de forma interativa.

    ---

    ### 🗺️ Como Navegar
    Use o menu na barra lateral à esquerda para navegar entre as diferentes seções de análise:
    - **🏠 Home:** Esta página inicial, com a documentação do projeto.
    - **🎲 Dados:** Permite a visualização do conjunto de dados completo e suas estatísticas.
    - **📊 Gráficos:** A seção principal, onde você pode interagir com os filtros e visualizar os gráficos.

    ---

    ### ⚙️ Como Usar os Filtros
    Na página de **Gráficos**, você encontrará filtros interativos na barra lateral. Eles permitem segmentar os dados para uma análise mais específica:
    - **Tipo de Título:** Escolha entre "Filme", "Série de TV" ou ambos.
    - **País de Produção:** Selecione um ou mais países para analisar suas produções.
    - **Ano de Lançamento:** Defina um intervalo de anos para focar em um período específico.

    Qualquer alteração nos filtros atualizará todos os gráficos da página instantaneamente.

    ---

    ### 📊 Gráficos Disponíveis
    A página de gráficos contém as seguintes visualizações:
    1.  **Relação entre Ano e Duração (Interativo):** Veja se os filmes estão ficando mais longos.
    2.  **Top 10 Países Produtores:** Um gráfico de barras com os países que mais produzem conteúdo.
    3.  **Proporção de Filmes vs. Séries:** Um gráfico de pizza mostrando a distribuição do catálogo.
    4.  **Top 10 Gêneros:** As categorias mais populares na plataforma.
    5.  **Duração por Classificação Indicativa:** Um boxplot para analisar a duração dos títulos por sua classificação.
    6.  **Títulos Adicionados por Ano (Interativo):** Um gráfico de linha com um seletor de intervalo para explorar o crescimento do catálogo.

    """
)

st.markdown("---")
st.info("Este projeto é um exemplo de como construir um dashboard interativo com Streamlit, Python, Pandas e Plotly.")
