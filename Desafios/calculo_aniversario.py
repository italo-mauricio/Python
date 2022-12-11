from datetime import date

'''
    Esse é um programinha básico para comparar datas de anives




'''



def origem():

    data = date.today()
    print('Hoje é: {}'.format(data))

    while True:

        dia_origem = int(input("Digite o dia do seu nascimento: "))
        mes_origem = int(input("Digite o mês do seu nascimento: "))
        ano_origem = int(input("Digite o ano do seu nascimento: "))

        day = date.today().day
        month = date.today().month
        year = date.today().year
        age = year - ano_origem
        if mes_origem == month and dia_origem == day:
            print('Você tem: {} anos'.format(age))
            print('Hoje é o seu aniversário')
        else:
            print('Você tem {} anos'.format(age))
            print('Hoje não é o seu aniversário')
        
        conti = input("Deseja continuar verificando? [S/N] ")
        if conti == 'S':
            continue
        elif conti == 'N':
            print("Obrigado!")
            break;
        else:
            print("Opção inválida!")


origem()  # chamando a função


























