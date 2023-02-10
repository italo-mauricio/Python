'''

Aqui vemos o conceito de listas dentro de listas


'''

dados = []
dados.append('pedro')
dados.append('25')
pessoas = list()
pessoas.append(dados[:])   # <---   usando esse método, podemos adicionar uma lista, dentro de outra lista
pessoas = [['pedro, 25', ['maria, 24']], ['italo, 18']]  # posso adicionar mais elementos nessa lista, desta maneira

print(pessoas)