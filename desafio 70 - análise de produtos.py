from validacoes import *
# Código precisando de manuntenção!


total = totmil = menor = 0
'''def isnumber(value):
    try:
        float(value)
        int (value)
    except ValueError:
        str(value)
        return False
    return True'''


while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    cont = 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f"O total da compra foi de R${total:.2f}")
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato custa R${menor:.2f}')