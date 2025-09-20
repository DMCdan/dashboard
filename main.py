import pandas as pd
import streamlit as st
import plotly.express as px

st.markdown("""
<style>
#dashboard-de-analise-de-roupas {
    color: #b209f5ff
}
            
</style>
""", unsafe_allow_html=True)

#config da pag
st.set_page_config(
    page_title="dashboard da zara",
    layout="wide"
)

st.title("dashboard de analise de roupas")
st.markdown("**explore** os dados de produtos de zara")

@st.cache_data
def load_data():
    df = pd.read_csv("zara.csv", sep=";")
    return df

df = load_data()

section = st.sidebar.multiselect(
    "Selecione a Seção: ",
    options=df["section"].unique(),
    default=df["section"].unique()
)

promotion = st.sidebar.multiselect(
    "Selecione se deseja promoções: ",
    options=df["Promotion"].unique(),
    default=df["Promotion"].unique()
)

df_filtered = df[df["section"].isin(section) & df["Promotion"].isin(promotion)]
st.subheader("Principais Métricas: ")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Produtos", len(df_filtered))
col2.metric("Soma Total", round(df_filtered["price"].sum(),2))
col3.metric("Média Total", round(df_filtered["price"].mean(),2))
price_distiribution = px.histogram(
    df_filtered,
    x="price",
    nbins=50,
    title="DIstribuiçao de Preços",
    template="plotly_white"
)

st.plotly_chart(price_distiribution)
st.dataframe(df_filtered)
