import streamlit as st
import pandas as pd

df = pd.read_csv("./data/remotive_validado.csv")

st.title("Validador Inteligente de Vagas")

# Filtros
categoria = st.selectbox("Categoria", options=["Todas"] + sorted(df["category"].unique().tolist()))
min_score = st.slider("Score mínimo de qualidade", 0, 6, 1)

# Aplicar filtros
df_filtrado = df.copy()
if categoria != "Todas":
    df_filtrado = df_filtrado[df_filtrado["category"] == categoria]
df_filtrado = df_filtrado[df_filtrado["pontuacao"] >= min_score]

# Visualização
st.write(df_filtrado[["title", "company_name", "pontuacao", "salary", "description"]])
