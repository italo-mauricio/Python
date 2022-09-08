lanche = ('hamburguer', 'pizza', 'pudim')
# Tuplas são imutáveis
# exemplo {Lanche[1] = 'refrigerante' '} daria erro de syntax, pois tuplas são imutáveis
#for comida in lanche:
    #print(f'eu vou comer {comida}')
#print('comi muito')

#for cont in range(0, len(lanche)):
    #print(lanche[cont])
#print('comi muito')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche): # o Enumerate retorna tanto o dado, quanto a posição
    print(f'Eu vou comer {comida} na posição {pos}')

print ('comi pra caramba')