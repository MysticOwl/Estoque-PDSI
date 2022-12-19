from lib.estoque import *
empresa = Estoque("Coisa")

algo = Produto()
algo.setNome("camisa")
algo.setCodigo('001')
algo.setUnidade(25)
algo.setValor(19.23)

venda = Venda()
venda.setCodigo('xyz')
venda.setValor(19.20)
venda.setProduto('001')


empresa.adicionaProduto(algo)
empresa.adicionaVenda(venda)

print(empresa.consultaProduto('001'))
print(empresa.consultaVenda('xyz'))