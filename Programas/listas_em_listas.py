'''

Aqui vemos o conceito de listas dentro de listas


'''

dados = []
dados.append('pedro')
dados.append('25')
pessoas = list()
pessoas.append(dados[:])   # <---   usando esse método, podemos adicionar uma lista, dentro de outra lista
pessoas = [['pedro', 25], ['maria', 24], ['italo', 18]]  # posso adicionar mais elementos nessa lista, desta maneira
for i in pessoas:
    print(f'{i[0]} tem {i[1]} de idade')

print(pessoas)


amigos = []
dados = []
total_maior_idade = total_menor_idade = 0

for c in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(str(input("Idade: ")))
    amigos.append(dados[:])
    dados.clear()
print(amigos)

for p in amigos:
    if p[1] >= '21':
        print(f'{p[0]} é maior de idade.')
        total_maior_idade+=1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor_idade+=1
 
print(f'Temos {total_maior_idade} maiores e {total_menor_idade} menos de idade')