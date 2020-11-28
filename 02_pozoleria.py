IVA = 0.16

precios_sin_iva = [415, 90, 355, 385, 115, 100, 250, 600]

for precio in precios_sin_iva:
    resultado = precio * (1 + IVA)
    resultado = round(resultado, 2)
    resultado_impreso = f'${precio} con IVA incluido: ${resultado}'
    print(resultado_impreso)