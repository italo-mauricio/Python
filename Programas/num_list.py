num = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print("Valor adicionado com sucesso!")
        input("Pressione qualquer tecla para continuar...")
        break   
    else:
        print("Valor duplicado")

    r = str(input("Deseja continuar?[s/N] "))

    if r in 'Nn':
        break