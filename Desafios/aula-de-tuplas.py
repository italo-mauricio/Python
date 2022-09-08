from re import A


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
print(pessoa)