bar = "+----------+---------+---------+"
def menuPrincipal():
    #Top bar
    print(bar)
    
def menuAlteraProduto() -> str:
    '''Função para alteração de produto'''
    
    #Menu de opções para a alteração do produto
    while True:
        print("\n"+bar)
        print("|            OPÇÕES            |")
        print("|    1- Alterar nome           |")
        print("|    2- Alterar codigo         |")
        print("|    3- Alterar unidade        |")
        print("|    4- Alterar valor          |")
        print("|    0- Sair                   |")
        print(bar)
        opcao = input("\nDigite sua opção: ")
        
        #Verificação se a opção está correta
        if int(opcao) < 0 or int(opcao) > 4:

            print("\nOpção inválida!")

            return menuAlteraProduto()

        #Retorna o valor da opção desejada    
        return opcao