import os

# Lista para guardar os contatos
agenda = []

# Adicionar contato
def adicionar_contato(nome, telefone, email):
    pass

# Visualizar lista de contato
def listar_contatos(nome, telefone, email):
    pass

# Editar contato
def editar_contato(nome, telefone, email):
    pass

# Marcar/Desmarcar contato favorito
def marcar_desmarcar_favorito(nome, telefone, email):
    pass

# Listar favoritos
def listar_favoritos(nome, telefone, email):
    pass

# Apagar contato
def apagar_contato(nome, telefone, email):
    pass

# Mostrar menu de opções
def mostrar_menu():
    print("\nAgenda de Contatos")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contato")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato favorito")
    print("5. Listar contatos favoritos")
    print("6. Apagar contato")
    print("6. Sair")

# Limpar tela - cls para windows e clear para linux
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    # Menu de opções
    mostrar_menu()
    try:
        escolha = int(input("Informe o número de sua escolha: "))
    except Exception as e:
        limpar_tela()
        print("Escolha inválida!")
    else:
        if escolha == 1:
            print("Adicionando contato")
            nome        = input("Informe um nome*: ")
            telefone    = input("Informe número de telefone*: ")
            email       = input("Informe um e-mail: ")
            adicionar_contato(nome, telefone, email)
        elif escolha == 6:
            break