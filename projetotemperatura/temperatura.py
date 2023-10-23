from calculo import *

print('\t  Calculadora de C e F   \n')

print('1, para Celsius')
print('2, para Fahrenheit')

comando = int(input('Qual operação deseja ?  \n Escreva aqui: '))

if comando == 1:
    print('De Fahrenheit para Celsius \n')
    c = int(input('Coloque o valor: '))
    print('\n De Fah para Celsius = {}'.format(fahr(c)))

if comando == 2:
    print('De Celsius para Fahrenheit \n')
    f = int(input('Coloque o valor: '))
    print('\n De Celsius para Fahrenheit = {}'.format(cels(f)))