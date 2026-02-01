import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------
# Configuração da página
# -----------------------
st.set_page_config(
    page_title="Dashboard de Salários",
    layout="wide"
)

st.title("📊 Dashboard de Salários")

# -----------------------
# Carregamento dos dados
# -----------------------
@st.cache_data
def carregar_dados():
    return pd.read_csv(
        "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
    )

df = carregar_dados()

# -----------------------
# Sidebar - Filtros
# -----------------------
st.sidebar.header("🎛️ Filtros")

filtro_ano = st.sidebar.multiselect(
    "Ano",
    options=sorted(df["ano"].unique()),
    default=sorted(df["ano"].unique()),
)

filtro_senioridade = st.sidebar.multiselect(
    "Senioridade",
    options=sorted(df["senioridade"].unique()),
    default=sorted(df["senioridade"].unique()),
)

filtro_contrato = st.sidebar.multiselect(
    "Tipo de contrato",
    options=sorted(df["contrato"].unique()),
    default=sorted(df["contrato"].unique()),
)

filtro_remoto = st.sidebar.multiselect(
    "Modalidade de trabalho",
    options=sorted(df["remoto"].unique()),
    default=sorted(df["remoto"].unique()),
)

# -----------------------
# DataFrame filtrado
# -----------------------
df_filtrado = df[
    (df["ano"].isin(filtro_ano)) &
    (df["senioridade"].isin(filtro_senioridade)) &
    (df["contrato"].isin(filtro_contrato)) &
    (df["remoto"].isin(filtro_remoto))
]

# -----------------------
# KPIs
# -----------------------
st.subheader("📌 Indicadores Gerais")

k1, k2, k3, k4 = st.columns(4)

k1.metric("💰 Salário médio (USD)", f"${df_filtrado['usd'].mean():,.0f}")
k2.metric("📊 Salário mediano (USD)", f"${df_filtrado['usd'].median():,.0f}")
k3.metric("🚀 Salário máximo (USD)", f"${df_filtrado['usd'].max():,.0f}")
k4.metric("🧮 Total de registros", df_filtrado.shape[0])

st.divider()

# -----------------------
# Layout 2x2 - Gráficos
# -----------------------
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# 🌍 Mapa
with col1:
    st.subheader("🌍 Salário médio por país")

    import pycountry

    def iso3_para_nome(iso3):
        try:
            return pycountry.countries.get(alpha_3=iso3).name
        except:
            return iso3

    df_pais = (
        df_filtrado
        .groupby("residencia_iso3", as_index=False)
        .agg(salario_medio=("usd", "mean"))
    )

    # 🔑 cria o nome do país APÓS o groupby
    df_pais["pais"] = df_pais["residencia_iso3"].apply(iso3_para_nome)

    fig_mapa = px.choropleth(
        df_pais,
        locations="residencia_iso3",
        color="salario_medio",
        hover_name="pais",  # 👈 AGORA FUNCIONA
        labels={"salario_medio": "Salário médio (USD)"},
        color_continuous_scale=[
            (0.0, "red"),
            (0.5, "yellow"),
            (1.0, "green")
        ],
        hover_data={
            "residencia_iso3": False,
            "salario_medio": ":,.0f"
        }
    )

    fig_mapa.update_layout(
        coloraxis_colorbar=dict(
            title="Salário médio (USD)"
        )
    )

    st.plotly_chart(fig_mapa, use_container_width=True)



# 🥧 Contrato
with col2:
    st.subheader("🥧 Média salarial por tipo de contrato")

    df_contrato = (
        df_filtrado
        .groupby("contrato", as_index=False)
        .agg(media_salarial=("usd", "mean"))
    )

    fig_contrato = px.pie(
        df_contrato,
        names="contrato",
        values="media_salarial",
        hole=0.4
    )

    st.plotly_chart(fig_contrato, use_container_width=True)

# 🥧 Senioridade
with col3:
    st.subheader("🥧 Distribuição por senioridade")

    df_senioridade = (
        df_filtrado
        .groupby("senioridade", as_index=False)
        .size()
        .rename(columns={"size": "quantidade"})
    )

    fig_senioridade = px.pie(
        df_senioridade,
        names="senioridade",
        values="quantidade",
        hole=0.4
    )

    st.plotly_chart(fig_senioridade, use_container_width=True)

# 🥧 Modalidade
with col4:
    st.subheader("🥧 Modalidade de trabalho")

    df_remoto = (
        df_filtrado
        .groupby("remoto", as_index=False)
        .size()
        .rename(columns={"size": "quantidade"})
    )

    fig_remoto = px.pie(
        df_remoto,
        names="remoto",
        values="quantidade",
        hole=0.4
    )

    st.plotly_chart(fig_remoto, use_container_width=True)

st.divider()

# -----------------------
# Top 10 cargos
# -----------------------
st.subheader("🏆 Top 10 cargos por salário médio")

df_top_cargos = (
    df_filtrado
    .groupby("cargo", as_index=False)
    .agg(media_salarial=("usd", "mean"))
    .sort_values("media_salarial", ascending=False)
    .head(10)
)

fig_top_cargos = px.bar(
    df_top_cargos,
    x="media_salarial",
    y="cargo",
    orientation="h"
)

st.plotly_chart(fig_top_cargos, use_container_width=True)






















