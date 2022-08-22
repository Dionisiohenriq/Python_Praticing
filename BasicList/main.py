# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from inventario_funcoes import *


def main():
    inventario_produtos = cadastro()
    lista(inventario_produtos)
    pesquisa(inventario_produtos)
    depreciacao(inventario_produtos)
    remover(inventario_produtos)
    lista(inventario_produtos)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
