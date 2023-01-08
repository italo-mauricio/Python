'''

        Exercicio adicionando números numa lista sem permitir repetições


'''




num = []
som = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print("Valor adicionado com sucesso!")
          
    else:
        print("Valor duplicado")

    r = str(input("Deseja continuar?[s/N] "))
    if r in 'Nn':
        break

for i in num:
    soma_tudo = i + n
    som += soma_tudo



print(f"Você adicionou os seguintes valores: {num}")
print(f"A soma dos valores é de: {som}")