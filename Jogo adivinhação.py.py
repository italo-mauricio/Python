from random import randint
import time
print('Bem Vindos ao jogo da adivinhação')
print('O jogo tem 2 FASES')
print('Vamos a primeira fase...')
time.sleep(1)
print('''REGRAS DO JOGO:
['1° regra = Escolher um número]
['2° regra = tenha muita sorte]
['3° regra = seguir as duas primeras haha]
''')
comp = randint(1,9)
player = int(input('Tente acertar um número: '))
i = 1
while player != comp and i < 3:
    print('Você errou!')
    if player > comp:
        print('Você foi muito a frente, tente um número menor')
    else:
        print('Você precisa subir mais essa colina, está quase!')
    player = int(input('Tente acertar um número: '))
    
    i += 1
  
if player == comp:
        print('Você acertou após %d tentativas'%i)

elif player != comp:
    print('Você errou mesmo com 3 tentativas!')

if i == 1 and player == comp:
    print('Sorte de principiante hahaha')
elif i == 2 and player == comp:
    print('Você foi bem perspicaz, mas ainda acho que foi sorte!')
elif i == 3 and player == comp:
    print('Você foi bem perpiscaz, um excelente estrategista, Sun Tzu teria inveja de você!')
else:
        print('Não foi dessa vez... mas não desista!')  
              
print('Valor de cpu = {}'.format(comp))
time.sleep(2)
print('*=='*30)
print('==*'*30)
print("Você chegou ao segundo nível, acertando ou não o primeiro, não tem problema!!")
print('o jogo continua!!!')
print('o desafo agora é acertar um número entre 1 e 100!')
print('GOOD LOOK DUDE')
print('Vamos começar o segundo desafio, agora bem maior que o primeiro!')
print('Aguarde um instante!')
print('LOADING...')
time.sleep(5) #Aqui foi um plus, lembrei que existia esse comando de sleep e decidir usar
#para parecer que estamos num jogo de verdade com tela de carregamento.
print('Tudo pronto, vamos ao desafio jogador!')
#Professor, quis fazer o desafio na sequênca, como se fosse um próximo nível
import random
cpu = random.randint(1, 100)
min = 1 #minimo de números na faixa de representação
max = 100 #máxmo na faixa de representação
desc = False #varável para desclassificação
jogador = int(input('Digite seu palpite: '))
if jogador < min or jogador > max:
    desc = True
jogadas = 1
while jogador != cpu and jogadas < 10 and not desc:
    print('Você não conseguiu amigo...')
    if jogador < min or jogador > max:
        desc = True
    else:
        if jogador > cpu:
            print('Rapaz... eu díria que é mais pra baixo rsrs')
            max = jogador - 1
        else:
            print('A resposta é uma colina... suba mais um pouco!')
            min = jogador + 1 
        print('Você só tem mais %d jogadas guerreiro(a)'%(10-jogadas))
        jogador = int(input('Digite seu palpite: '))
        jogadas += 1
if jogador == cpu:
    print('Você conseguiu campeão(a)... após {} jogadas'.format(jogadas))
    if jogadas == 1:
        print('Você é MUITO cagado irmão kkkkk parabéns!!')
    elif jogadas <= 4:
        print('okay, você coneseguiu após {} tentativas, mas ainda sim foi muita sorte!'.format(jogadas))
    elif jogadas <= 7:
        print('Você é um ótimo estrategista, porém precisa melhorar um pouco!')
    else:
        print('Você conseguiu, porém precisa melhorar bastante!')

elif desc == True:
    print('...infelizmente você furou os limites de representação, está desclassificado!')
    print('''MOTIVO: Você selecionou um número abaixo ou acima da dica
    pois existem duas formas de desclassficação:
    1° - escolha um número menor que 1 e maior que 100
    2° - o seu próximo palpite após o primeiro desobedecer a dica, por exemplo:
    seu palpite foi 20, a resposta é 18, a dica irá lhe sugerir um número menor que 20
    caso você escolha 21 por exemplo, estará desclassificado, pois a faixa se reduzirá para
    1 e 19.''')#Quis esclarecer aqui como funciona o sistema de desclassificação
    print('Valor mínimo era de: ', min)
    print('Valor máximo era de: ', max)
    print('A CPU escolheu: ', cpu)
else:
    print('Opa, infelizmente você não acertou e excedeu o número de jogadas')
    print('O número era {}'.format(cpu))


print('FIM DO JOGO!')