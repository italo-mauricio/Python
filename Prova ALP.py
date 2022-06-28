#Correção da prova de ALP
#######
#######
from math import log
aluno = ''
print("""======== Correção da Prova de Algoritmos! ====================
======== Selecione as questões que você quer acessar =========
================== Questão [1] ===============================
================== Questão [2] ===============================
================== Questão [3] ===============================
================== Sair do programa [4] ======================
==============================================================
""")

aluno = input('Faça sua escolha: ')
i=0
while aluno != 4: 
    if aluno == '1':
        print('''Questão 01: Acompanhe a execução do programa abaixo,
        analisando o valor de cada variável em cada linha do programa.
        Simule a tela de execução do programa, mostrando os valores que serão
        exibidos cada vez que a função print() é chamada.

        lista = [__,___,___,___,___]
        print('Lista inicial: ', lista)
        tam = len(lista)
        for i in range(1, tam):
            chave = lista[1]
            k = 1
            while (k > 0) and (chave < lista[k-1]):
                lista[k] = lista[k - 1]
                k -= 1
            lista[k] = chave
            print('i=%d, k=%d, lista: '%(i,k), lista)
        print('Lista final: ',lista)

        [A]) Construa uma tabela que apresente o valor das variáveis em cada linha:
        [B]) Identifique o que o programa faz com os valores que são fornecidos como entrada:
        [C]) Apresente o que será exibido na tela durante a execução do programa.
        ''')
        aluno = input('Selecionei uma das questões: ')
        
        if aluno == 'A'.lower():
            
            lista = [71, 74, 16, 27, 84]
            print('Lista inicial: ', lista)
            tam = len(lista)
            for i in range(1, tam):
                    chave = lista[1]
                    k = 1
                    while (k > 0) and (chave < lista[k-1]):
                        lista[k] = lista[k - 1]
                        k -= 1
                    lista[k] = chave
                    print('i=%d, k=%d, lista: '%(i,k), lista)
            print('Lista final: ',lista)

            print("Flavius, eu não consegui responder essa Letra A")
            aluno = '1'

        elif aluno == 'B'.lower():
            i=0
            print('Mas sei que o programa irá verificar a ordem crescente da lista')
            aluno = input('Selecionei uma das questões: ')
            i+=1
            aluno = '1'

        elif aluno == 'C'.lower():
            i=0
            print("Usando um método de controle, irá exibir a lista em ordem crescente ao final")
            aluno = input('Selecionei uma das questões: ')
            i+=1
            aluno = '1'

    elif aluno == '2':
        print('''Questão 2: O quadrado de um número N pode ser calculado a partir da soma dos N
        primeiros termos ímpares. Escreva um programa em Python que receba um número inteiro, calcule
        e retorne o seu quadrado usando o método acima.
        
        ''')
        num = int(input('Digite um número: '))
        somatório = 0

        for i in range(1, (num+1)):
            somatório = somatório + (2 * i) - 1 #eu pego a minha variável que recebe zero fora do for, e jogo dentro dela o i multiplicado por 2
            # menos 1, que dessa forma eu pego o i do for que foi somado ao meu input e consigo calcular o quadrado desse input.
        print('Dessa forma, o quadrado de {} seria {}'.format(num, somatório))
        
        

    elif aluno == '3':
        print('''Questão 3: Você já deve ter escutado falar que para calcular a idade humana de um cão, deve-se
                    multiplicar a idade do animal por 7. Porém, cientistas da Universidade da Califórnia (EUA)
                    descobriram que não é bem assim. Um cálculo mais realista pode ser obtido usando-se a
                    fórmula abaixo. Ou seja, é só multiplicar o logaritmo natural da idade do cão por 16 e
                    acrescentar 31. Escreva um programa em Python que permita ao usuário digitar a idade do
                    seu cãozinho (em anos e meses) e, a partir dos dados informados, calcule e exiba a idade
                    humana do animal.
                    
            ''')

        ano = float(input('Digite o ano do seu animal: '))
        mês = float(input('Digite o mês que ele nasceu: '))
        idade = ano + (mês/12)
        idade_humano = (16*(log(idade))) + 31
        idade_ano = int(idade_humano)
        idade_mes = round((idade_ano - (int(idade_humano))) * 12)

        print('A idade aproximada do seu animalzinho é de {} anos e {:.2f} meses'.format(idade_ano, idade))

    elif aluno == '4':
        print('Obrigado, volte sempre!')
        break
else:
    print("Opção inválida!")


                        

