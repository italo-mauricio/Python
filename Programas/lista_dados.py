lista = []

while True:
    num = int(input('Digite um valor: '))
    num.append(lista)
    print("Número adicionado com sucesso!")

    conti = str(input("Deseja continuar?[s/N] "))
    if conti in 'Nn':
        break

print(f"Foram digitados {len(lista)} números ")
