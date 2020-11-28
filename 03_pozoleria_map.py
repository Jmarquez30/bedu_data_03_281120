#como usar la funcion map de python 

IVA = 0.16

def aplicar_iva(precio):
    resultado = precio * (1 * IVA)
    return round(resulado, 2)
    

precios_sin_iva = [415, 90, 355, 385, 115, 100, 250, 600]
print(precios_sin_iva)

#usar map para palicar una funcion a cada elemento de mi lista
precios_con_iva = list(map(aplicar_iva, precios_sin_iva ))
print(precios_con_iva)
