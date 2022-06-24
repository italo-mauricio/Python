from time import sleep
opção = ''
print("""Bem vindos Algoritmos e lógica de Programação!
Essa é sua calculadora de média para o seu Primeiro período de ALP!
Ministrada pelo Prof Dr, Flavius Gorgonio.
Vamos calcular a sua média nesse semestre...""")
print('=+'*40)
print("""
========== Unidade 1 =================
========== Unidade 2 =================
========== Unidade 3 =================
========== Resultado final 4 =========
========== Sair do menu 5 ============
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
        nota4 = float(input('Digite sua quarta nota: '))
        nota5 = float(input('Digite sua quinta nota: '))
        media2 = (nota1 + nota2 + nota3 + nota4 + nota5)/ 5
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
                print('Loading...')
                sleep(1)
                print('Aprovado com média {:.2f}'.format(médias/3))
                print('Bem vindo ao próximo período!')
        else:
                print('Loading...')
                sleep(1)
                print('Reprovado com média {:.2f}'.format(médias/3))
                print("Não desanime, você consegue na próxima vez!")
        aluno = input('Qual unidade você deseja acessar: ')
        i+=1
        
    elif aluno == '5':
        print("Obrigado, tenha um bom dia!")
        break

    elif aluno > '5':
        print('Opção inválida, tente novamente')
        aluno = input('Qual unidade você deseja acessar: ')
        i+=1
    
                



