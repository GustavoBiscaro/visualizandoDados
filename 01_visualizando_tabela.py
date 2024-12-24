from pathlib import Path
import streamlit as st
import pandas as pd

# Define o caminho da pasta e do arquivo
pasta_datasets = Path("D:\Asimov Projects\Prj1\datasets")
caminho_vendas = pasta_datasets / 'vendas.csv'

# Lê o arquivo CSV
df_vendas = pd.read_csv(caminho_vendas, sep=';', decimal=',')

# Exibe o DataFrame no Streamlit
st.dataframe(df_vendas)
