from datetime import datetime
hora_atual = datetime.now()
datahora = hora_atual.strftime('%d/%m/%Y %H:%M:%S')

#Programinha para gerenciamento de pagamentos de uma loja

print('''Bem vindo(a) às lojas Caicó!
Aqui você encontra os melhores preços da cidade.
================================================

Detectamos no nosso sistema que você já escolheu o seu produto \U0001f970

================================================
''')
print('A data e hora atual para a sua segurança!')
print(f'Compra sendo efetuada as {datahora}')


cliente = ''
cliente = str(input('Você deseja comprar algum produto [S/N]: ')) #opção se o cliente quer comprar
while cliente.startswith('S') or cliente.startswith('s'):
    
        valor = float(input('Quanto você pagou no produto: '))  #menuzinho padrão
        print('''FORMAS DE PAGAMENTO
        [ 1 ] à vista, dinheiro/cheque
        [ 2 ] à vista no cartão
        [ 3 ] 2x no cartão
        [ 4 ] 3x ou mais no cartão''')
        opção = int(input('Escolha uma das opções: '))
#opções de pagamentos
        if opção == 1:
            total = valor
            print('Você pagou o valor cheio, de R${}'.format(total))
        elif opção == 2:
            total = valor - (valor * 5/ 100)
            print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))
        elif opção == 3:
            total = valor
            parcela = total / 2
            print('Sua compra será parcelada em 2x de R${:.2F}'.format(parcela))
            print('Sua compra de R${:.2f} vai custar ao final R${:.2f}'.format(valor, total))
        elif opção == 4:
            total = valor + (valor * 20 / 100)
            totparcela = int(input('Quantas parcelas: '))
            parcela = total / totparcela
            print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparcela, parcela))
            print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))
        else:
            opção > 5
            print('Opção inválida, retorne ao menu!')

while cliente.startswith('N') or cliente.startswith('n'):
    print('Obrigado, volte sempre!')
    break
else:
    print('Opção inválida!')
