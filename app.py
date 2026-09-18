"""Aplicação Streamlit para análise de um portefólio de investimentos."""

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Análise de Portefólio", page_icon="📊", layout="wide")

COLUNAS_OBRIGATORIAS = [
    "Ticker",
    "Quantidade",
    "Preco_Medio_Compra",
    "Tipo_Ativo",
    "Setor",
    "Pais",
]

TIPOS_ATIVO_VALIDOS = ["Ações", "ETF", "Crypto", "P2P"]


def carregar_portefolio(ficheiro) -> pd.DataFrame:
    df = pd.read_csv(ficheiro)
    df.columns = [c.strip() for c in df.columns]

    colunas_em_falta = [c for c in COLUNAS_OBRIGATORIAS if c not in df.columns]
    if colunas_em_falta:
        raise ValueError(
            "O ficheiro CSV não tem as colunas obrigatórias: "
            + ", ".join(colunas_em_falta)
        )

    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce")
    df["Preco_Medio_Compra"] = pd.to_numeric(df["Preco_Medio_Compra"], errors="coerce")

    linhas_invalidas = df[df["Quantidade"].isna() | df["Preco_Medio_Compra"].isna()]
    if not linhas_invalidas.empty:
        st.warning(
            f"{len(linhas_invalidas)} linha(s) com Quantidade ou Preço Médio de "
            "Compra inválidos foram ignoradas."
        )
    df = df.dropna(subset=["Quantidade", "Preco_Medio_Compra"])

    df["Valor_Investido"] = df["Quantidade"] * df["Preco_Medio_Compra"]
    return df


def grafico_alocacao(df: pd.DataFrame, coluna: str, tipo_grafico: str, titulo: str):
    dados = df.groupby(coluna, as_index=False)["Valor_Investido"].sum()
    dados = dados.sort_values("Valor_Investido", ascending=False)

    if tipo_grafico == "Pie Chart":
        fig = px.pie(
            dados,
            names=coluna,
            values="Valor_Investido",
            title=titulo,
            hole=0.35,
        )
        fig.update_traces(textinfo="percent+label", hovertemplate="%{label}<br>%{value:,.2f} €")
    else:
        fig = px.treemap(
            dados,
            path=[coluna],
            values="Valor_Investido",
            title=titulo,
        )
        fig.update_traces(hovertemplate="%{label}<br>%{value:,.2f} €")

    fig.update_layout(margin=dict(t=60, l=10, r=10, b=10))
    return fig


st.title("📊 Análise do Meu Portefólio de Investimentos")
st.caption(
    "Carrega um ficheiro CSV com o teu portefólio para veres o valor total "
    "investido e a distribuição por tipo de ativo, setor e país."
)

with st.expander("ℹ️ Formato esperado do ficheiro CSV", expanded=False):
    st.markdown(
        """
O ficheiro CSV deve ter as seguintes colunas (o nome tem de ser exatamente igual):

| Coluna | Descrição | Exemplo |
|---|---|---|
| `Ticker` | Símbolo do ativo | `AAPL` |
| `Quantidade` | Número de unidades detidas | `10` |
| `Preco_Medio_Compra` | Preço médio pago por unidade | `150.50` |
| `Tipo_Ativo` | Um de: Ações, ETF, Crypto, P2P | `Ações` |
| `Setor` | Setor económico do ativo | `Tecnologia` |
| `Pais` | País do ativo/empresa | `EUA` |

Tens um ficheiro de exemplo (`sample_portfolio.csv`) na pasta do projeto que podes
usar para testar a aplicação.
        """
    )

ficheiro = st.file_uploader("Carrega o teu ficheiro CSV", type=["csv"])

if ficheiro is None:
    st.info("Carrega um ficheiro CSV acima para começar a análise.")
    st.stop()

try:
    df = carregar_portefolio(ficheiro)
except ValueError as erro:
    st.error(str(erro))
    st.stop()

if df.empty:
    st.error("O ficheiro não contém linhas válidas para analisar.")
    st.stop()

valor_total = df["Valor_Investido"].sum()
num_posicoes = len(df)
num_tickers = df["Ticker"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Valor Total Investido", f"{valor_total:,.2f} €")
col2.metric("Número de Posições", num_posicoes)
col3.metric("Ativos Distintos", num_tickers)

st.divider()

st.subheader("Dados do Portefólio")
st.dataframe(
    df.style.format({"Preco_Medio_Compra": "{:,.2f} €", "Valor_Investido": "{:,.2f} €"}),
    use_container_width=True,
)

st.divider()

st.subheader("Distribuição da Carteira")
tipo_grafico = st.radio(
    "Tipo de gráfico", ["Pie Chart", "Treemap"], horizontal=True
)

col_tipo, col_setor, col_pais = st.columns(3)
with col_tipo:
    st.plotly_chart(
        grafico_alocacao(df, "Tipo_Ativo", tipo_grafico, "Por Tipo de Ativo"),
        use_container_width=True,
    )
with col_setor:
    st.plotly_chart(
        grafico_alocacao(df, "Setor", tipo_grafico, "Por Setor"),
        use_container_width=True,
    )
with col_pais:
    st.plotly_chart(
        grafico_alocacao(df, "Pais", tipo_grafico, "Por País"),
        use_container_width=True,
    )
