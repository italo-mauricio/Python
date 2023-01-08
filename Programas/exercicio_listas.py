'''
        Exercicio de maior e menor valor numa lista

'''


num = []
maior = 0
menor = 0
for i in range(0, 5):
    num.append(int(input(f"Digite um valor na posição {i}: ")))
    if i == 0:
            maior = menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]

print(f'''

    Os valores digitados foram {num}
    O maior valor foi {maior}
    O menor valor foi {menor}

''')

for i, v in enumerate(num):
    if v == maior:
        print(f"O maior valor apareceu posição {i}")
    if v == menor:
        print(f"O menor valor apareceu na posição {i}")