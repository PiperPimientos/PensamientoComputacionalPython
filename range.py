# Otra estructura de datos son los rangos que:
# -	Representan una secuencia de enteros
# -	Su sintaxis es: range(comienzo, fin, pasos)
# -	Al igual que las cadenas y las tuplas, loos rangos son inmutables
# -	Muy eficientes en uso de memoria y normalmente utilizados en for loops.

# Ejemplo

my_range = range(1, 5)

for i in my_range:
    print(i)

# >>>
# 1
# 2
# 3
# 4




# Si definimos un numero de pasos incluso podríamos hacer rangos que tenan un comienzo y fin distintos, pero que sean iguales ==

# Ejemplo

# 1.	creamos un rango llamado 
my_range = range(0, 7, 2) #es decir que va del 0 hasta el 7 en pasos de dos en dos
# 2.	creamos un rango llamado 
my_other_range = range(0, 8, 2) #es decir que va del 0 hasta el 8 en pasos de dos en dos
# 3.	Creamos el loop 
for i in my_range:
    print(i)
# 4.	Creamos el loop 
for i in my_other_range: 
    print(i)

#En ejecucion ambos son iguales >>>
# 0
# 2
# 4
# 6



#Si queremos por ejemplo enerar los numeros pares del 1 al 100

for i in range(1, 101, 2):
    print(i)







# RETO: Hacer un rango del 1 al 99 con los numeros nones

# Buscando imprimir los nones de 1 a 99 en pocas líneas, me encontré con dos modificadores de la función print en Python 3.x, que son: \t para imprimir un tabulador y end="" para evitar el salto de línea


nones = range(1, 101, 2)
col = 1
for i in nones:
    if(col<10):
        print(f'(i)\t', end="")
        col += 1
    else:
        print(i)
        col=1
