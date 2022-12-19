from datetime import datetime

class Produto:
    def __init__(self):
        self.__nome     = str
        self.__codigo   = str
        self.__unidade  = int
        self.__valor    = float
        self.__devolve  = False
        self.__data     = datetime.today().strftime('%d-%m-%y')
        self.__hora     = datetime.today().strftime('%H:%M')

    def __repr__(self) -> str:
        nome    = str(self.__nome)
        codigo  = str(self.__codigo)
        unidade = str(self.__unidade)
        valor   = str(self.__valor)
        return str("Produto:{}, Codigo:{}, Valor:{}, Quantidade:{}".format(nome,codigo,valor,unidade))
    
    def getData(self):
        '''Retorna a data em que o produto foi registrado'''
        return "Data:{} Hora:{}".format(self.__data,self.__hora)
    
    def getNome(self):
        '''Retorna o nome do produto'''
        return self.__nome
    
    def getCodigo(self):
        '''Retorna o código do produto'''
        return self.__codigo
    
    def getUnidade(self):
        '''Retorna a quantidade do produto'''
        return self.__unidade
    
    def getValor(self):
        '''Retorna o valor do produto'''
        return self.__valor
    
    def getDevolve(self):
        '''Retorna se o produto foi devolvido ou não'''
        return self.__devolve

    def setNome(self, nome:str):
        '''Insere o nome do produto'''
        self.__nome = nome
        return True

    def setCodigo(self, codigo:str):
        '''Insere o codigo do produto'''
        self.__codigo = codigo
        return True

    def setUnidade(self, unidade:int):
        '''Insere a quantidade de produto'''
        self.__unidade = unidade
        return True

    def setValor(self, valor:float):
        '''Insere o valor do produto'''
        self.__valor = float(valor)
        return True

    def setDevolve(self):
        '''Muda o estado de devolução do produto'''
        self.__devolve = True
        return True