# Pedro Henrique Alves Guariente, RM550301
# Lucas Augusto Dutra Keller, RM551073
# David de Medeiros Pacheco Junior RM551462
# Orlando AKio Morii Cardoso, RM98067
# Kaique Maia Reis Silva, RM552112

# Criação de duas listas vazias, uma para compras e outra para estoque
compras = []
estoque = []

# Função para cadastrar uma nova compra
def cadastrar_compra():
    descricao = input("Descrição do produto: ")
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor unitário: "))

    # Adiciona a nova compra à lista de compras
    compras.append({"descrição": descricao, "quantidade": quantidade, "valor": valor})

# Função para cadastrar uma entrada no estoque
def cadastrar_entrada():
    descricao = input("Descrição do produto: ")
    quantidade = int(input("Quantidade: "))

    # Adiciona a nova entrada à lista de estoque
    estoque.append({"descrição": descricao, "quantidade": quantidade})

# Função para cadastrar uma saída do estoque (venda)
def cadastrar_saida():
    descricao = input("Descrição do produto: ")
    quantidade = int(input("Quantidade: "))

    # Verifica se a quantidade de saída é menor ou igual à quantidade em estoque
    for produto in estoque:
        if produto["descrição"] == descricao:
            if produto["quantidade"] >= quantidade:
                produto["quantidade"] -= quantidade

                # Caso a saída seja registrada com sucesso, encerra a função
                return
    
    # Caso não haja quantidade suficiente em estoque, exibe uma mensagem de erro
    print("Erro: quantidade insuficiente em estoque.")

# Função para exibir todas as compras registradas
def exibir_compras():
    print("Compras realizadas:")
    for compra in compras:
        print(f"Descrição: {compra['descrição']}, Quantidade: {compra['quantidade']}, Valor unitário: {compra['valor']}")

# Função para exibir todo o estoque atual
def exibir_estoque():
    print("Estoque atual:")
    for produto in estoque:
        print(f"Descrição: {produto['descrição']}, Quantidade: {produto['quantidade']}")

# Loop principal do programa
while True:
    print("Opções:")
    print("1 - Cadastrar nova compra")
    print("2 - Cadastrar nova entrada no estoque")
    print("3 - Cadastrar nova saída do estoque (venda)")
    print("4 - Exibir todas as compras")
    print("5 - Exibir todo o estoque")
    print("6 - Sair")

    opcao = int(input("Digite o número da opção desejada: "))

    # Utilização de estrutura Match-Case para escolher a função correspondente à opção escolhida
    match opcao:
        case 1:
            cadastrar_compra()
        case 2:
            cadastrar_entrada()
        case 3:
            cadastrar_saida()
        case 4:
            exibir_compras()
        case 5:
            exibir_estoque()
        case 6:
            # Encerra o loop e finaliza o programa
            print("Encerrando programa...")
            break
        case _:
            # Caso a opção escolhida não seja válida, exibe uma mensagem de erro
            print("Opção inválida. Digite um número de 1 a 6.")