import pandas as pd

# Leitura do Conjunto de Dados Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
nomes_colunas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dados = pd.read_csv(url, names=nomes_colunas)

# Exibição das Estatísticas Descritivas
estatisticas_descritivas = dados.describe()
print("Estatísticas Descritivas:")
print(estatisticas_descritivas)

# Contagem de Amostras por Classe
contagem_classes = dados['class'].value_counts()
print("\nContagem de Amostras por Classe:")
print(contagem_classes)

# Salvando as Estatísticas Descritivas em um Novo Arquivo CSV
arquivo_estatisticas = "estatisticas_descritivas.csv"
estatisticas_descritivas.to_csv(arquivo_estatisticas, index=False)
print(f"\nEstatísticas Descritivas salvas em '{arquivo_estatisticas}'.")
