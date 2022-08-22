# funções
def cadastro():
    resposta = "S"
    inventario_produtos = []
    while resposta == "S":
        inventario_produtos = [(input("Nome do produto: "),
                                float(input("Valor: ")),
                               input("Numero de série: "),
                               input("Departamento: "))]
        resposta = input("Deseja cadastrar outro produto? \"S\"?")
    return inventario_produtos


def lista(inventario_produtos):
    for produto in range(0, len(inventario_produtos)):
        print(f"Nome: {inventario_produtos[produto][0]}")
        print(f"Valor: {inventario_produtos[produto][1]}")
        print(f"Serial: {inventario_produtos[produto][2]}")
        print(f"Departamento: {inventario_produtos[produto][3]}")


def remover(inventario_produtos):
    # remoção de um equipamento
    busca = input("Insira o nome do produto a ser excluído: ")
    if inventario_produtos.index(busca):
        inventario_produtos.remove(busca)


def depreciacao(inventario_produtos):
    # depreciação do equipamento
    busca = int(input("Insira o número do produto a ser depreciado: "))
    if len(inventario_produtos) >= busca:
        print(inventario_produtos[busca])
        inventario_produtos[busca][1] *= 0.9
        print(inventario_produtos[busca])



def pesquisa(inventario_produtos):
    # busca por equipamento pelo índice do array ( ordem em que foi inserido )
    busca = int(input("Insira o número do produto a ser encontrado: "))
    if len(inventario_produtos) >= busca:
        print(inventario_produtos[busca])
    else:
        print("Produto não encontrado!")
