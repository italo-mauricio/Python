#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dees
#e escrevendo o nome na tela
import random
print('Bom Dia a todos!')
print('Iremos anunciar hoje a lista oficial de convocados da seleção brasileira para a copa de 2022')
print("Como todos sabem, iremos buscar o hexa, e para isso, teremos que contar com os nossos melhores jogadores")
print("Segue a lista de todos os convocados: \n")
lista = []

lgol = ['Alisson - Liverpool (ING)', 'Ederson - Manchester City (ING)', 'Weverton - Palmeiras (BRA)', 'Hugo Neneca - Flamengo (BRA)', 'Diego Alves - Flamengo (BRA)', 'Mailson - Sport (BRA)']
lzag = ['Eder Militão - Real Madrid (ESP)', 'Gabriel Magalhães - Arsenal (ING)', 'Marquinhos - Paris Saint-Germain (FRA)', 'Thiago Silva - Chelsea (ING)', 'Luciano Juba - Sport (BRA)', 'David Luiz - Flamengo (BRA)']
lteral = ['Daniel Alves - Barcelona (ESP)', 'Danilo - Juventus (ITA)', 'Alex Telles - Manchester United (ING)', 'Guilherme Arana - Atlético (MG)', 'Marcos Rocha - Palmeiras (BRA)', 'Rafinha - Grêmio (BRA)']
lmeio = ['Arthur - Juventus (ITA)', 'Bruno Guimarães - NewCastle (ING)', 'Casemiro - Real Madrid (ESP)', 'Fabinho - Liverpool (ING)', 'Fred - Manchester United - (ING)', 'Lucas Paquetá - Lyon (FRA)', 'Philippe Coutinho - Aston Villa (ING)', 'Gerson - Olympique de Marseille (FRA)', 'Éverton Ribeiro - Flamengo (BRA)', 'João Gomes - Flamengo (BRA)']
lata = ['Neymar - Paris Saint-Germain (FRA)', 'Antony - Ajax (HOL)', 'Gabriel Martinelli - Arsenal (ING)', 'Raphinha - Leeds United (ING)', 'Richarlison - Everton (ING)', 'Rodrygo - Real Madrid (ESP)', 'Vini Jr - Real Madrid (ESP)', 'Gabigol - Flamengo (BRA)', 'Hulk - Atlético (MG)']

while len(lgol) !=0:
    random.shuffle(lgol)
    lgol = lgol[:4]
    print('A lista de convocados para goleiros são: \n')
    print(lgol[1])
    print(lgol[2])
    print(lgol[3])
    print('\n')
    break
while len(lzag) !=0:
    random.shuffle(lzag)
    lzag = lzag [:5]
    print('A Lista de convocados para zagueiros são: \n')
    print(lzag[1])
    print(lzag[2])
    print(lzag[3])
    print(lzag[4])
    print('\n')
    break
while len(lteral) !=0:
    random.shuffle(lteral)
    lteral = lteral[:5]
    print('A Lista de convocados para a lateral são: \n')
    print(lteral[1])
    print(lteral[2])
    print(lteral[3])
    print(lteral[4])
    print('\n')
    break
while len(lmeio) !=0:
    random.shuffle(lmeio)
    lmeio = lmeio [:8]
    print('A Lista de convocados para o meio campo são:\n')
    print(lmeio[1])
    print(lmeio[2])
    print(lmeio[3])
    print(lmeio[4])
    print(lmeio[5])
    print(lmeio[6])
    print(lmeio[7])
    print('\n')
    break
while len(lata) !=0:
    random.shuffle(lata)
    lata = lata[:9]
    print('A Lista de convocados para o ataque são: \n')
    print(lata[1])
    print(lata[2])
    print(lata[3])
    print(lata[4])
    print(lata[5])
    print(lata[6])
    print(lata[7])
    print('\n')
    break

print('Estes são os convocados para a copa do mundo de 2022')
print('Boa sorte para a nossa seleção!!')


