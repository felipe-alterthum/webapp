import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Esse é o meu primeiro aplicativo web', divider ='blue')
st.header('O app foi feito utilizando red[*Streamlit*]')

car_data = pd.read_csv('/notebooks/vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma')

if hist_button:
    #Escrevendo a mensagem
    st.write('Criando o histograma com os dados de kilometragem')

    #Criando um histograma
    fig = px.histogram(car_data, x="odometer")

    #Exibindo
    st.plotly_chart(fig, use_container_width=True) 



