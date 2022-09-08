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