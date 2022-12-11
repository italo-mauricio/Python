from datetime import date

'''
    Esse é um programinha básico para comparar datas de anivesário.


'''



def origem():
    
    # informo que dia é hoje
    data = date.today()
    print('Hoje é: {}'.format(data))

    while True:
        # peço que a pessoa digite seu aniversário

        dia_origem = int(input("Digite o dia do seu nascimento: "))
        mes_origem = int(input("Digite o mês do seu nascimento: "))
        ano_origem = int(input("Digite o ano do seu nascimento: "))

        # defino a data de hoje através da função today
        day = date.today().day
        month = date.today().month
        year = date.today().year

        # a idade eu faço o ano atual menos o ano origem
        age = year - ano_origem

        # agora eu faço a comparação, se o mês de origem e o dia origem forem iguais ao dia atual
        # então hoje é o seu aniversário, e digo quantos anos você tem

        if mes_origem == month and dia_origem == day:
            print('Você tem: {} anos'.format(age))
            print('Hoje é o seu aniversário')
        else:
            # se não, digo quantos anos você tem igualmente e digo que hoje não é seu aniversário
            print('Você tem {} anos'.format(age))
            print('Hoje não é o seu aniversário')
        
        # pergunto se o usuário deseja continuar
        conti = input("Deseja continuar verificando? [S/N] ")
        if conti == 'S':
            continue
        elif conti == 'N':
            print("Obrigado!")
            break;
        else:
            print("Opção inválida!")


origem()  # chamando a função


























