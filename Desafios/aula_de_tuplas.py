from re import A

'''
    Aqui temos uma pequena aula sobre Tuplas, que servem para armazenar dados e trabalhar com eles.
    vemos bem exemplificado como funcionam, sempre com parênteses () para defirnirlas. 

    Uma característica muito importante das tuplas é que elas são imutáveis, ou seja, uma vez definida
    elas não podem ser alteradas. Porém, tuplas podem ter objetos mutáveis como listas por exemplo




'''
# exemplo de tuplas com objetos mutáveis

minha_tupla = ([1,2,3,4], ['a', 'b', 'c'])
print(minha_tupla)
minha_tupla[0].append(10)
print(minha_tupla)

'''
    No exemplo acima vemos uma tupla com uma lista dentro. As listas que estão entre colchetes []
    são mutáveis, na linha abaixo "minha_tupla[0].append(10)" eu uso o método append, para inserir um novo
    número elemento na tupla. no caso o "10".

'''





lanche = ('hamburguer', 'pizza', 'pudim')
# Tuplas são imutáveis
# exemplo {Lanche[1] = 'refrigerante' '} daria erro de syntax, pois tuplas são imutáveis
for comida in lanche:
    print(f'eu vou comer {comida}')
print('comi muito')

for cont in range(0, len(lanche)):
    print(lanche[cont])
print('comi muito')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche): # o Enumerate retorna tanto o dado, quanto a posição
    print(f'Eu vou comer {comida} na posição {pos}')

print ('comi pra caramba')



# trabalhando com index

a = (2, 3, 4, 5, 6)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1)) 

# posso ter dados de tipos diferentes nas tuplas

#exemplo:

pessoa = ('gustavo', 39, 'M', 89.9)
del(pessoa) # podemos usar o del para apagar a tupla e não posso deletar somend 1 elemento da tupla, tenho que deletar ela por inteira.
print(pessoa)  # no seu programa irá retornar um erro, pois "pessoa" já não existe mais.