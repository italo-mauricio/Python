import time
from random import randint
from time import sleep

diary = []

option = ''
print('WELCOME TO UFRN \U0001f600 !!!')
print('''My name is Helena \U0001F600 , i'm the campus virtual assistant, 
i'm here to help you.
''')
print('But first, i need to ask you a question...')
time.sleep(1)
print('You want to access the options menu?')
print('if yes, type -> Yes')
print('if not, type -> No')
print('if bônus, type -> Game')
print('if Utilites, type -> Utilites')

user = str(input("What's your choice: ")).lower()
if user == 'yes':
    print('Wonderfull, you chose to access the menu')
    print("Let's go \U0001F51B ...")
    time.sleep(1)
    while option != '0':
        print('''        ===============================================
        ===============================================
        =============== Contact Book \U0001F4D5 ===============
        ===============================================
        =============== 1 - Register \U0001F4D6 ===============
        =============== 2 - Display  \U0001F9D0 ===============
        =============== 3 - Search   \U0001F513 ===============
        =============== 4 - Remove   \U0001F504 ===============
        =============== 5 - Close    \U0001F519 ===============
        ===============================================
        ===============================================
        ''')
        option = input('Choose one of the options: ')
        contact = False
        if option == '1':
            print()
            print('You chose option 1')
            print("Let's register you in the system")
            contact = []
            name = input('Please, type your name: ').lower()
            contact.append(name)
            email = input('Please, type your email: ').lower()
            contact.append(email)
            fone = int(input('Please, enter your contact number: '))
            contact.append(fone)
            diary.append(contact)
            print('Congratulations, your registration was succesfull!!! \U0001F929')
            print('Loading Menu...')
            time.sleep(1)
            print()
            
        
        elif option == '2':
            print()
            print('You chose option 2')
            print('We will show you all registered contacts!')
            time.sleep(1)
            print('Loading Contacts..')
            for i in diary:
                print('Name:\t', i[0])
                print('Email:\t', i[1])
                print('Contact Number:\t', i[2])
                print()
                print('Wonderful, here are the contacts we found for you! \U0001F609')
                print('Loadin menu...')
                time.sleep(1)
        
        elif option == '3':
            print()
            print("You chose option 3")
            print("We'll find you some contact for you!")
            name_search = input('Which contact do you want to find in our system?: ')
            demand = False
            for people in diary:
                if name_search.upper() in people[0].upper():
                    demand = True
                    print('Searching...')
                    time.sleep(1)
                    print('We found!')
                    print('Name:\t', people[0])
                    print('Email:\t', people[1])
                    print('Contact Number:\t', people[2])
                    print('Hope it was of great help to you!\U0001F606')
            if not demand:
                print("Unfortunately we could't findthe contact \U0001F914")
                print("Loading Menu...")
                time.sleep(1)
            print()
        
        
        elif option == '4':
            print()
            print('You chose option 4')
            print('So you want to remove a contact from your diary?')
            print("Okay... let's go.")
            name_remove = input('Qual contato vc quer remover: ')
            remove = False
            for name_remove in diary:
                
                remove = True
                diary.remove(name_remove)
                print('Contato removido')
            if not remove:
                print('Opção inválida')
            
            
        elif option == '5':
            print()
            print('So do you want to go out menu?')
            print('Okay!')
            break
        
        else:
            print("Invalid Option")
    print('GOODBYE, COME BACK SOON \U0001F44B')
elif user == 'no':
    print("Damn, I'll miss you, but thanks for dropping by")
    print("See you \N{slightly smiling face}")
elif user == 'game':

    option = ''
    print('You chose the games option!')
    print('Welcome to the player options menu')
    print('Do you want to continue?')
    print('if yes, type -> Yes')
    print('If not, type -> No')
    
    
    user = str(input("What's your choice: ")).lower()
    if user == 'no':
        print('Good bye')
    if user == 'yes':
        while user == 'yes':
            print('Welcome to the games menu, take your pick! ')
            print('''        ============================================
        ============================================
        ===============  GAMES! ====================
        ========= 1 - Gessing Game \U0001F3B2 ==============
        ========= 2 - Tic-Tak-Toe Game \U0001F475 ==========
        ========= 3 - Jokenpô \u2702\uFE0F ====================
        ========= 4 - Saída \U0001F6B6 =====================
        ============================================
            ''')

            player = str(input("What's your choice: ")).lower()
            if player == '1':
                acertou = False
                while option != '0' and not acertou:
                    
                    print('Welcome to the Guessing Game')
                    print("=="*20)
                    time.sleep(1)
                    print('The game has two phases')
                    print("let's go to the first phase...")
                    time.sleep(1)
                    print('''GAME RULES:
                    ['Rule 1° = Chose one number]
                    ['Rule 2° = Be very lucky]
                    ['Rule 3° = follow the first two \U0001F605]
                    ''')
                    CPU = randint(1,9)
                    player_game = int(input('Try to hit a value: '))
                    i = 1
                    while player_game != CPU and i < 3:
                        print('You missed!')
                        if player_game > CPU:
                            print('You went too far, go back a little...')
                        else:
                            print('You need to climb this mountain more, keep going!')
                        player_game = int(input('Try to hit a value: '))
                        
                        i += 1
                    
                    if player_game == CPU:
                            print('You got it right after %d trying'%i)

                    elif player_game != CPU:
                        print('You failed even with 3 attempts!!')

                    if i == 1 and player_game == CPU:
                        print("Beginner's luck \U0001F602")
                    elif i == 2 and player_game == CPU:
                        print('You were pretty insightful but it was still luck!\U0001F92D')
                    elif i == 3 and player_game == CPU:
                        print('You were very perceptive, an excellent strategist, Sun Tzu would be jealous of you!\U0001F44F')
                    else:
                            print("It wasn't this time, but don't give up! \U0001F4AA")  
                                
                    print('CPU value = {}'.format(CPU))
                    time.sleep(2)
                    print('*=='*30)
                    print('==*'*30)
                    print("You made it to the second level, whether or not you hit the first one, no problem!!")
                    print('Keep going with the game!!!')
                    print('The challenge now is to hit a number between 1 and 100!')
                    print('GOOD LOOK DUDE')
                    print("Let's start the second challenge, now much bigger than the first!")
                    print('Wait a minute!')
                    print('LOADING \U0001F3B2...')
                    time.sleep(5) #Aqui foi um plus, lembrei que existia esse comando de sleep e decidir usar
                    #para parecer que estamos num jogo de verdade com tela de carregamento.
                    print("all ready, let's start!")
                    #Professor, quis fazer o desafio na sequênca, como se fosse um próximo nível
                    import random
                    cpu = random.randint(1, 100)
                    min = 1 #minimo de números na faixa de representação
                    max = 100 #máxmo na faixa de representação
                    disqua = False #varável para desclassificação
                    player_game2 = int(input('Try to hit a value:: '))
                    if player_game2 < min or player_game2 > max:
                        disqua = True
                    plays = 1
                    while player_game2 != cpu and plays < 10 and not disqua:
                        print("you didn't get friend...")
                        if player_game2 < min or player_game2 > max:
                            disqua = True
                        else:
                            if player_game2 > cpu:
                                print("Boy... I'd say it's lower \U0001F602")
                                max = player_game2 - 1
                            else:
                                print('The answer is a hill... go higher!')
                                min = player_game2 + 1 
                            print('You only have more %d plays champion'%(10-plays))
                            player_game2 = int(input('Digite seu palpite: '))
                            plays += 1
                    if player_game2 == cpu:
                        
                        print('You got it... after {} plays'.format(plays))
                        if plays == 1:
                            print('You are very lucky, congratulations!!! \U0001F970')
                        elif plays <= 4:
                            print('Okay, you got it after {} tries but stil, but still it was very lucky! \U0001F605'.format(plays))
                        elif plays <= 7:
                            print('You are a great strategist, but you need to improve a lot! \U0001F60A')
                            
                        else:
                            print('You got it, but i recommend more training! \U0001F601')
                        acertou = True

                    elif disqua == True:
                        acertou = True
                        print('...Unfortunately you broke the limits of representation, you are disqualified!')
                        print('REASON: You selected a number below or above the tip')
                        print('''Because there are two ways to declassify:
            1st - choose a number less than 1 and greater than 100
            2nd - your next guess after the first one disobeys the hint, for example:
            your guess was 20, the answer is 18, the hint will suggest you a number less than 20
            if you choose 21, for example, you will be disqualified, as the range will be reduced to
            1 and 19.''')#Quis esclarecer aqui como funciona o sistema de desclassificação
                        print('Minimum value was: ', min)
                        print('Maximum value was: ', max)
                        print('The computer chose: ', CPU)
                    else:
                        acertou = True
                        print("Oops, unfortunately you didn't get it right and exceeded the number of moves")
                        print('The number was: {}'.format(CPU))
                    print('END GAME!')


                

                
            
            elif player == '2':
                while option != '0':
                    print('''Welcome to Tic-tac-to
                    one of the oldest games and for sure one of the first you played in your childhood.
                    ''')
                    print('lets go...')
                    time.sleep(1)
                    old = [

                                ['_', '_', '_'],
                                ['_', '_', '_'],
                                ['_', '_', '_']
                            
                            ]

                    #condicionais de vitória e de jogadas   
                    win = False
                    play = 0
                    draw = False
                    #laço de repetição
                    while play < 10 and not(win):
                        print("Board")
                        for i in range(3):
                            for j in range(3):
                                print(old[i][j], end=' ')
                            print()  
                        #espaçamento
                        
                        print("\nPlayer X it's your turn!")
                        i = int(input('Inform the line: '))
                        j = int(input('Inform the column: '))
                        old[i-1][j-1] = 'X'
                        print("Board")
                        for i in range(3):
                            for j in range(3):
                                print(old[i][j], end=' ')
                            print()
                        #condicionais de teste 
                        if (old[0][0] == old[0][1]) and (old[0][1] == old[0][2]) and (old[0][2] != '_'):
                            win= True
                        elif (old[1][0] == old[1][1]) and (old[1][1] == old[1][2]) and (old[1][2] != '_'):
                            win = True
                        elif (old[2][0] == old[2][1]) and (old[2][1] == old[2][2]) and (old[2][2] != '_'):
                            win = True
                        elif (old[0][0] == old[1][0]) and (old[1][0] == old[2][0]) and (old[2][0] != '_'):
                            win = True
                        elif (old[0][1] == old[1][1]) and (old[1][1] == old[2][1]) and (old[2][1] != '_'):
                            win = True
                        elif (old[0][2] == old[1][2]) and (old[1][2] == old[2][2]) and (old[2][2] != '_'):
                            win = True
                        elif (old[0][0] == old[1][1]) and (old[1][1] == old[2][2]) and (old[2][2] != '_'):
                            win = True
                        elif (old[0][2] == old[1][1]) and (old[1][1] == old[2][0]) and (old[2][0] != '_'):
                            win = True

                        if win == True:
                            print("Calculating result...")
                            time.sleep(1)
                            print('Player X WINS!!!')
                        
                        else:
                            print("\nPlayer Y its's your turn!")
                            i = int(input('Inform the line: '))
                            j = int(input('Inform the column: '))
                            old[i-1][j-1] = 'Y'
                            if (old[0][0] == old[0][1]) and (old[0][1] == old[0][2]) and (old[0][2] != '_'):
                                win= True
                            elif (old[1][0] == old[1][1]) and (old[1][1] == old[1][2]) and (old[1][2] != '_'):
                                win = True
                            elif (old[2][0] == old[2][1]) and (old[2][1] == old[2][2]) and (old[2][2] != '_'):
                                win = True
                            elif (old[0][0] == old[1][0]) and (old[1][0] == old[2][0]) and (old[2][0] != '_'):
                                win = True
                            elif (old[0][1] == old[1][1]) and (old[1][1] == old[2][1]) and (old[2][1] != '_'):
                                win = True
                            elif (old[0][2] == old[1][2]) and (old[1][2] == old[2][2]) and (old[2][2] != '_'):
                                win = True
                            elif (old[0][0] == old[1][1]) and (old[1][1] == old[2][2]) and (old[2][2] != '_'):
                                win = True
                            elif (old[0][2] == old[1][1]) and (old[1][1] == old[2][0]) and (old[2][0] != '_'):
                                win = True
                                
                                #encerramento do laço

                            if win == True:
                                
                                print('Calculating result...')
                                time.sleep(1)
                                print('Player Y WINS!!!')
                                play += 1
                            while play >= 9:
                                draw = True
                                print('Deu velha')
                                play +=1
                            
                    print('End of the phase!')
                    print('==*'*30)
                    print('==*'*30)
            elif player == '3':
                from random import choice
                print('Welcome to JOKENPÔ')
                time.sleep(1)
                print('===*'*20)
                print('''The game consists of you choosing rock, paper or scissors, and you will try to beat the CPU,
                good look...''')
                print("Loading...")
                time.sleep(1)

                items = ['Stone', 'Paper', 'Scissors']

                CPU = items.index(choice(items))
                print('''Your Options:
                [ 0 ] STONE
                [ 1 ] PAPER
                [ 2 ] SCISSORS''')
                player = int(input("What's your move: "))
                
                count = 0
                
                while True:
                    if player > 2:
                        print('Número inválido')
                        player = int(input('Qual é a sua jogada: '))
                        count += 1
                    else:
                        print('CPU playing: {}'.format(items[CPU]))
                        print('Player playing: {}'.format(items[player]))
                        if CPU == 0:
                            if player == 0:
                                time.sleep(1)
                                print('Draw')
                            elif player == 1:
                                time.sleep(1)
                                print('Player Wins!')
                            elif player == 2:
                                time.sleep(1)
                                print('CPU Wins!')
                        elif CPU == 1:
                            if player == 0:
                                time.sleep(1)
                                print('CPU Wins!')
                            elif player == 1:
                                time.sleep(1)
                                print('Draw')
                            elif player == 2:
                                time.sleep(1)
                                print('Player Wins!')
                        elif CPU == 2:
                            if player == 0:
                                time.sleep(1)
                                print('Player Wins!')
                            elif player == 1:
                                time.sleep(1)
                                print('CPU Wins!')
                            elif player == 1:
                                time.sleep(1)
                                print('Draw')
                        player = int(input('Qual é a sua jogada: '))
                        count +=1
                    
            else:
                print('Bye!')
elif user == "utilites":
    option = ''
    print('Welcome to utilities, here I bring you more options for our platform!')
    print('Do you want to continue?')
    print('if yes, type -> Yes')
    print('If not, type -> No')
    user = str(input("What's your choice: ")).lower()

    if user == 'no':
        print('Okay, good bye!')
    if user == 'yes':

        while user == 'yes':
            print('Welcome to utilities menu!!!')
            print('Please choose from the options below!')
            print('''            =======================================================
            ==================== Utilities \U0001f5fa\uFE0F  =====================
            ================ 1 - Leap Year Calendar \U0001F4C5 ==================
            ================ 2 - Average Calculator ===================
            
            
            ''')

            user = str(input("What's your choice: ")).lower()
            
            if user == '1':
                print('Welcome to the leap year calculator!')
                print("let's check if the year you entered is valid or not")
                day = int(input('Inform the day: '))
                month = int(input('Inform the month: '))
                year = int(input('Inform the year: '))
                leap = year % 4 == 0 and year % 100 != 0 or year % 400 ==0

                print('You informed: month {} of the day {} of the year {}'.format(month, day, year))

                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    if day <= 31:
                        print('Invalid Date')
                elif day > 31:
                    print('Invalid Date')

                if month == 4 or month == 6 or month == 9 or month == 11:
                    if day <= 30:
                        print('Valid Date')
                elif day > 30 and month == 4 or month == 6 or month == 9 or month == 11:
                        print('Invalid Date')
                        if month <= 12 and month != 0:
                            print('Valid Month')
                        elif month > 12:
                            print('Valid Month')
                if month == 2 and day > 31:
                        print('Valid Month')

                if month == 2 and day >= 29 and leap == 0:
                    print('Invalid date, does not exist this year')
                elif month == 2 and day <= 29 and leap:
                    print('Valid date, leap year')
                elif month == 2 and day <= 28:
                    print('Valid date, leap year')

                if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
                    print('Leap Year!')
                else:
                    print('Non-leap year')
            elif user == '2':
                print("""Welcome to the average calculator to BSI!
                Below are the articles from this period!

                ====== Introduction to Informatics [1]
                ====== General Theory of Administration [2]
                ====== Logic [3]
                ====== Fundamentals of Mathematics [4]
                ====== Algorithms and Programming Logic [5]
                """)
                student = input('Choose an option: ')
                
                if student == '1':
                        print("""Welcome to Introduction to Informatics!
                        This is your average calculator for your first period of INTF!
                        Given by: Prof Luiz Paulo
                        Le'ts calculate your average this semester...""")
                        print('=+'*40)
                        print("""
                        ========== Unity: 1 =================
                        ========== Unity: 2 =================
                        ========== Unity: 3 =================
                        ========== Final Result: 4 =========
                        ========== Exit Menu: 5 ============
                        ========== Return to Main Menu: 0 ===
                        """)
                        print('+='*40)
                        print('Loading...')
                        sleep(1)
                        i = 0
                        average = 0


                        student = input('Which unity do you want to access: ')
                        while student != '0':
                            
                            if student == '1':
                            
                                print('You chose to chek the first unit grades')
                                print('To be approved you need an average of 5')
                                print('In this unit there will be 2 avalutations')
                                note1 = float(input('Type your first note: '))
                                note2 = float(input('Type your second note: '))
                                average1 = (note1 + note2 ) / 2
                                print('His average was {:.2f}'.format(average1))
                                if average1 >= 5:
                                    print('Congratulations you PASSED with average {:.2f}!!!'.format(average1))
                                else:
                                    print('Unfortunately you failed with average {:.2f}'.format(average1))
                                average += average1
                                
                            
                                student = input('Which unit do you want to access: ')
                                i += 0
                                    

                            elif student == '2':
                                
                                print('You chose to chek the second unit grades')
                                print('To be approved you need an average of 5')
                                print('In this unit there will be 3 avalutations')
                                note1 = float(input('Type your first note: '))
                                note2 = float(input('Type your second note: '))
                                note3 = float(input('Type your third note: '))
                                average2 = (note1 + note2 + note3 )/ 3
                                print('His average was {:.2f}'.format(average2))
                                if average2 >= 5:
                                    print('Congratulations you PASSED with average {:.2f}!!!'.format(average2))
                                else:
                                    print('Unfortunately you failed with average {:.2f}'.format(average2))
                                average += average2
                                
                                student = input('Which unit do you want to access: ')
                                i += 0
                            elif student == '3':
                                
                                print('You chose to chek the third unit grades')
                                print('To be approved you need an average of 5')
                                print('In this unit there will be 4 avalutations')
                                note1 = float(input('Type your first note: '))
                                note2 = float(input('Type your second note: '))
                                note3 = float(input('Type your third note: '))
                                note4 = float(input('Type your four note: '))
                                average3 = (note1 + note2 + note3 + note4)/4
                                print('His average was {:.2f}'.format(average3))
                                if average3 >= 5:
                                    print('Congratulations you PASSED with average {:.2f}!!!'.format(average3))
                                else:
                                    print('Unfortunately you failed with average {:.2f}'.format(average3))
                                average += average3
                                
                                student = input('Which unit do you want to access: ')
                                i += 0
                            elif student == '4':
                                if average / 3 >= 5:
                                    print('Approved by Average!!! {:.2f}'.format(average/3))
                                else:
                                    print("Failed but don't drop out of the course")
                                student = input('Which unit do you want to access: ')
                                i+=1
                            elif student == '5':
                                print("Thank you, have a great day!")
                                break

                            elif student > '5':
                                print('Invalid option, try again!')
                                student = input('Which unit do you want to access: ')
                                i+=1
                                
                        while student == '0':
                            
                            print("""Welcome to the average calculator to BSI!
                            Below are the articles from this period!

                            ====== Introduction to Informatics [1]
                            ====== General Theory of Administration [2]
                            ====== Logic [3]
                            ====== Fundamentals of Mathematics [4]
                            ====== Algorithms and Programming Logic [5]
                            """)
                            aluno = input('Escolha uma opção: ')
                            i+=1
                if aluno == '2':
                        print("""Welcome to General Theory of Administration!
                        This is your average calculator for your first period of TGA!
                        Given by: Prof. Dra Adrianne Souza
                        Le'ts calculate your average this semester...""")
                        print('=+'*40)
                        print("""
                        ========== Unity: 1 =================
                        ========== Unity: 2 =================
                        ========== Unity: 3 =================
                        ========== Final Result: 4 =========
                        ========== Exit Menu: 5 ============
                        ========== Return to Main Menu: 0 ===
                        """)
                        print('+='*40)
                        print('Loading...')
                        sleep(1)
                        i = 0
                        médias = 0


                        aluno = input('Qual unidade você deseja acessar: ')
                        while aluno != '0':
                            
                            if aluno == '1':
                            
                                print('Você escolheu verificar as notas da primeira unidade')
                                print('Para ser aprovador você precisa de média 5')
                                print('Nesta unidade serão 3 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                nota3 = float(input('Digite sua terceira nota: '))
                                media1 = (nota1 + nota2 + nota3) / 3
                                print('Sua média foi de {:.2f}'.format(media1))
                                if media1 >= 5:
                                    print('Parabéns você foi aprovado com média {:.2f}'.format(media1))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media1))
                                médias += media1
                                
                            
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                                    

                            elif aluno == '2':
                                
                                print('Você escolheu verificar as notas da segunda unidade')
                                print('Para ser aprovado você precisa de média 5')
                                print('Nesta unidade serão 5 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                nota3 = float(input('Digite sua terceira nota: '))
                                media2 = (nota1 + nota2 + nota3 )/ 3
                                print('Sua média foi de {:.2f}'.format(media2))
                                if media2 >= 5:
                                    print('Parabéns, você foi aprovado com média {:.2f}'.format(media2))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media2))
                                médias += media2
                                
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                            elif aluno == '3':
                                
                                print('Você escolheu verificar as notas da terceira unidade')
                                print('Para ser aprovado você precisa de média 5')
                                print('Nesta unidade serão 4 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                nota3 = float(input('Digite sua terceira nota: '))
                                nota4 = float(input('Digite sua quarta nota: '))
                                media3 = (nota1 + nota2 + nota3 + nota4)/4
                                print('Sua média foi de {:.2f}'.format(media3))
                                if media3 >= 5:
                                    print('Parabéns você foi aprovado com média {:.2f}'.format(media3))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media3))
                                médias+= media3
                                
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                            elif aluno == '4':
                                if médias / 3 >= 5:
                                    print('Aprovado com média {:.2f}'.format(médias/3))
                                else:
                                    print('reprovado')
                                aluno = input('Qual unidade você deseja acessar: ')
                                i+=1
                            elif aluno == '5':
                                print("Obrigado, tenha um bom dia!")
                                break

                            elif aluno > '5':
                                print('Opção inválida, tente novamente')
                                aluno = input('Qual unidade você deseja acessar: ')
                                i+=1
                        while aluno == '0':
                            print("""Welcome to the average calculator to BSI!
                            Below are the articles from this period!

                            ====== Introduction to Informatics [1]
                            ====== General Theory of Administration [2]
                            ====== Logic [3]
                            ====== Fundamentals of Mathematics [4]
                            ====== Algorithms and Programming Logic [5]
                            """)
                            aluno = input('Escolha uma opção: ')
                            i+=1
                if aluno == '3':
                    
                        print("""Welcome to Logic!
                        This is your average calculator for your first period of LGC!
                        Given by: Prof Dr. João Paulo
                        Le'ts calculate your average this semester...""")
                        print('=+'*40)
                        print("""
                        ========== Unity: 1 =================
                        ========== Unity: 2 =================
                        ========== Unity: 3 =================
                        ========== Final Result: 4 =========
                        ========== Exit Menu: 5 ============
                        ========== Return to Main Menu: 0 ===
                        """)
                        print('+='*40)
                        print('Loading...')
                        sleep(1)
                        i = 0
                        médias = 0


                        aluno = input('Qual unidade você deseja acessar: ')
                        while aluno != '0':
                            
                            if aluno == '1':
                            
                                print('Você escolheu verificar as notas da primeira unidade')
                                print('Para ser aprovador você precisa de média 5')
                                print('Nesta unidade serão 3 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                nota3 = float(input('Digite sua terceira nota: '))
                                media1 = (nota1 + nota2 + nota3) / 3
                                print('Sua média foi de {:.2f}'.format(media1))
                                if media1 >= 5:
                                    print('Parabéns você foi aprovado com média {:.2f}'.format(media1))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media1))
                                médias += media1
                                
                            
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                                    

                            elif aluno == '2':
                                
                                print('Você escolheu verificar as notas da segunda unidade')
                                print('Para ser aprovado você precisa de média 5')
                                print('Nesta unidade serão 5 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                nota3 = float(input('Digite sua terceira nota: '))
                                media2 = (nota1 + nota2 + nota3 )/ 3
                                print('Sua média foi de {:.2f}'.format(media2))
                                if media2 >= 5:
                                    print('Parabéns, você foi aprovado com média {:.2f}'.format(media2))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media2))
                                médias += media2
                                
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                            elif aluno == '3':
                                
                                print('Você escolheu verificar as notas da terceira unidade')
                                print('Para ser aprovado você precisa de média 5')
                                print('Nesta unidade serão 4 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                nota3 = float(input('Digite sua terceira nota: '))
                                nota4 = float(input('Digite sua quarta nota: '))
                                media3 = (nota1 + nota2 + nota3 + nota4)/4
                                print('Sua média foi de {:.2f}'.format(media3))
                                if media3 >= 5:
                                    print('Parabéns você foi aprovado com média {:.2f}'.format(media3))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media3))
                                médias+= media3
                                
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                            elif aluno == '4':
                                if médias / 3 >= 5:
                                    print('Aprovado com média {:.2f}'.format(médias/3))
                                else:
                                    print('reprovado')
                                aluno = input('Qual unidade você deseja acessar: ')
                                i+=1
                            elif aluno == '5':
                                print("Obrigado, tenha um bom dia!")
                                break

                            elif aluno > '5':
                                print('Opção inválida, tente novamente')
                                aluno = input('Qual unidade você deseja acessar: ')
                                i+=1
                        while aluno == '0':
                            
                            print("""Welcome to the average calculator to BSI!
                            Below are the articles from this period!

                            ====== Introduction to Informatics [1]
                            ====== General Theory of Administration [2]
                            ====== Logic [3]
                            ====== Fundamentals of Mathematics [4]
                            ====== Algorithms and Programming Logic [5]
                            """)
                            aluno = input('Escolha uma opção: ')
                            i+=1
                if aluno == '4':
                        print("""Welcome to Fundamentals of Mathematics!
                        This is your average calculator for your first period of FM!
                        Given by: Prof Dr. Marcio Barboza
                        Le'ts calculate your average this semester...""")
                        print('=+'*40)
                        print("""
                        ========== Unity: 1 =================
                        ========== Unity: 2 =================
                        ========== Unity: 3 =================
                        ========== Final Result: 4 =========
                        ========== Exit Menu: 5 ============
                        ========== Return to Main Menu: 0 ===
                        """)
                        print('+='*40)
                        print('Loading...')
                        sleep(1)
                        i = 0
                        médias = 0


                        aluno = input('Qual unidade você deseja acessar: ')
                        while aluno != '0':
                            
                            if aluno == '1':
                            
                                print('Você escolheu verificar as notas da primeira unidade')
                                print('Para ser aprovador você precisa de média 5')
                                print('Nesta unidade serão 3 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                nota3 = float(input('Digite sua terceira nota: '))
                                nota4 = float(input('Digite sua quarta nota: '))
                                media1 = (nota1 + nota2 + nota3 + nota4) / 4
                                print('Sua média foi de {:.2f}'.format(media1))
                                if media1 >= 5:
                                    print('Parabéns você foi aprovado com média {:.2f}'.format(media1))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media1))
                                médias += media1
                                
                            
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                                    

                            elif aluno == '2':
                                
                                print('Você escolheu verificar as notas da segunda unidade')
                                print('Para ser aprovado você precisa de média 5')
                                print('Nesta unidade serão 5 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                media2 = (nota1 + nota2  )/ 2
                                print('Sua média foi de {:.2f}'.format(media2))
                                if media2 >= 5:
                                    print('Parabéns, você foi aprovado com média {:.2f}'.format(media2))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media2))
                                médias += media2
                                
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                            elif aluno == '3':
                                
                                print('Você escolheu verificar as notas da terceira unidade')
                                print('Para ser aprovado você precisa de média 5')
                                print('Nesta unidade serão 4 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                media3 = (nota1 + nota2 )/ 2
                                print('Sua média foi de {:.2f}'.format(media3))
                                if media3 >= 5:
                                    print('Parabéns você foi aprovado com média {:.2f}'.format(media3))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media3))
                                médias+= media3
                                
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                            elif aluno == '4':
                                if médias / 3 >= 5:
                                    print('Aprovado com média {:.2f}'.format(médias/3))
                                else:
                                    print('reprovado')
                                aluno = input('Qual unidade você deseja acessar: ')
                                i+=1
                            elif aluno == '5':
                                print("Obrigado, tenha um bom dia!")
                                break

                            elif aluno > '5':
                                print('Opção inválida, tente novamente')
                                aluno = input('Qual unidade você deseja acessar: ')
                                i+=1
                        while aluno == '0':
                            
                            print("""Welcome to the average calculator to BSI!
                            Below are the articles from this period!

                            ====== Introduction to Informatics [1]
                            ====== General Theory of Administration [2]
                            ====== Logic [3]
                            ====== Fundamentals of Mathematics [4]
                            ====== Algorithms and Programming Logic [5]
                            """)
                            aluno = input('Escolha uma opção: ')
                            i+=1
                if aluno == '5':
                        print("""Welcome to Algorithms and Programming Logic!
                        This is your average calculator for your first period of ALP!
                        Given by: Prof Dr. Flavius Gorgônio
                        Le'ts calculate your average this semester...""")
                        print('=+'*40)
                        print("""
                        ========== Unity: 1 =================
                        ========== Unity: 2 =================
                        ========== Unity: 3 =================
                        ========== Final Result: 4 =========
                        ========== Exit Menu: 5 ============
                        ========== Return to Main Menu: 0 ===
                        """)
                        print('+='*40)
                        print('Loading...')
                        sleep(1)
                        i = 0
                        médias = 0


                        aluno = input('Qual unidade você deseja acessar: ')
                        while aluno != '0':
                            
                            if aluno == '1':
                            
                                print('Você escolheu verificar as notas da primeira unidade')
                                print('Para ser aprovador você precisa de média 5')
                                print('Nesta unidade serão 3 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                nota3 = float(input('Digite sua terceira nota: '))
                                nota4 = float(input('Digite sua quarta nota: '))
                                nota5 = float(input('Digite sua quinta nota: '))
                                media1 = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
                                print('Sua média foi de {:.2f}'.format(media1))
                                if media1 >= 5:
                                    print('Parabéns você foi aprovado com média {:.2f}'.format(media1))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media1))
                                médias += media1
                                
                            
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                                    

                            elif aluno == '2':
                                
                                print('Você escolheu verificar as notas da segunda unidade')
                                print('Para ser aprovado você precisa de média 5')
                                print('Nesta unidade serão 5 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                nota3 = float(input('Digite sua terceira nota: '))
                                media2 = (nota1 + nota2 + nota3  )/ 3
                                print('Sua média foi de {:.2f}'.format(media2))
                                if media2 >= 5:
                                    print('Parabéns, você foi aprovado com média {:.2f}'.format(media2))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media2))
                                médias += media2
                                
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                            elif aluno == '3':
                                
                                print('Você escolheu verificar as notas da terceira unidade')
                                print('Para ser aprovado você precisa de média 5')
                                print('Nesta unidade serão 4 avaliações')
                                nota1 = float(input('Digite sua primeira nota: '))
                                nota2 = float(input('Digite sua segunda nota: '))
                                media3 = (nota1 + nota2 )/ 2
                                print('Sua média foi de {:.2f}'.format(media3))
                                if media3 >= 5:
                                    print('Parabéns você foi aprovado com média {:.2f}'.format(media3))
                                else:
                                    print('Infelizmente você foi reprovado com média {:.2f}'.format(media3))
                                médias+= media3
                                
                                aluno = input('Qual unidade você deseja acessar: ')
                                i += 0
                            elif aluno == '4':
                                if médias / 3 >= 5:
                                    print('Aprovado com média {:.2f}'.format(médias/3))
                                else:
                                    print('reprovado')
                                aluno = input('Qual unidade você deseja acessar: ')
                                i+=1
                            elif aluno == '5':
                                print("Obrigado, tenha um bom dia!")
                                break

                            elif aluno > '5':
                                print('Opção inválida, tente novamente')
                                aluno = input('Qual unidade você deseja acessar: ')
                                i+=1
                        while aluno == '0':
                            
                            print("""Welcome to the average calculator to BSI!
                            Below are the articles from this period!

                            ====== Introduction to Informatics [1]
                            ====== General Theory of Administration [2]
                            ====== Logic [3]
                            ====== Fundamentals of Mathematics [4]
                            ====== Algorithms and Programming Logic [5]
                            """)
                            aluno = input('Escolha uma opção: ')
                            i+=1
            


                        
                            
                            
                            




        




        

        
