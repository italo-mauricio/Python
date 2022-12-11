'''
    Neste exercício temos uma pequena análise de dados usando tuplas


    1 - pegamos quatro valores diferentes através do input
    2 - mostramos na tela  os números digitados em uma tupla
    3 - através da função "count" contamos para contar quantas vezes você digitou determinado valor
    4 - fazemos um if para ver quantas vezes  o 3 apareceu na posição determinada, utilizando
    {num.index(3)+1}.
    5 = fazemos um for para verificar os números pares digitados


    Esse exemplo é só uma pequena amostra de como analisar os dados em uma tupla.

'''

#tupla
num = (int(input("Digite um número: ")),     
       int(input("Digite outro número: ")),
       int(input("Digite um terceiro número: ")),
       int(input("Digite o quarto número: ")))

print(f"Você digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1} posição") # evita que o código quebre quando o 3 não for digitado
else:
    print("O número 3 não apareceu nenhuma vez")
print('Os valores pares digitados foram', end='')
for n in num:  # irá verificar quantos números pares existem
    if n % 2 == 0:
        print(n, end='')