from datetime import datetime

class Produto:
    def __init__(self):
        self.__nome     = None
        self.__codigo   = None
        self.__unidade  = None
        self.__valor    = None
        self.__data     = datetime.today().strftime('%d-%m-%y')
        self.__hora     = datetime.today().strftime('%H:%M')

    def __repr__(self) -> str:
        nome    = str(self.__nome)
        codigo  = str(self.__codigo)
        unidade = str(self.__unidade)
        valor   = str(self.__valor)
        return str("Produto:{}, Codigo:{}, Valor:{}, Quantidade:{}".format(nome,codigo,valor,unidade))

    def adicionaPreco (self, preco):
        self.__valor = preco
        return True
    
    def getData(self):
        return "Data:{} Hora:{}".format(self.__data,self.__hora)

    def adicionaCodigo (self, codigo):
        self.__codigo = codigo
        return True
    
    def getNome(self):
        return self.__nome
    
    def getCodigo(self):
        return self.__codigo
    
    def getUnidade(self):
        return self.__unidade
    
    def getValor(self):
        return self.__valor

    def setNome(self, nome):
        self.__nome = nome
        return True

    def setCodigo(self, codigo):
        self.__codigo = codigo
        return True

    def setUnidade(self, unidade):
        self.__unidade = unidade
        return True

    def setValor(self, valor):
        self.__valor = valor
        return True