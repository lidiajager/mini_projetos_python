from pprint import pprint

estoque = []

def adicionar_produto():
    try:
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        unidade = input("Digite o unidade: ")
        preco = float(input("Digite o preço R$: "))
        novo_produto = {
            'nome': nome,
            'quantidade': quantidade,
            'unidade': unidade,
            'preco': preco
        }
    except ValueError:
        print("Erro de digitação.Tente novamente")
        return
    estoque.append(novo_produto)
    print(f"\n✅ Produto '{nome}' adicionado com sucesso!")

def listar_produto():
    for i in estoque:
     print(i['nome'])

def vender_produto(nome, quantidade):

  for i in estoque:
    if i["nome"] == nome:
        print (f"Produto encontrado no cadastro, com a quantidade: {i['quantidade']}")
        i["quantidade"] = i["quantidade"] - quantidade
        print(f"Sobrou {i['quantidade']} do produto no estoque")
        if i["quantidade"] < 0:
            i["quantidade"] = 0
            print("Acabou esse produto")


def gerar_relatorio():
    pprint(estoque)

# Menu principal
while True:
    print('\n___Menu de operações____')
    print("[ 1 ] Adicionar produto")
    print("[ 2 ] Listar produtos")
    print("[ 3 ] Vender produto")
    print("[ 4 ] Gerar relatório")
    print("[ 5 ] Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        vender_produto(nome, quantidade)
    elif opcao == 4:
        gerar_relatorio()
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")





