num = [1, 2, 4, 6, 5]
num[2] = 9
num.append(19)
num.sort(reverse=True)
num.insert(2, 25)
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