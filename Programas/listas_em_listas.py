'''

Aqui vemos o conceito de listas dentro de listas


'''



dados = []
dados.append('pedro')
dados.append('25')
pessoas = list()
pessoas.append(dados[:])   # <---   usando esse método, podemos adicionar uma lista, dentro de outra lista

print(pessoas)