# --- INÍCIO DA MODIFICAÇÃO ---
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import carregar_dados

st.set_page_config(
    page_title="Gráficos", 
    page_icon="📊",
    layout="wide"
)

st.title("📊 Análise Gráfica do Catálogo da Netflix")
st.markdown("---")

df = carregar_dados()

st.sidebar.header("Filtros")

tipos_selecionados = st.sidebar.multiselect(
    "Selecione o Tipo",
    options=sorted(df['type'].unique()),
    default=sorted(df['type'].unique()) 
)

paises_disponiveis = df['countries'].dropna().str.split(', ').explode().unique()
paises_selecionados = st.sidebar.multiselect(
    "Selecione o País",
    options=sorted(paises_disponiveis),
    default=None 
)

min_ano, max_ano = int(df['release_year'].min()), int(df['release_year'].max())
anos_selecionados = st.sidebar.slider(
    "Selecione o Intervalo de Anos de Lançamento",
    min_value=min_ano,
    max_value=max_ano,
    value=(min_ano, max_ano)
)

df_filtrado = df[
    (df['type'].isin(tipos_selecionados)) &
    (df['release_year'] >= anos_selecionados[0]) & 
    (df['release_year'] <= anos_selecionados[1])
]

if paises_selecionados:
    df_filtrado = df_filtrado[df_filtrado['countries'].dropna().apply(lambda x: any(p in x for p in paises_selecionados))]

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado com os filtros selecionados.")
else:
    st.subheader("Métricas Chave")
    col1, col2, col3 = st.columns(3)
    total_titulos = df_filtrado.shape[0]
    total_filmes = df_filtrado[df_filtrado['type'] == 'Movie'].shape[0]
    total_series = df_filtrado[df_filtrado['type'] == 'TV Show'].shape[0]
    col1.metric("Total de Títulos", f"{total_titulos:,}")
    col2.metric("Total de Filmes", f"{total_filmes:,}")
    col3.metric("Total de Séries", f"{total_series:,}")
    st.markdown("---")

    st.subheader("Visualizações")
    
    col_graf1, col_graf2 = st.columns(2)

    df_paises = df_filtrado['countries'].dropna().str.split(', ').explode().value_counts().nlargest(10)
    fig_bar_paises = px.bar(
        df_paises, 
        x=df_paises.index, 
        y=df_paises.values, 
        title='Top 10 Países com Mais Produções',
        labels={'x': 'País', 'y': 'Quantidade de Títulos'}
    )
    # CORREÇÃO DO AVISO: Trocando use_container_width por width
    col_graf1.plotly_chart(fig_bar_paises, width='stretch')

    df_tipos = df_filtrado['type'].value_counts()
    fig_pie_tipos = px.pie(
        df_tipos, 
        names=df_tipos.index, 
        values=df_tipos.values, 
        title='Proporção de Filmes vs. Séries de TV'
    )
    # CORREÇÃO DO AVISO: Trocando use_container_width por width
    col_graf2.plotly_chart(fig_pie_tipos, width='stretch')

    df_generos = df_filtrado['listed_in'].dropna().str.split(', ').explode().value_counts().nlargest(10)
    fig_bar_generos = px.bar(
        df_generos,
        x=df_generos.values,
        y=df_generos.index,
        orientation='h',
        title='Top 10 Gêneros Mais Comuns',
        labels={'x': 'Quantidade de Títulos', 'y': 'Gênero'}
    )
    fig_bar_generos.update_layout(yaxis={'categoryorder':'total ascending'})
    # CORREÇÃO DO AVISO: Trocando use_container_width por width
    st.plotly_chart(fig_bar_generos, width='stretch')

    df_filmes = df_filtrado[df_filtrado['type'] == 'Movie'].copy()
    
    # --- CORREÇÃO DO ERRO FATAL APLICADA AQUI ---
    # 1. Remove ' min' e converte para número de forma segura, transformando erros em NaN
    duration_numeric = pd.to_numeric(df_filmes['duration'].str.replace(' min', ''), errors='coerce')
    # 2. Remove as linhas onde a conversão falhou (onde a duração agora é NaN)
    df_filmes = df_filmes.dropna(subset=['duration'])
    df_filmes['duration_min'] = duration_numeric.dropna().astype(int)

    fig_scatter = px.scatter(
        df_filmes, 
        x='release_year', 
        y='duration_min', 
        hover_data=['title'],
        title='Duração dos Filmes por Ano de Lançamento',
        labels={'release_year': 'Ano de Lançamento', 'duration_min': 'Duração (minutos)'}
    )
    # CORREÇÃO DO AVISO: Trocando use_container_width por width
    st.plotly_chart(fig_scatter, width='stretch')

    df_ano_adicionado = df_filtrado.groupby('year_added').size().reset_index(name='count')
    fig_line_ano = px.line(
        df_ano_adicionado,
        x='year_added',
        y='count',
        title="Evolução de Títulos Adicionados à Netflix por Ano",
        labels={'year_added': 'Ano', 'count': 'Quantidade de Títulos'}
    )
    fig_line_ano.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
    # CORREÇÃO DO AVISO: Trocando use_container_width por width
    st.plotly_chart(fig_line_ano, width='stretch')
# --- FIM DA MODIFICAÇÃO ---