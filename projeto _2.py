import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Configuração do estilo dos gráficos
sns.set(context='talk', style='ticks')

# Configuração da página
st.set_page_config(
     page_title="Análise de Previsão de Renda",
     page_icon="💰",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

# Upload do CSV (mais flexível do que caminho fixo)
arquivo = st.file_uploader("Envie o arquivo CSV de renda", type="csv")

if arquivo is not None:
    renda = pd.read_csv(arquivo)

    # ---------------------------
    # Gráficos ao longo do tempo
    # ---------------------------
    st.write('## Gráficos ao longo do tempo')
    fig, ax = plt.subplots(8, 1, figsize=(10, 70))

    renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
    sns.lineplot(x='data_ref', y='renda', hue='posse_de_imovel', data=renda, ax=ax[1])
    ax[1].tick_params(axis='x', rotation=45)

    sns.lineplot(x='data_ref', y='renda', hue='posse_de_veiculo', data=renda, ax=ax[2])
    ax[2].tick_params(axis='x', rotation=45)

    sns.lineplot(x='data_ref', y='renda', hue='qtd_filhos', data=renda, ax=ax[3])
    ax[3].tick_params(axis='x', rotation=45)

    sns.lineplot(x='data_ref', y='renda', hue='tipo_renda', data=renda, ax=ax[4])
    ax[4].tick_params(axis='x', rotation=45)

    sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax[5])
    ax[5].tick_params(axis='x', rotation=45)

    sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda, ax=ax[6])
    ax[6].tick_params(axis='x', rotation=45)

    sns.lineplot(x='data_ref', y='renda', hue='tipo_residencia', data=renda, ax=ax[7])
    ax[7].tick_params(axis='x', rotation=45)

    sns.despine()
    st.pyplot(fig)

    # ---------------------------
    # Gráficos bivariados
    # ---------------------------
    st.write('## Gráficos bivariados')
    fig2, ax2 = plt.subplots(7, 1, figsize=(10, 50))

    sns.barplot(x='posse_de_imovel', y='renda', data=renda, ax=ax2[0])
    sns.barplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax2[1])
    sns.barplot(x='qtd_filhos', y='renda', data=renda, ax=ax2[2])
    sns.barplot(x='tipo_renda', y='renda', data=renda, ax=ax2[3])
    sns.barplot(x='educacao', y='renda', data=renda, ax=ax2[4])
    sns.barplot(x='estado_civil', y='renda', data=renda, ax=ax2[5])
    sns.barplot(x='tipo_residencia', y='renda', data=renda, ax=ax2[6])

    sns.despine()
    st.pyplot(fig2)
else:
    st.warning("Por favor, envie o arquivo CSV para visualizar os gráficos.")
