#tabuada com condição de parada
while True:
    n = int(input('Gostaria de ver a tabuada de qual valor: '))
    print('-'*30)
    if n < 0:
        print('Número negativo detectado, tente novamente!')
        break
        
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
        
    print('-'*30)