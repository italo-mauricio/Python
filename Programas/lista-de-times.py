import os

def main():
    os.system("cls")
    while True:
        print(f'''
        | ==================================================================== |
        |                        Brasileirão Assaí                             |
        | ==================================================================== |
        |                                                                      |
        |                    Acessar Tabela Série A - 1                        |
        |                    Acessar Tabela Série B - 2                        |                   
        |                    Acessar Tabela Série C - 3                        |         
        |                    Sair - 4                                          | 
        |                                                                      |
        | ==================================================================== |

        ''')
        opção = ' '
        opção = input("Escolha uma opção: ")

        if opção == '1':
            timesa()
        elif opção == '2':
            timesb()
        elif opção == '3':
            timesc()
        elif opção == '4':
            print("Obrigado pela preferência.")
            break
        else:
            print('Opção inválida!')

main()






def timesa():
    os.system("cls")
    while True:
        times = ('Corinthians', 'Palmeiras', 'Santos','Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
        'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense',
        'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')

        print(f'''Lista de todos os times da Série A do Brasileirão

            Lista de times {times}

            Os cinco primeiros {times[:5]}

            Os quatro últimos são {times[-4:]}

            Os times em ordem alfabética{sorted(times)}


        ''')

        cont = input("Aperte ENTER para retornar ao Menu...")
        main()



def timesb():
    os.system("cls")
    while True:
        times = ('Náutico', 'Santa Cruz', 'Ituano','Boa Esporte',
        'Criciuma', 'Flamengo-CE', 'Vasco-PI', 'Corinthians-RN', 'Atlético-RN',
        'Botafogo-PI', 'Brasiliense', 'Barcelona-PI', 'Rondonópolis', 'Fluminense-CE',
        'Sport', 'Guarani', 'Curitiba', 'Jec', 'Ponte Preta-PR',
        'Atlético-GO')

        print(f'''Lista de todos os times da Série B do Brasileirão

            Lista de times {times}

            Os cinco primeiros {times[:5]}

            Os quatro últimos são {times[-4:]}

            Os times em ordem alfabética{sorted(times)}


        ''')

        cont = input("Aperte ENTER para retornar ao Menu...")
        main()




def timesc():
    os.system("cls")
    while True:
        times = ('Mirassol', 'Volta Redonda', 'Aparecidense','ABC',
        'Figueirense', 'Vitória', 'Paysandu', 'São José-RS', 'Remo',
        'Manaus', 'Confiança', 'Floresta', 'Altos', 'Ypiranga-RS',
        'Ferroviário', 'Campinense', 'Brasil de Pelotas', 'Atlético-CE', 'Ponte Preta-PB',
        'Atlético-CE')

        print(f'''Lista de todos os times da Série C do Brasileirão

            Lista de times {times}

            Os cinco primeiros {times[:5]}

            Os quatro últimos são {times[-4:]}

            Os times em ordem alfabética{sorted(times)}


        ''')

        cont = input("Aperte ENTER para retornar ao Menu...")
        main()




