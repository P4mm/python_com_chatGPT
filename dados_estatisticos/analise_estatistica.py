#Análise Estatística:

#Calcule a média, mediana e desvio padrão para cada coluna numérica do conjunto de dados.
#Determine quantas amostras existem para cada classe no conjunto de dados.

import pandas as pd

# Leitura do conjunto de dados Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
nomes_colunas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dados = pd.read_csv(url, names=nomes_colunas)

# Exibição das estatísticas descritivas
estatisticas_descritivas = dados.describe()
print("Estatísticas Descritivas:")
print(estatisticas_descritivas)

# Contagem de amostras para cada classe
contagem_classes = dados['class'].value_counts()
print("\nContagem de Amostras por Classe:")
print(contagem_classes)

# Salvar o DataFrame em um arquivo CSV
caminho_saida_csv = "iris_output.csv"
data_iris.to_csv(caminho_saida_csv, index=False)

print(f"Os dados foram salvos em: {caminho_saida_csv}")
