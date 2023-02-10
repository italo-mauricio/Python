'''
    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
    analisar a expressão passada está com os parênteses abertos e fechados na ordem correta.

'''

expressao = str(input("Digite a expressão: "))
pilha = []

for i in expressao:
    if i == '(':
        pilha.append('()')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressão está valida")
else:
    print("Sua pilha está inválida")