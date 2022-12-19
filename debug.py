from lib.estoque import *
empresa = Estoque("Coisa")

algo = Produto()
algo.setNome("camisa")
algo.setCodigo('001')
algo.setUnidade(25)
algo.setValor(19)

algo2 = Produto()
algo2.setNome("camisa2")
algo2.setCodigo('002')
algo2.setUnidade(25)
algo2.setValor(19)

empresa.adicionaProduto(algo)

empresa.consultaProduto('001')