from lib import estoque,produto,venda

empresa = input("Digite o nome da empresa: ")

empresa = estoque.Estoque(empresa)

while True:
    print("1 - Estoque")
    print("2 - Produto")
    print("3 - Venda")
    print("0 - Sair")
    nav = input("Digite a opção desejada: ")
    if nav == '1':
        print("1 - Consultar lista de produto")
        print("2 - Consultar lista de vendas")
        print("3 - Sair")
        e_nav = input("Digite a opção desejada: ")
        if e_nav == '1':
            print(empresa.imprimeProduto())
            print("Estoque atual\n")
        elif e_nav == '2':
            empresa.imprimeVenda()
            print(empresa.imprimeVenda())
            print("Vendas Atuais\n")
        else:
            pass
    elif nav == '2':
        print("1 - Adicionar produto")
        print("2 - Consultar produto")
        print("3 - Remover produto")
        print("4 - Sair")
        p_nav = input("Digite a opção desejada: ")
        if p_nav == '1':
            prod = produto.Produto()
            prod.setNome(input("Digite o nome do produto: "))
            prod.setCodigo(input("Digite o código do produto: "))
            prod.setUnidade(int(input("Digite as unidades do produto: ")))
            prod.setValor(float(input("Digite o valor do produto: ")))
            empresa.adicionaProduto(prod)
        elif p_nav == '2':
            empresa.consultaProduto(str(input("Digite o codigo do produto: ")))
        elif p_nav == '3':
            empresa.removeProduto(str(input("Escreva o código do produto: ")))
    elif nav == 3:
        print("1 - Adicionar venda")
        print("2 - Consultar venda")
        print("3 - Remover venda")
        print("4 - Sair")
        v_nav = input("Digite a opção desejada: ")
    elif nav == '0':
        break
    else:
        print("Erro!")