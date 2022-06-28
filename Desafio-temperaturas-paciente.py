
from time import sleep
usuario = ''


print('''Bem vindo(a) ao Hospital Regional de Caicó
=====================================================  
========= Aferir sua temperatura [1] ================
========= Sair [2] ==================================
=====================================================
''')  #menuzinho pq eu gosto

tempdia = []     #temperatura do ambiente
tempi = []     #temperatura do usuário
hora = []      #hora que foi medido

enfermeira = input('Escolha uma opção: ') #enfermeira irá colocar a temperatura que foi medico

if enfermeira == '1':
        print(""" Você escolheu aferir a sua temperatura
        Por favor siga a instrução abaixo!""")
        
        for i in range (0, 8):
            tempi.append(float(input('Digite uma temperatura em graus: ')))
            hora.append(int(input(f"Digite a hora que a temperatura {tempi[i]} foi aferida: ")))

        print(f"""Suas temperaturas foram:
        ==============================================
        ======== {tempi[0]} em {hora[0]}hrs ==========
        ======== {tempi[1]} em {hora[1]}hrs ==========
        ======== {tempi[2]} em {hora[2]}hrs ==========
        ======== {tempi[3]} em {hora[3]}hrs ==========
        ======== {tempi[4]} em {hora[4]}hrs ==========
        ======== {tempi[5]} em {hora[5]}hrs ==========
        ======== {tempi[6]} em {hora[6]}hrs ==========
        ======== {tempi[7]} em {hora[7]}hrs ==========
        ==============================================
        """) #tempeturas medidas e as horas em que foram medidas
        media = sum(tempi)/ len(tempi) #média das temperaturas
       

        print("A temperatura média do paciente no dia foi: {:.2f}".format(media))
        print("Loading...")
        sleep(1)
        print('=='*30)
        print('Agora vamos mostrar em quais horários e quantas vezes sua temperatura variou!')
        print('=='*30)
        count = 0
        count1 = 8
        if tempi[0] > media:
            print('Sua temperatura ficou acima da média em {} horas'.format(hora[0]))
            print('E sua temperatura foi de {}'.format(tempi[0]))
            count+=1
            count1-=1
        elif tempi[1] > media:
            print('Sua temperatura ficou acima da média em {} horas.'.format(hora[1]))
            print('E sua temperatura foi de {}'.format(tempi[1]))
            count+=1
            count1-=1
        elif tempi[2] > media:
            print('Sua temperatura ficou acima da média em {} horas'.format(hora[2]))
            print('Sua temperatura foi de {}'.format(tempi[2]))
            count+=1
            count1-=1
        elif tempi[3] > media:
            print('Sua temperatura ficou acima da média em {} horas'.format(hora[3]))
            print('E sua temperatura foi de {}'.format(tempi[3]))
            count+=1
            count1-=1
        elif tempi[4] > media:
            print('Sua temperatura ficou acima da média em {} horas'.format(hora[4]))
            print('E sua temperatura foi de {}'.format(tempi[4]))
            count+=1
            count1-=1
        elif tempi[5] > media:
            print('Sua temperatura ficou acima da média em {} horas'.format(hora[5]))
            print('E sua temperatura foi de {}'.format(tempi[5]))
            count+=1
            count1-=1
        elif tempi[6] > media:
            print('Sua temperatura ficou acima da média em {} horas'.format(hora[6]))
            print('E sua temperatura foi de {}'.format(tempi[6]))
            count+=1
            count1-=1
        elif tempi[7] > media:
            print('Sua temperatura ficou acima da média em {} horas'.format(hora[7]))
            print('E sua temperaturafoi de {}'.format(tempi[7]))
            count+=1
            count1-=1
        else:
            print('Opção inválida!')
        print('Sua temperatura ficou acima da média {} vezes'. format(count)) #mostra quantas vezes ela ficou acima da média
        print('Sua temperatura ficou abaixo da média em {} vezes'.format(count1)) #mostra quantas vezes ela ficou abaixo da média

elif usuario == '2':
    while True:
        print('Obrigado volte sempre!')
        break
    


                        




