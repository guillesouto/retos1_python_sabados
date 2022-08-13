numero = int(input("Digite un numero entero: "))
residuo = numero%5

print(f'el residuo es= {residuo}')

#CONDICIONAL SIMPLE DE PYTHON
if(residuo == 0):
    print("es multiplo de 5")
else:
    print("no es multiplo de 5")
print("fin del programa")