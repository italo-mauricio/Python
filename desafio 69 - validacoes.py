from validacoes import *
total18 = totalh = totalm = 0
while True:
    idade = input("Digite a sua idade: ")
    if validnum(idade):
        sexo = ' '
        while sexo not in "MF":
            sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if idade >= '18':
            total18 += 1
        if sexo == 'M':
            totalh += 1
        if sexo == 'F' and idade < '20':
            totalm += 1
        resp = ' '
        while resp not in "SN":
            resp = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
        if resp == 'N':
            break
    else:
        print("Idade inválida")
print(f"O total de pessoas com mais de 18 anos é de {total18}")
print(f"O total de homens com mais de 18 anos é de {totalh}")
print(f'O total de mulheres com menos de 20 anos é de {totalm}')