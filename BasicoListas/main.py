# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    inventario_produtos = []
    resposta = "S"
    while resposta == "S":
        inventario_produtos.append(input("Nome do produto: "))
        inventario_produtos.append(input("Valor do produto: "))
        inventario_produtos.append(input("Número de série: "))
        resposta = input("Inserir outro produto? ").upper()

    for produto in inventario_produtos: print(produto)
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
