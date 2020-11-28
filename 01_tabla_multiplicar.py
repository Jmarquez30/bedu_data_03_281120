#preguntar el numero que el usuario queria saber su tabla de multiplicar
# numero = int(input('Que numero quieres multiplicar\t')) tambien se puede poner asi
numero = input('Que numero quieres multiplicar\t')
numero = int(numero)

print(f'A continuacion se muestra la tabla del {numero}')
print('-----------------------------------------')

for n in range(10):
    indice = n + 1 
    resultado = numero * indice
    print(f'{numero} * {indice} = {resultado}')