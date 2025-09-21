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
def listar_contatos(agenda, filtrar_favorito = False):
    print("\nLista de contatos: ")
    existe_favoritos = False
    for indice, contato in enumerate(agenda):
        nome        = contato['nome']
        telefone    = contato['telefone']
        email       = contato['email']
        favorito    = "✅" if contato['favorito'] else "❌"
        if filtrar_favorito and not contato['favorito']:
            continue
        else:
            existe_favoritos = True
        print(f"Índice [{indice+1}] - Nome: {nome}. Telefone: {telefone}. Email: {email}. Favorito: {favorito}")
    if not existe_favoritos:
        print("⚠️  Não há contatos como favoritos.")

# Editar contato
def editar_contato(agenda, nome, telefone, email, favorito, indice):
    if indice >= 0 and indice < len(agenda):
        agenda[indice]["nome"] = nome if nome else agenda[indice]["nome"]
        agenda[indice]["telefone"] = telefone if telefone else agenda[indice]["telefone"]
        agenda[indice]["email"] = email if email else agenda[indice]["email"]
        agenda[indice]["favorito"] = favorito
        print("🔄️  Contato atualizado.")
    else:
        print("⚠️  Índice de contato inválido.")        

# Marcar/Desmarcar contato favorito
def marcar_desmarcar_favorito(agenda, indice, favorito):
    if indice >= 0 and indice < len(agenda):
        agenda[indice]["favorito"] = favorito
        mensagem = "✅  Contato marcado como favorito." if favorito else "❌  Contato marcado como não favorito."
        print(mensagem)
    else:
        print("⚠️  Índice de contato inválido.") 

# Apagar contato
def apagar_contato(agenda, indice):
    if indice >= 0 and indice < len(agenda):
        confirmacao = input(f"Deseja realmente remover este contato: {agenda[indice]['nome']} (s/n)")
        if confirmacao == "s":
            agenda.pop(indice)
            print("⛔  Contato removido.")
        else:
            print("🔄️  Contato mantido.")

# Mostrar menu de opções
def mostrar_menu():
    print("\nAgenda de Contatos")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contato")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato favorito")
    print("5. Listar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

def existe_contato(agenda):
    if not len(agenda) > 0:
        print("⚠️  Não há nenhum contato na agenda")
        return False
    return True

# Limpar tela - cls para windows e clear para linux
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    # Menu de opções
    mostrar_menu()
    try:
        escolha = int(input("Informe o número de sua escolha: "))

        limpar_tela()

        # Pula iteração caso a escolha não seja 1 ou 7 e não exista contato na agenda
        if not escolha in (1,7) and not existe_contato(agenda): continue

        if escolha == 1:
            print("\nAdicionando contato")
            nome        = input("Informe um nome*: ")
            telefone    = input("Informe número de telefone*: ")
            email       = input("Informe um e-mail: ")
            adicionar_contato(agenda, nome, telefone, email)
        elif escolha == 2:
            listar_contatos(agenda)
        elif escolha == 3:
            listar_contatos(agenda)
            print("\nAtualizando contato")
            indice      = input("Informe o índice do contato: ")
            nome        = input("Informe nome atualizado (Deixe em branco para manter): ")
            telefone    = input("Informe telefone atualizado (Deixe em branco para manter): ")
            email       = input("Informe email atualizado (Deixe em branco para manter): ")
            favorito    = input("Favoritar contato? (s/n): ")
            editar_contato(agenda, nome, telefone, email, True if favorito == "s" else False, int(indice)-1)
        elif escolha == 4:
            listar_contatos(agenda)
            print("\nMarcar/desmarcar contato favorito")
            indice      = input("Informe o índice do contato: ")
            favorito    = input("Favoritar contato? (s/n): ")
            marcar_desmarcar_favorito(agenda, int(indice)-1, True if favorito == "s" else False)
        elif escolha == 5:
            listar_contatos(agenda, True)
        elif escolha == 6:
            listar_contatos(agenda)
            indice = input("\nInforme o índice do contato que deseja remover: ")
            apagar_contato(agenda, int(indice)-1)
        elif escolha == 7:
            print("⏹️  Programa finalizado.")
            break
    except Exception as e:
        limpar_tela()
        print("❌  Falha ao tentar executar a operação.")