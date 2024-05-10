import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set_theme() 


def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):  ## função para plotar gráficos
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'sort':  # organizar valores 
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    elif opcao == 'unstack':   # quando quiser usar 2 colunas como referência, uma como linhas e a outra como colunas
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)  # legenda do eixo y
    plt.xlabel(xlabel)  # legenda do eixo x
    st.pyplot(fig=plt)
    return None


st.set_page_config(page_title= 'SINASC RO', 
                   page_icon= 'https://st.depositphotos.com/9212956/55734/v/600/depositphotos_557348774-stock-illustration-rondonia-map-flag-vector-silhouette.jpg', 
                   layout='wide')

st.write('# Análise SINASC - RO')

sinasc = pd.read_csv('SINASC_RO_2019.csv') # carregar base de dados

sinasc.DTNASC = pd.to_datetime(sinasc.DTNASC)

min_data = sinasc.DTNASC.min()
max_data = sinasc.DTNASC.max()



data_inicial = st.sidebar.date_input('Data inicial', 
                            value = min_data,
                            min_value = min_data,
                            max_value = max_data) 


data_final = st.sidebar.date_input('Data final', 
                            value = max_data,
                            min_value = min_data,
                            max_value = max_data) 


st.sidebar.write('Data inicial = ', data_inicial)
st.sidebar.write('Data final = ', data_final)

sinasc = sinasc[(sinasc['DTNASC'] <= pd.to_datetime(data_final)) & (sinasc['DTNASC'] >= pd.to_datetime(data_inicial))]
st.write(sinasc)
st.write(sinasc.shape)

plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe', 'data_nascimento', opcao='nada')
plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'count', 'quantidade de nascimentos', 'data_nascimento', opcao='nada')
plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'count', 'idade', 'data_nascimento', opcao='unstack')
plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'count', 'peso', 'data_nascimento', opcao='unstack')
plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'peso', 'escolaridade_mae', opcao='sort') 
plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio', 'gestacao', opcao='sort')
plota_pivot_table(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio', 'gestacao', opcao='sort')

