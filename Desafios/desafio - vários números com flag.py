#testando condições de flag
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para o programa): ')) #o programa vai parar quando 999 ou 0 forem digitados
    if num == 999 or num == 0:
        break
    cont += 1
    soma += num
print(f'a soma dos {cont} valores foi {soma}!') #vai mostrar quants valores foram digitados e a soma entre eles.
