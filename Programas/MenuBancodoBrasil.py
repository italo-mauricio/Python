import os



def menu():
    os.system("cls")
    print('''
    
        versaldo = 1
        empréstimo = 2
        atendimento = 3
        crédito = 4
        retornar = 5
        sal = 1250
    
    
    ''')
    usuario = int(input('Escolha entre uma das opções abaixo: '))
    

    if usuario == 1:
        versaldo = int(input('Informe o seu saldo: '))
        print('Seu saldo é de R${:.1f} reais'.format(versaldo))
        input("Press enter to continue")
    if usuario == 2:
        emprestimo = str(input('Você deseja um empréstimo: ')).upper()
        if emprestimo == 'Sim'.upper():
            s = str(input('Perfeito, agora preciso saber para qual finalidade vai o dinheiro: '))
            casa = int(input('De quanto você precisa: '))
            ano = int(input('Okay, agora informe em quantos anos você pretende pagar: '))
            sal2 = int(input('Okay, agora informe o seu salário: '))
            parcelas = (casa / ano) / 12
            if parcelas > sal2 + (30 / 100):
                print('Empréstimo negado')
                input("Press enter to continue")
            else:
                print('Empréstimo concedido!')
                print('A parcela do seu empréstimo é de {:.2f}R$ ao mês!'.format(parcelas))
                input("Press enter to continue")
        elif emprestimo == 'Não'.upper():
            print('Okay, retorne ao menu principal!')
            input("Press enter to continue")

    if usuario == 3:
        print('Já iremos lhe atender, aguarde um minuto!')
        input("Press enter to continue")

    if usuario == 4:
        c = int(input('Quanto de crédito o senhor deseja: '))
        sal2 = int(input('Okay, agora informe o seu salário: '))
        if c > sal2 + (30 / 190):
            print('Crédito negado, seus ganhos são incompátiveis com seu pedido!')
            input("Press enter to continue")
        else:
            print('Crédito concedido!')
            input("Press enter to continue")
    if usuario == 5:
        print('Retore ao menu principal!')
        
            
        
        


while True:
    os.system("cls")
    print('''

            | -------------- Bem vindo(a) ao Banco do Brasil! ---------------- |
            | ================================================================ |
            |                     1 - Empréstimo                               |
            |                     2 - Saldo                                    |
            |                     3 - Sair                                     |
            | ================================================================ |
    ''')
    cliente = ' '
    cliente = input("Escolha uma opção: ")
    if cliente == '1':
        menu()
    elif cliente == '2':
        print("oi")
    elif cliente == '3':
        print("Obrigado volte sempre!")
        break
    else:
        print("Opção inválida")

