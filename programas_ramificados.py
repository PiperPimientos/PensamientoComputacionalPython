#Programas ramificados.

# Para que nuestros programas realicen trabajos interesantes estos deben ser capaces de tomar decisiones, test o pruebas, es desde este concepto donde salen las ramificaciones. Dentro de los test que podemos realizar son los operadores de comparación y estos nos devolveras si la comparación es verdadera (True) o falsa (False).
# •	Igual (==): Lo utilizaremos para comparar 2 objetos.
# •	Distinto (!=): Verificamos que los objetos sean distintos.
# •	Mayor que (>): Igual que en algebra, comparamos si el primer termino es mayor que el segundo.
# •	Menor que (<): Verificamos que el primer termino sea menor que el segundo.
# •	Mayor igual que (>=): Verificamos que el primer termino sea mayor igual al segundo.
# •	Menor igual que (<=): Verificamos que el primer termino sea menor igual al segundo.
# Ademas de los operadores de comparación también tenemos los operadores lógicos, estos son 3 (and, or, not).

# Una vez que podemos entender bien los operadores de comparación y lógicos podemos generar nuestros programas ramificados. Una forma típica de ocupar los operadores es con el método if.
if condition:   # Evaluamos en primera instancia una condición.
    #expresion
elif:           # En caso de que no se cumpla la condición anterior evaluamos nuevamente con otra.
    #expresion
else:           # En caso de que no se cumpla ninguna condición.
    #expresion

# En el ejemplo anterior pueden es obligatorio el 'if', sin embargo 'elif'
# y 'else' son opcionales. Pueden existir cuantos 'elif' queramos, pero solo
# puede haber 1 'if' y 1 'else'.

if 4 > 5:
    pass
elif 4 < 5:
    print('4 es menor que 5')
else:
    pass

# Para poner en práctica esto crearemos un archivo programas_ramificados.py y dentro de el escribiremos:
num_1 = int(input('Escoge un entero: '))    # Preguntamos por un primer numero.
num_2 = int(input('Escoge otro entero: '))  # Luego preguntamos por un segundo numero.

if num_1 > num_2:       # Si el primer numero es mayor que el segundo.
    print('El primer numero es mayor que el segundo.')  # Imprimimos esta expresión.
elif num_1 < num_2:     # En caso de que el segundo sea mayor.
    print('El segundo numero es mayor que el primero.') # Imprimiremos esta expresión.
else:   # En caso de que no cumpla ninguna condición.
    print('Los 2 numeros son iguales.')
