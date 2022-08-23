from main import *


def insert(dictionary):
    dictionary[input("Insira o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite o último acesso: "),
                                                     input("Digite o último setor: ").upper()]


def find(dictionary=None):
    user = input("Digite um user para pesquisa: ")
    if dictionary is None:
        dictionary = {}
    if dictionary.__contains__(user):
        print(dictionary.get(user))


def exclude(user, dictionary=None):
    if dictionary is None:
        dictionary = {}
    if dictionary.__contains__(user):
        dictionary.pop(user)
    else:
        print("Usuário não encontrado!")


def login(user, dictionary=None):
    if dictionary is None:
        dictionary = {}
    if dictionary.__contains__(user):
        print("Bem vindo! Você está logado!")
        return True
    else:
        print("Usuário não encontrado!")
        return False


def list_all(dictionary):
    for key, values in dictionary.items():
        print(f"{key} : {[print(i) for i in values]}\n")


def ask(dictionary):
    """ Asks an existing user to manage data """
    user = input("Login: ").upper()
    if dictionary.__contains__(user):
        option = menu()
        while option == "I" or option == "P" or option == "E" or option == "L" or option == "LL":
            if option == "I":
                insert(dictionary)

            elif option == "P":
                find(dictionary)

            elif option == "E":
                exclude(dictionary)

            elif option == "L":
                user = input("Insira o nome de usuário: ").upper()
                login(user, dictionary)

            elif option == "LL":
                list_all(dictionary)

            option = menu()
    else:
        print("Usuário não encontrado!")


def menu():
    option = input("Escolha uma opção: \n"
                   "\"I\" para Inserir \n  "
                   "\"P\" para Pesquisar \n"
                   "\"E\" para Excluir \n "
                   "\"L\" para Logar \n"
                   "\"LL\" para Listar Todos ")
    return option
