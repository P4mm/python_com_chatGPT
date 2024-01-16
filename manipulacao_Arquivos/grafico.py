import csv
import matplotlib.pyplot as plt

# Nome do arquivo CSV de entrada
arquivo_csv = "dados2.csv"

# Leitura dos dados do arquivo CSV
try:
    with open(arquivo_csv, "r") as csv_file:
        leitor_csv = csv.DictReader(csv_file)
        dados = list(leitor_csv)
except FileNotFoundError:
    print(f"Arquivo {arquivo_csv} não encontrado.")
    dados = []

# Verificar se há dados no arquivo CSV
if dados:
    # Extrair salários e nomes dos funcionários
    salarios = []
    nomes = []

    for linha in dados:
        if 'salario' in linha:
            try:
                salario = float(linha['salario'])
                salarios.append(salario)
                nomes.append(linha.get('nome', 'Funcionário'))
            except ValueError:
                print(f"Erro ao converter salário para float na linha: {linha}")

    # Criar gráfico de barras
    plt.bar(nomes, salarios, color='blue')
    plt.xlabel('Funcionários')
    plt.ylabel('Salários')
    plt.title('Salários dos Funcionários')

    # Exibir o gráfico
    plt.show()
else:
    print("Não há dados no arquivo CSV.")
import csv
import matplotlib.pyplot as plt

# Nome do arquivo CSV de entrada
arquivo_csv = "dados2.csv"

# Leitura dos dados do arquivo CSV
try:
    with open(arquivo_csv, "r") as csv_file:
        leitor_csv = csv.DictReader(csv_file)
        dados = list(leitor_csv)
except FileNotFoundError:
    print(f"Arquivo {arquivo_csv} não encontrado.")
    dados = []

# Verificar se há dados no arquivo CSV
if dados:
    # Extrair salários e nomes dos funcionários
    salarios = []
    nomes = []

    for linha in dados:
        if 'salario' in linha:
            try:
                salario = float(linha['salario'])
                salarios.append(salario)
                nomes.append(linha.get('nome', 'Funcionário'))
            except ValueError:
                print(f"Erro ao converter salário para float na linha: {linha}")

    # Criar gráfico de barras
    plt.bar(nomes, salarios, color='blue')
    plt.xlabel('Funcionários')
    plt.ylabel('Salários')
    plt.title('Salários dos Funcionários')

    # Exibir o gráfico
    plt.show()
else:
    print("Não há dados no arquivo CSV.")
