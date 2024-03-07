import streamlit as st 
import pandas as pd
import plotly.express as px

# Define um layout de página amplo para o aplicativo Streamlit
st.set_page_config(layout="wide")

# Lê o arquivo CSV "supermarket_sales.csv" em um DataFrame Pandas com separador e ponto decimal específicos
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
# Converte a coluna "Date" para o formato datetime
df["Date"] = pd.to_datetime(df["Date"])
# Ordena o DataFrame com base na coluna "Date"
df = df.sort_values("Date")

# Cria uma nova coluna "Month" aplicando uma função lambda para concatenar ano e mês da coluna "Date"
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
# Cria um widget de barra lateral com um dropdown para selecionar um mês específico
month = st.sidebar.selectbox("Mês", df["Month"].unique())

# Filtra o DataFrame incluindo apenas as linhas correspondentes ao mês selecionado
df_filtered = df[df["Month"] == month]

# Cria colunas no Streamlit para organizar o layout
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Cria um gráfico de barras para as vendas totais por dia, colorido por cidade
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

# Cria um gráfico de barras horizontais para as vendas totais por linha de produto, colorido por cidade
fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# Agrupa por cidade e calcula as vendas totais para cada cidade, depois cria um gráfico de barras
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

# Cria um gráfico de pizza para a distribuição das vendas totais por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

# Agrupa por cidade e calcula a avaliação média para cada cidade, depois cria um gráfico de barras
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, x="City", y="Rating", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)


#streamlit run caminho_do_arquivo