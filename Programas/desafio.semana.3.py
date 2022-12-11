
import math

print('Vamos a situação!')
print('Digamos que um corpo X esteja caindo de uma altura X em queda livre')
print('Qual o tempo necessário para que este corpo atinja o solo?')

h = float(input('Digite uma altura X em m: '))   #altura
g = float(input('Digite uma velocidade em m/s: ')) #gravidade
vzero = 0                #velocidade inicial
h1 = (h - vzero)/g     #altura 1 para dferenciar da variável "h"
temp_i = (g* h1**2)/ 2  #tempo de impacto
r = math.sqrt(h1)      #raiz quadrada
c = temp_i / 3600          #conversor de hora

print("o objeto vai atingir o solo em %.2f s ou %.2f h  " % (r, c))





