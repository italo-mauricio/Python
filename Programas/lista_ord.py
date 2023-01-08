
'''

    Lista ordenada


'''



lista = []

for i in range(0, 5):
    num = int(input("Digite um valor: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print(f"Os valores digitados em ordem foram: {lista}")
lista.sort(reverse=True)
print(f"Os números em forma decrescente são {lista}")


if 5 in lista:

    print("O Valor 5 está na lista")
    print(f"O valor 5 apareceu a primeira vez na posição: {lista.index(5, 0, 5)}")
else:
    print("O 5 não está na lista")
    

