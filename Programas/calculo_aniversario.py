from datetime import date

'''
    Esse é um programinha básico para comparar datas de anivesário.

    Ele pede que você coloque o dia, o mês e o seu ano de nascimento, e faz as verificações necessárias
    para obter sua idade atual, quantos dias fazem que você nasceu e se é ou não seu aniversário hoje.

'''


def numOfDays(date1, date2):
    return (date2-date1).days
    '''
        Essa função pega o dia do seu aniversário e subtrai pelo dia atual, capturado peo "days" 
     
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


        # aqui é aplicada a função para verificar os dias que você nasceu.
        date1 = date(ano_origem, mes_origem, dia_origem)
        date2 = date(year, day, month)
        print("\nVocê nasceu a exatamente: ")
        print(numOfDays(date1, date2), "dias")
                
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


























