#Biblioteca local
from lib.produto import Produto
from lib.venda import Venda

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
        return str("Estoque da empresa: " + self.__empresa)

    def adicionaProduto(self,
                        elem=Produto()):
        '''Adiciona um produto dentro do estoque'''

        #Lista de atributos da classe Produto
        lista_atributos = [
            'nome','codigo',
            'unidade','valor'
        ]

        #Loop para setar os atributos do objeto elem
        for i in lista_atributos:
            if i == 'unidade':
                setattr(elem,
                        i,
                        int(input('{} do produto: '.format(i))))
            elif i == 'valor':
                setattr(elem,
                        i,
                        float(input('{} do produto: '.format(i))))
            else:
                setattr(elem,
                        i,
                        str(input('{} do produto: '.format(i))))

        #Adiciona o objeto na lista de produtos dentro do estoque
        self.__listaDeProdutos.append(elem)                
        return True

    def _verificaVenda(self,elem) -> bool:
        '''Função que indentifica se é possível \n
            Realizar a venda o produto'''
        venda = self.consultaProduto(elem.getProduto())

        if not(venda):
            return False
        
        if venda.getUnidade() <= 0:
            return False
        
        return True
    
    def adicionaVenda(self,venda):
        '''Adiciona uma venda dentro do estoque'''
        produto = self._verificaVenda(venda)
        if not(produto):
            return False
        return self.__listaDeVendas.append(venda)        

    def consultaProduto(self,elem):
        '''Consulta um produto dentro do estoque'''
        if self.isEmpty(self.__listaDeProdutos):
            return False
        for i in range(0, len(self.__listaDeProdutos)):
            if (self.__listaDeProdutos[i].getCodigo() == elem):
                return self.__listaDeProdutos[i]
            else:
                return False
    
    def consultaVenda(self,venda:str) -> str:
        '''Consulta um produto dentro do estoque'''
        if self.isEmpty(self.__listaDeVendas):
            return False
        for i in range(0,len(self.__listaDeVendas)):
            if (self.__listaDeVendas[i].getCodigo()==venda):
                return self.__listaDeVendas[i]
            else:
                return False
    
    def imprimeVenda(self) -> list:
        '''Função responsável por retornar a lista de vendas'''
        for i in self.__listaDeVendas:
            print(i)
    
    def imprimeProduto(self) -> list:
        '''Imprime a lista de produtos no estoque'''
        for i in self.__listaDeProdutos:
            print(i)
    
    def removeProduto(self,produto:str) -> bool:
        if self.isEmpty(self.__listaDeProdutos):
            return False
        self.__listaDeProdutos.pop(self.consultaProduto(produto))
        return True
    
    def removeVenda(self,venda:str) -> bool:
        if self.isEmpty(self.__listaDeVendas):
            return False
        self.__listaDeVendas.pop(self.__listaDeVendas.index(venda))