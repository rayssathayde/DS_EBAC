import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(layout='wide')

st.title('Primeiro aplicativo com Streamlit')


st.write('''Com o comando `st.write()`, conhecido como o canivete suiço do Streamlit, podemos fazer muitas coisas. 
         Como, por exemplo, um dataframe: ''')

st.write('##### Dataframe criado a partir do pacote Pandas')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.write('Ou um gráfico:')

st.write('##### Histograma criado pelo pacote Matplotlib, usando como referência um array criado pelo pacote Numpy')

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  

st.write('''Contudo, nem sempre o ideal é utilizar o `st.write()`. 
         Esse comando analisa os dados que você transmitiu e, em seguida, decide a melhor forma de renderizá-los no aplicativo. 
         Se você quiser mostrar os dados de uma forma mais específica, outros comandos podem ajudar. ''')


st.write(''' Por exemplo, abaixo está uma tabela interativa criada com o comando `st.dataframe()`. 
         Para os dados, usamos o Numpy para gerar uma amostra aleatória.
         Com o objeto :blue[Styler] destacamos os elementos de maior valor em cada coluna.''')



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


st.write('Com o método `st.table()` podemos gerar tabelas estáticas.')


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

st.write('Você pode adicionar facilmente um gráfico de linhas ao seu aplicativo com `st.line_chart()`.')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write('Com `st.map()` você pode exibir pontos de dados em um mapa.')

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


st.markdown('-----------')

st.write('##### Widgets')

st.write('Você pode incluir widgets interativos, como os exemplos abaixo:')

st.markdown('-`st.slider()`')

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.markdown('-----------')

st.write('Pode usar uma caixa de seleção para ocultar ou mostrar dados.')

st.markdown('-`st.checkbox()`')


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st.markdown('-----------')


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)


# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write('Pode organizar seus dados e widgets em duas colunas, usando `st.columns()`.')

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

st.markdown('-----------')

st.write('Ao adicionar cálculos de execução longa, você pode usar `st.progress()` para exibir o status em tempo real.')


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

st.markdown('-----------')

st.write('''Enfim, há um mundo de possibilidades.
         Você pode criar uma barra lateral, como a desse aplicativo, e organizar melhor seus dados.
         Pode mudar o tema do seu aplicativo, aumentar e diminuir fontes, deixar :red[textos coloridos], em **negrito** ou *itálico*.
         É so usar sua imaginação para apresentar seus dados da melhor forma possível!''')