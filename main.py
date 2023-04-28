import pandas as pd
import plotly.express as px
# Passo 1: Importar a base de dados
tabela = pd.read_csv(r"E:\Cursos\hashtag_python\Aula 2\telecom_users.csv")

# axis -> 0 = Linha; axis -> 1 = Coluna
tabela = tabela.drop("Unnamed: 0", axis=1)

# Vizualizar informações sobre a tabela (tipo de dados, quantos valores em cada coluna)
# print(tabela.info())

# Passo 3: Tratamento de Dados
# - Resolver os valores que estão sendo reconhecidos de forma errada

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - Resolver valores vazios
# excluir todas as colunas que TODOS os valores são vazios
tabela = tabela.dropna(how="all", axis=1)

# excluir todas as linhas que tem pelo menos um campo vazio
tabela = tabela.dropna(how="any", axis=0)
# print(tabela.info())

# print(tabela["Churn"].value_counts())
# print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# cria o grafico
coluna = "Aposentado"
grafico = px.histogram(tabela, x=coluna, color="Churn")

grafico.show()
