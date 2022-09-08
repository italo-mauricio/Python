

produtos = ('Lápis', 1.75,
            'Borracha', 0.50, 
            'Caderno', 25.0,
            'Estojo', 10.0,
            'Transferidor', 2.0,
            'Compasso', 1.0,
            'Mochila', 55.0,
            'Canetas', 2.0,
            'Livro', 50.0, )


for i in range(0, len(produtos)):
    if i %2 == 0:
        print(f'{produtos[i]}: .<30')
    else:
        print(f'R${produtos[i]}:.<30')



# programa incompleto




