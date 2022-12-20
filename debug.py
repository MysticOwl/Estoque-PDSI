from lib.estoque import *
empresa = Estoque("Coisa")

for i in range (0,5):
    algo = Produto()
    algo.setCodigo('{}'.format(i))
    algo.setNome("Camisa")
    algo.setUnidade(10)
    algo.setValor(12.99)
    empresa.adicionaProduto(algo)

venda_camisa = Venda()

venda_camisa.setCodigo('zxc')
venda_camisa.setProduto('0')
venda_camisa.setValor(19.99)

empresa.adicionaVenda(venda_camisa)

empresa.imprimeVenda()