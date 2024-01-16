import gspread
from google.oauth2 import service_account

def autenticar_google_sheets(credencial_path, planilha_nome, guia_nome):
    try:
        # Configurar as credenciais usando google-auth
        creds = service_account.Credentials.from_service_account_file(
            credencial_path,
            scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        )

    except Exception as e:
        print(f"Erro durante a autenticação: {e}")
        return None

    # Autorizar o cliente gspread
    gc = gspread.authorize(creds)

    try:
        # Abrir a planilha pelo nome
        planilha = gc.open(planilha_nome)
        guia = planilha.worksheet(guia_nome)

    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Planilha não encontrada: {e}")
        return None

    except gspread.exceptions.WorksheetNotFound as e:
        print(f"Guia não encontrada: {e}")
        return None

    return guia

def adicionar_dados(guia, dados):
    # Adicionar uma nova linha à planilha
    guia.append_row(dados)

if __name__ == "__main__":
    # Configurações
    credencial_path = r"C:/Users/User/Desktop/credentials.json"
    planilha_nome = "automacao1"
    guia_nome = "sheet"

    # Dados para adicionar
    novos_dados = ["Novo Dado 1", "Novo Dado 2", "Novo Dado 3"]

    # Autenticar no Google Sheets
    guia = autenticar_google_sheets(credencial_path, planilha_nome, guia_nome)

    if guia:
        # Adicionar dados à planilha
        adicionar_dados(guia, novos_dados)

        print("Dados adicionados com sucesso!")
