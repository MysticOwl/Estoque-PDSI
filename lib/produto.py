from datetime import datetime

class Produto:
    def __init__(self) -> object:
        '''Retorna o objeto produto com os parâmetros \n
        nome:str, codigo:str, unidade:int, valor:float'''
        self.nome     = str
        self.codigo   = str
        self.unidade  = int
        self.valor    = float
        self.devolve  = False
        self.data     = datetime.today().strftime('%d-%m-%y')
        self.hora     = datetime.today().strftime('%H:%M')

    def __repr__(self) -> str:
        nome    = str(self.nome)
        codigo  = str(self.codigo)
        unidade = str(self.unidade)
        valor   = str(self.valor)
        return str("Produto:{}, Codigo:{}, Valor:{}, Quantidade:{}".format(nome,codigo,valor,unidade))