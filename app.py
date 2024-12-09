import pandas as pd
import requests
import streamlit as st
import matplotlib.pyplot as plt

def load_data(start_data = None,end_data=None,product=None):
    url = 'http://127.0.0.1:8000/api/sales'
    parames = {}
    if start_data:
        parames['start_data'] = start_data
    if end_data:
        parames['end_data'] = end_data
    if product:
        parames['product'] = product
    response = requests.get(url,params=parames)
    
    data = response.json()
    if isinstance(data,list):
        return pd.DataFrame(data)
    else:
        st.error('formato inesperado na api')
        return pd.DataFrame()
#filtros
st.sidebar.header('filtros')
start_data = st.sidebar.date_input('data de inicio', pd.to_datetime('2024-01-01'))
end_data = st.sidebar.date_input('data de fim', pd.to_datetime('2024-12-31'))
product = st.sidebar.text_input('produto','')
#carregar os dados 
data = load_data(start_data=start_data,end_data=end_data,product=product)

tab = st.selectbox('Escolha Uma ABA',[
                  'Tabela Com Dados',
                  'Gráfico De Vendas',] 
                   )
if tab == 'Tabela Com Dados':
    st.title('análise de vendas')
    st.subheader('dataset de vendas')
    st.dataframe(data,use_container_width=True)
    #exportando dados para csv
    st.subheader('exportar dados para csv')
    csv = data.to_csv(index=False)
    st.download_button(
        label='baixar dados como csv',
        data=csv,
        file_name='dados_vendas.csv',
        mime='text/csv'
    )
    
elif tab == 'Gráfico De Vendas':
    

    #grafico de vendas

    st.subheader('gráfico de vendas por data ')
    fig,ax = plt.subplots()
    data['data'] = pd.to_datetime(data['data'])
    data.groupby('data')['quantidade'].sum().plot(ax=ax)
    ax.set_xlabel('data')
    ax.set_ylabel('quantidade vendida')
    st.pyplot(fig)

    #grafico (vendas/produto)

    st.subheader('gráfico de vendas por produto')
    product_sales = data.groupby('produto')['quantidade'].sum().reset_index()
    fig2,ax2 = plt.subplots()
    product_sales.plot(
        kind='bar',x='produto',
        y='quantidade',ax=ax2
    )
    ax2.set_xlabel('produto')
    ax2.set_ylabel('quantidde vendida')
    ax2.set_title('vendas por produto')
    st.pyplot(fig2)

