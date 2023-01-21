print("Vamos criar uma sequência de Fibonacci !")

n = int(input("Digite a quantidade de termos que você quer mostrar: "))
t1 = 0
t2 = 1

print("=="*30)
print(f'{t1} -> {t2}', end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1

termo = (t1 + t2) - 1

print(' -> FIM')
print(f'A soma dos termos apresentados é {termo}')