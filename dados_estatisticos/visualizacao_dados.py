import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do Conjunto de Dados Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
nomes_colunas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dados = pd.read_csv(url, names=nomes_colunas)

# Gráfico de Dispersão (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='class', data=dados)
plt.title('Gráfico de Dispersão entre Comprimento e Largura das Sépalas')
plt.xlabel('Comprimento da Sépala (cm)')
plt.ylabel('Largura da Sépala (cm)')
plt.show()

# Histograma
plt.figure(figsize=(10, 6))
sns.histplot(data=dados, x='petal_length', kde=True, hue='class', multiple='stack', bins=30)
plt.title('Histograma do Comprimento da Pétala')
plt.xlabel('Comprimento da Pétala (cm)')
plt.show()

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='class', y='petal_width', data=dados)
plt.title('Boxplot da Largura da Pétala por Classe')
plt.xlabel('Classe')
plt.ylabel('Largura da Pétala (cm)')
plt.show()
