#faça uma ordem de apresentação de trabalho de 4 alunos randomicamente numa sala de aula

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))


lista = [n1, n2, n3, n4]

while len(lista) !=0:
    random.shuffle(lista[:4])
    lista = lista[:4]
    print('A ordem de apresentação será: \n')
    print('Primeiro: ', lista[1])
    print('Segundo: ', lista[2])
    print('Terceiro: ', lista[3])
    print('Quarto: ', lista[0])


    break

