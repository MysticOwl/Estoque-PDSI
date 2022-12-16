from datetime import datetime

class Venda:
    def __init__(self, codigo):
        self.__codigo = codigo
        self.__data = datetime.today().strftime('%d-%m-%y')
        self.__hora = datetime.today().strftime('%H:%M')

    def __repr__(self):
        codigo = str(self.__codigo)
        data = str(self.__data)
        hora = str(self.__hora)
        return "Venda:{}, realizada em:{} as {}".format(codigo,data,hora)