import string
from random import seed, random, choice


values = string.ascii_letters  # todos os caracteres maiúsculos e minúsculos
string.punctuation   # caracteres acentuados    
string.digits  # números de 0 a 9 
tamanho = 6
senha = " "

for i in range(tamanho):
    senha += choice(values)

print(senha)