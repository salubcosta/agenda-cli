import os

# Lista para guardar os contatos
agenda = []

# Adicionar contato
def adicionar_contato(agenda, nome, telefone, email):
    if not nome or not telefone:
        print("⚠️  Informe nome e telefone.")
    else:
        contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
        agenda.append(contato)
        print("✅  Contato adicionado.")

# Visualizar lista de contato
def listar_contatos(agenda):
    print("Lista de contatos: ")
    for indice, contato in enumerate(agenda):
        nome        = contato['nome']
        telefone    = contato['telefone']
        email       = contato['email']
        favorito    = "✅" if contato['favorito'] else "❌"

        print(f"Número do Contato [{indice+1}] Nome: {nome}. Telefone: {telefone}. Email: {email}. Favorito: {favorito}")

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
            adicionar_contato(agenda, nome, telefone, email)
        elif escolha == 2:
            listar_contatos(agenda)
        elif escolha == 6:
            break