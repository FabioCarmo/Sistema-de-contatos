# Programa de contatos que adiciona, remove e lista contatos
# Autor: Fabio Goncalves
# Data: 26-04-25 // Versao Final 1.1

#importar biblioteca time 
import time

contatos = {} # Dicionario para armazenar os contatos 

# Funcoes para adicionar, remover, listar e editar contatos
def exibir_menu():
    print("Sistema de contatos")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Listar contatos")
    print("4 - Editar contato")
    print("0 - Sair")

def adicionar_contato(nome, tel):
    if (len(nome) == 0 or len(tel) == 0):
        return print("Necessario informar os dados corretamente!\n")
    else:
        if (nome in contatos):
            return print("Contato ja existe!\n")
        else:
            # Cria um indice na variavel contatos com o nome do contato e adiciona os dados ao dicionario
            contatos[nome] = {
                "Nome": nome,
                "Telefone": tel
            }
            return print(f"O Contato de {nome} foi adicionado com sucesso! \n")   

def remover_contato(nome):
    if (len(nome) == 0):
        return print("Necessario informar o nome do contato!\n")
    elif (nome not in contatos):
        return print("Contato nao encontrado!\n")
    else:
        # Remove o contato no dicionario pelo nome do indice informado
        del contatos[nome]
        return print(f"O contato {nome} foi removido com sucesso!\n")

def listar_contato():
    print("Lista de contatos: ")
    if (contatos == {}):
        return print("Nenhum contato encontrado!\n")
    else:  
        for indice, (chave, contato) in enumerate(contatos.items()):
            print(f"{indice} - Nome: {contato['Nome']} - Telefone: {contato['Telefone']}\n")

def editar_contato(nome_edit, novo_nome, novo_tel):
    if (len(novo_nome) == 0 or len(novo_tel) == 0 or len(nome_edit) == 0):
        return print("Necessario informar os dados corretamente!\n")
    elif (nome_edit not in contatos):
        return print("Contato nao encontrado!\n")
    else:
        # Atualiza o contato no dicionario pelo nome do indice informado
        contatos[nome_edit] = {
            "Nome": novo_nome,
            "Telefone": novo_tel
        }
        return print(f"O contato {nome} foi editado com sucesso!\n")

# Loop principal para manter as opcoes do menu e executar as funcoes
while True:
    exibir_menu()
    escolha_opcao = input("Escolha uma opcao: ")

    if (escolha_opcao == "1"):
        nome_contato = input("Digite o nome do contato: ")
        tel_contato = input("Digite o telefone do contato: ")
        adicionar_contato(nome_contato, tel_contato)
        time.sleep(1)
    elif (escolha_opcao == "2"):
        nome_remocao = input("Digite o nome do contato a ser removido: ")
        remover_contato(nome_remocao)
        time.sleep(1)
    elif (escolha_opcao == "3"):
        listar_contato()
        time.sleep(1)
    elif (escolha_opcao == "4"):
        nome_editar = input("Digite o nome do contato a ser editado: ")
        time.sleep(1)
        nome_editado = input("Digite o novo nome do contato:")
        tel_editado = input("Digite o novo telefone do contato:")
        editar_contato(nome_editar, nome_editado, tel_editado)
        time.sleep(1)
    elif (escolha_opcao == "0"):
        print("Saindo do sistema de contatos...")
        time.sleep(2)
        break
    else:
        print("Opção invalida. Tente novamente")