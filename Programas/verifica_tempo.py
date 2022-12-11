
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
horapassou = []
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
        count= 0

        for i in range(8):
            if tempi[i] > media:
                count += 1
                horapassou.append(hora[i])
            if i == 7:
                print('A temperatura passou da média {} vezes'.format(count))
        print("Os horários que a temperatura ficou acima da média:")       
        for j in horapassou:
            print('{} hrs'.format(j))
               
            

            
              
        
              

elif usuario == '2':
    while True:
        print('Obrigado volte sempre!')
        break
    


                        




