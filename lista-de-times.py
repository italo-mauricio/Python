import os

def main():
    os.system("cls")

    print(f'''
    | ==================================================================== |
    |                        Brasileirão Assaí                             |
    | ==================================================================== |
    |                                                                      |
    |                    Acessar Tabela Série A - 1                        |
    |                    Acessar Tabela Série B - 2                   
    |
    |
    |

    
    
    
    ''')








def timesa():
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

            O sport está na posição {times.index("Sport Recife")}



        ''')








