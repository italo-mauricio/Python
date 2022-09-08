
numeros = ('zero', 'um', 'dois', 'três', 'quatro',
'cinto', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinza',
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input(print("Digite um número entre 0 e 20: ")))
    if 0 <= num <= 20:
        print(f"Você digitou o número {numeros[num]}")
        break
    else:
        print('Você digitou um número acima de vinte')
