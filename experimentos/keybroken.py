import string
from random import seed, random, choice


values = string.ascii_lowercase + string.ascii_uppercase
tamanho = 6
senha = " "

for i in range(tamanho):
    senha += choice(values)

print(senha)