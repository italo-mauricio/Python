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
            break
        elif opção == '3':
            break
        elif opção == '4':
            break
        else:
            print('Opção inválida!')








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





main()