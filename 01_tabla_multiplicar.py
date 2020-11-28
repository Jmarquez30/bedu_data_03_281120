#preguntar el numero que el usuario queria saber su tabla de multiplicar

numero = input('Que numero quieres multiplicar\t')
numero = int(numero)

print(f'A continuacion se muestra la tabla del {numero}')
print('-----------------------------------------')

for n in range(10):
    r = numero * (n + 1)
    print(f'{numero} * {n + 1} = {r}')