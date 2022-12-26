#Biblioteca local
from lib.produto import Produto
from lib.venda import Venda
from lib.menu import *

class Estoque:
    def __init__(self,nome:str) -> any:
        '''Criação do estoque  com o parâmetro nome como obrigatório'''
        self.empresa = nome
        #Lista de atributos da classe Produto
        self.lista_atributos = [
            'nome','codigo',
            'unidade','valor'
        ]
        self.lista_de_produtos = []
        self.lista_de_vendas = []

    def isEmpty(self,elem) -> bool:
        '''Verifica se a lista (elem) está vazia'''
        if len(elem) <= 0:
            return True
        return False

    def __repr__(self) -> str:
        return str("Estoque da empresa: " + self.empresa)

    def _setAtributo(self,elem) -> object:

        #Loop para setar os atributos do objeto elem
        for i in self.lista_atributos:
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
                        str(input('{} do produto: '.format(i))).lower())
    
    def adicionaProduto(self):
        '''Adiciona um produto dentro do estoque'''

        #Cria o objeto Produto e armazena na variável elem
        elem=Produto()

        #Função para setar os atributos do objeto
        self._setAtributo(elem)

        #Adiciona o objeto na lista de produtos dentro do estoque
        self.lista_de_produtos.append(elem)  

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

        return self.lista_de_vendas.append(venda)        

    def consultaProduto(self,busca:str.lower,elem):     

        '''Consulta um produto dentro do estoque'''

        if (self.isEmpty(self.lista_de_produtos) or
            not(busca in self.lista_atributos)):

            return False
        
        #Lista que retorna os resultados da pesquisa
        resultado_consulta = []

        #Laço de repetição retornar todos os campos que corespondem ao elemento requisitado
        for i in self.lista_de_produtos:

            if getattr(i,busca) == elem:
                resultado_consulta.append(i)
                
            else:
                return False

        return resultado_consulta
    
    def alteraProduto(self,elem) -> bool:
        '''Função que altera o produto consultando o código'''
        if not(self.consultaProduto('codigo',elem)):
            return False
        
        elem = self.consultaProduto('codigo',elem)
        print("Produto selecioando:")
        print(elem)

        atributo = int(menuAlteraProduto())-1

        setattr(elem,
                self.lista_atributos[atributo],
                )

        return
        
    
    def consultaVenda(self,venda:str) -> str:
        '''Consulta um produto dentro do estoque'''
        if self.isEmpty(self.lista_de_vendas):
            return False
        for i in range(0,len(self.lista_de_vendas)):
            if (self.lista_de_vendas[i].codigo()==venda):
                return self.lista_de_vendas[i]
            else:
                return False
    
    def imprimeVenda(self) -> list:
        '''Função responsável por retornar a lista de vendas'''
        for i in self.lista_de_vendas:
            print(i)
    
    def imprimeProduto(self) -> list:
        '''Imprime a lista de produtos no estoque'''
        for i in self.lista_de_produtos:
            print(i)
    
    def removeProduto(self,produto:str) -> bool:
        if self.isEmpty(self.lista_de_produtos):
            return False
        self.lista_de_produtos.pop(self.consultaProduto(produto))
        return True
    
    def removeVenda(self,venda:str) -> bool:
        if self.isEmpty(self.lista_de_vendas):
            return False
        self.lista_de_vendas.pop(self.lista_de_vendas.index(venda))

    def debug(self,e):
        if e in self.lista_atributos:
            return True
        return False