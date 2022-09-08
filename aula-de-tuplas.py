lanche = ('hamburguer', 'pizza', 'pudim')
# Tuplas são imutáveis
# exemplo {Lanche[1] = 'refrigerante' '} daria erro de syntax, pois tuplas são imutáveis
for comida in lanche:
    print(f'eu vou comer {comida}')
print('comi muito')