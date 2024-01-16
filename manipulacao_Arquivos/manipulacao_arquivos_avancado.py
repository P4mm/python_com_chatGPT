import csv
import json

# Função para calcular a média dos salários
def calcular_media_salarios(dados):
    if not dados:
        return 0  # Retorna 0 se não houver dados

    salarios = [float(linha['salario']) for linha in dados]
    media = sum(salarios) / len(salarios)
    return media

# Função para encontrar o funcionário com o maior salário
def encontrar_maior_salario(dados):
    if not dados:
        return None  # Retorna None se não houver dados

    funcionario_maior_salario = max(dados, key=lambda x: float(x.get('salario', 0)))
    return funcionario_maior_salario

# Nome do arquivo CSV de entrada e arquivo JSON de saída
arquivo_csv = "dados.csv"
arquivo_json = "saida.json"

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
    # Operações nos dados (por exemplo, duplicar os salários)
    for linha in dados:
        if 'salario' in linha:
            try:
                linha['salario'] = float(linha['salario']) * 2
            except ValueError:
                print(f"Erro ao converter salário para float na linha: {linha}")

    # Escrita dos dados modificados no arquivo JSON
    with open(arquivo_json, "w") as json_file:
        json.dump(dados, json_file, indent=2)

    print(f"Dados modificados foram salvos em {arquivo_json}")

    # Calcular e exibir a média dos salários
    media_salarios = calcular_media_salarios(dados)
    print(f"Média dos salários: {media_salarios}")

    # Encontrar e exibir o funcionário com o maior salário
    funcionario_maior_salario = encontrar_maior_salario(dados)
    print(f"Funcionário com maior salário: {funcionario_maior_salario}")
else:
    print("Não há dados no arquivo CSV.")
