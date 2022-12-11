import string
import time
import sys
from datetime import timedelta
from random import choice, seed, random
from itertools import combinations_with_replacement

values = string.ascii_letters  # todos os caracteres maiúsculos e minúsculos
values += string.punctuation   # caracteres acentuados    
values += string.digits  # números de 0 a 9 
tam = 10
senha = " "

for i in range(tam):
    senha += choice(values)

print(senha)

def main(args):

    valores = string.ascii_letters
    valores += string.digits
    valores += string.punctuation

    tamanho =  5    # cuidado ao definir o tamanho da senha, pois consumirá bastante memória do seu PC

    init_temp = time.time()
    gerar_senhas(valores, tamanho)
    init_fim = time.time()

    temp = init_temp - init_fim


    print(f"O tempo de execução foi de {temp:2f}s")




def gerar_senhas(valores, tamanho):
    comb = combinations_with_replacement(valores, tamanho)
    print("Combinações:  " + str(len(list(comb))))


if __name__ == '__main__':
    main(sys.argv[1: ]) 

