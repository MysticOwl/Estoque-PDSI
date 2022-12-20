from datetime import datetime

class Venda:
    def __init__(self) -> vars:
        '''Construção da classe venda com os parâmentros \n
            Codigo; Valor; Codigo do produto'''
        self.__codigo   = None
        self.__valor    = None
        self.__produto  = None
        self.__data     = datetime.today().strftime('%d-%m-%y')
        self.__hora     = datetime.today().strftime('%H:%M')

    def __repr__(self):
        codigo = str(self.__codigo)
        valor = str(self.__valor)
        produto = str(self.__produto)
        data = str(self.__data)
        hora = str(self.__hora)
        return "Venda:{} Valor:{} Codigo do produto:{}, realizada em:{} as {}".format(codigo,valor,produto,data,hora)

    def setCodigo(self,elem:str) -> str:
        '''Insere o valor código da venda'''
        self.__codigo = elem
        pass

    def setValor(self,elem:float) -> float:
        '''Insere o valor valor da venda'''
        self.__valor = elem
        pass

    def setProduto(self,elem:str) -> str:
        '''Insere o valor produto da venda'''
        self.__produto = elem
        pass

    def getCodigo(self):
        '''Retorna o codigo da venda'''
        return self.__codigo

    def getValor(self):
        '''Retorna o valor da venda'''
        return self.__valor
    
    def getProduto(self):
        '''Retorna o codigo da venda do produto'''
        return self.__produto