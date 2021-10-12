#Funciones

# Con lo que ya conocemos hasta el momento podríamos diseñar casi cualquier programa, desde programas para lanzar cohetes hasta sistemas operativos. Conocer estos primitivos significa ser Turing complete, es decir que podríamos recrear por ejemplo una maquina de Turing. Sin embargo, un programa de este estilo, con miles de millones de líneas en un solo archivo, seria un completo desastre

# Los lenguajes de programación modernos nos permiten generar abstracciones, funciones, modulos que nos harán el camino mucho mas corto.

# La abstracción significa que uno no necesita entender la forma en la que algo opera internamente para poderlo utilizar. Por ejemplo, para utilizar una calculadora no se necesita saber de electrónica, no necesitamos saber como los componentes están conectados, lo que se necesita saber, es como operar esa calculadora. En código es utilizar las librerías de otros desarrolladores sin saber como están escritas, no es necesario.

# La Decomposicion por otro lado, permite dividir el código en componentes que colaboran con un fin en común. Se puede pensar como mini programas dentro de uno mismo.

# Ahí es donde las funciones nos ayudan. Las funciones nos permiten abstraer y decomponer nuestro código. 

# La sintaxis de una función

# def <nombre>(<parámetros>):
#         <cuerpo>
#          return <expresión>


# def suma(a, b):
#      total = a + b
#      return total

# suma(a, b)

# Las funciones en Python pueden tener argumentos de tipo keyword y valores por defecto. Esto que significa? Tenemos el keyword def luego tenemos el nombre de la función, luego podemos tener parámetros adentro, llamar variables que pueden incluso inicializarse con valor booleano. Luego dentro de la función habran condicionales para ver si se cumplen las condiciones. Al ejecutar la función podemos llamar los keyword que queremos ejecutar, como en el ejemplo.

# def nombre_completo(nombre, apellido, inverso=False):
#     if inverso:
#         return f' {apellido} {nombre}'
#     else:
#         return f' {nombre} {apellido}'

# nombre_completo('Felipe', 'Restrepo')
# nombre_completo('Felipe', 'Restrepo', inverso=True)
# nombre_completo(apellido='Restrepo', nombre='Felipe')

# Reto: encapsular todos los algoritmos que vimos en el modulo anterior y que el usuario pueda escoger cual de esos algoritmos quiere utilizar para encontrar la raíz cuadrada.

def algorithms():
    algo_option = int(input(""" 
    Bienvenido a calculador de raices cuadradas. Elige una opcion

    1- Para el algoritmo de fuerza bruta
    2- Para el algoritmo de aproximacion de resultados
    3- Para el algoritmo de busqueda binaria: 
    """))

    if algo_option == 1:
        brute_force()
    elif algo_option == 2:
        approximation()
    elif algo_option == 3:
        binary_search()
    else:
        print("Introduce una opcion valida")
    return algo_option

def brute_force():
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0
    
    while respuesta**2 < objetivo:
        print(respuesta) #Para saber como se ejecuta el programa
        respuesta += 1
    
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

def approximation():
    from time import time

    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01 #Entre mas pequeno sea nuestro epsilon, mas precisa sera la respuesta y tardaremos mas
    paso = epsilon**2
    respuesta = 0.0
    tiempo_inicio = time()
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta) #print statement para saber como funciona la ejecucion del algoritmo
        respuesta += paso
    
        tiempo_total = time() - tiempo_inicio
    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def binary_search():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    mid = (alto + bajo) / 2
    
    while abs(mid**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, mid={mid}')
        if mid**2 < objetivo:
            bajo = mid
        else:
            alto = mid
    
        mid = (alto + bajo) / 2
    
    print(f'La raiz cuadrada de {objetivo} es {mid}')


algorithms()