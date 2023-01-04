'''

        Aqui temos exemplo de funcionamento de listas com seus métodos e comandos geralmente usados!


'''


num = [1, 2, 4, 6, 5]
num[2] = 9
num.append(19)   # adiciona um elemtno a lista
num.sort(reverse=True)   # faz a ordenação inversa
num.insert(2, 25)  # insere na posição x o elemento y
print(num)
if 91 in num:
    num.remove(9)
else:
    print("Não achou")

print(f"a minha lista possui {len(num)} elementos")

valores = []
valores.append(1)
valores.append(2)
valores.append(3)

for c, v in enumerate(valores):  
    print(f"Na posição {c} encontrei o valor {v}!")