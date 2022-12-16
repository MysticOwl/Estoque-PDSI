import produto,venda

class Estoque:
    def __init__(self,nome:str) -> any:
        '''Criação do estoque  com o parâmetro nome como obrigatório'''
        self.__empresa = nome
        self.__listaDeProdutos = []
        self.__listaDeVendas = []

    def isEmpty(self,elem:str):
        '''Verifica se a lista (elem) está vazia'''
        if len(elem) <= 0:
            return True
        return False

    def __repr__(self) -> str:
        return "Estoque da empresa: " + self.__empresa

    def adicionaProduto(self,produto:str):
        '''Adiciona um produto dentro do estoque'''
        self.__listaDeProdutos.append(produto)
        return True
    
    def adicionaVenda(self,venda:str):
        '''Adiciona uma venda dentro do estoque'''
        self.__listaDeVendas.append(venda)
        return True
    
    def consultaProduto(self,produto:str) -> str:
        '''Consulta um produto dentro do estoque'''
        if self.isEmpty(self.__listaDeProdutos):
            return False
        index = self.__listaDeProdutos.index(produto)
        return self.__listaDeProdutos[index]
    
    def consultaVenda(self,venda:str) -> str:
        '''Consulta um produto dentro do estoque'''
        if self.isEmpty(self.__listaDeVendas):
            return False
        index = self.__listaDeVendas.index(venda)
        return self.__listaDeVendas[index]
    
    def imprimeVenda(self) -> list:
        return self.__listaDeVendas
    
    def imprimeProduto(self) -> list:
        return self.__listaDeProdutos
    
    def removeProduto(self,produto:str) -> bool:
        if self.isEmpty(self.__listaDeProdutos):
            return False
        self.__listaDeProdutos.pop(self.__listaDeProdutos.index(produto))
        return True
    
    def removeVenda(self,venda:str) -> bool:
        if self.isEmpty(self.__listaDeVendas):
            return False
        self.__listaDeVendas.pop(self.__listaDeVendas.index(venda))