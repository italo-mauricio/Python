import time
from random import randint

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
                player = input("What's your move: ")
                
                count = 0
                if player != 0 or 1 or 2 or 3:
                    print('Não pode string')
                while True:
                    if player != 1 and player != 2 and player != 3:
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
            print('Welcome to utilities manu!!!')
            print('Please choose from the options below!')
            print('''                ===================================================
            ==================== Utilities \U0001f5fa\uFE0F  =====================
            ================ 1 - Leap Year Calendar \U0001F4C5 ==================
            =================== 
            
            
            ''')

            user = str(input("What's your choice: ")).lower()
            i = 0
            while True:
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
                            print('Date verification: Valid Day \u2714\uFE0F')
                        
                    elif day > 31:
                        print('Date verification: Invalid Day \u274C')

                    if month == 4 or month == 6 or month == 9 or month == 11:
                        if day <= 30:
                            print('Date verification: Valid Date \u2714\uFE0F')
                    elif day > 30 and month == 4 or month == 6 or month == 9 or month == 11:
                            print('Date verification: Invalid Date \u274C')
                            if month <= 12 and month != 0:
                                print('Date verification: Valid Month \u2714\uFE0F')
                            elif month > 12:
                                print('Date verification: Valid Month \u2714\uFE0F')
                    if month == 2 and day > 31:
                            print('Date verification: Valid Month \u2714\uFE0F')

                    if month == 2 and day >= 29 and leap == 0:
                        print('Date verification: Invalid date, does not exist this year \u274C')
                    elif month == 2 and day <= 29 and leap:
                        print('Date verification: Valid date, leap year \u2714\uFE0F')
                    elif month == 2 and day <= 28:
                        print('Date verification: Valid date, leap year \u2714\uFE0F')
                    elif day >= 32:
                        print('Date verification: Invalid day \u274C')
                    elif month >= 12:
                        print('Date verification: Invalid Month \u274C')
                    

                    if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
                        print('Leap Year \u2714\uFE0F')
                    else:
                        print('Non-leap year \u274C')
                print('Loading...')
                time.sleep(1)
                print()
                print('Welcome to utilities manu!!!')
                print('Please choose from the options below!')
                print('''                ===================================================
                ==================== Utilities \U0001f5fa\uFE0F  =====================
                ================ 1 - Leap Year Calendar \U0001F4C5 ==================
                =================== 
                
                
                ''')

                user = str(input("What's your choice: ")).lower()
                i+=1
                        
                       
                        
                        
                        




    




    

    
