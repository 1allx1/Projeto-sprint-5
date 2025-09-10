# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles.csv')


def main():
    st.title("Projeto Sprint 5")
    st.markdown("Sprint 5 — Ferramentas de Desenvolvimento de Software")
    st.markdown(
        "Análise Exploratória de Dados no conjunto de dados de anúncios de vendas de carros.")

    # quick info
    st.dataframe(df.head())

    st.header("Histograma")

    if st.button("Criar histograma"):
        fig = px.histogram(df, x="odometer")
        st.plotly_chart(fig)

    st.header("Grafico de Dispersão")

    if st.checkbox("Mostrar Grafico de Dispersão"):
        fig2 = px.scatter(df, x='price', y='odometer', color='paint_color',
                          title=f"Dispersão — price vs odometer")
        st.plotly_chart(fig2)


if __name__ == "__main__":
    main()
