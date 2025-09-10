import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
fig = px.histogram(car_data, x="odometer")  # criar um histograma
fig.show()  # exibindo

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
# criar um gráfico de dispersão
fig = px.scatter(car_data, x="odometer", y="price")
fig.show()  # exibindo

st.write('Análise Exploratória de Dados')
st.write(
    'Este aplicativo realiza uma análise exploratória de dados no conjunto de dados de anúncios de vendas de carros.')

st.dataframe(car_data, height=600)  # exibir o dataframe

hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:  # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')
