class Produto:
    def __init__(self, nome, codigo, unidade, valor):
        self.__nome = nome
        self.__codigo = codigo
        self.__unidade = unidade
        self.__valor = valor

    def __repr__(self) -> str:
        nome    = str(self.__nome)
        codigo  = str(self.__codigo)
        unidade = str(self.__unidade)
        valor   = str(self.__valor)
        return "Produto:{}, Codigo:{}, Valor:{}, Quantidade:{}".format(nome,codigo,valor,unidade)