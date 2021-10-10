#Algoritmo de Busqueda binaria o metodo de biseccion

# Otro algoritmo en computer science es la Busqueda Binaria. Esto es, cuando la respuesta se encuentra en un conjunto ordenado, podemos utilizar búsqueda binaria. Es altamente eficiente, pues corta el espacio de búsqueda en dos por cada iteración.

# En la búsqueda binaria podemos acortar nuestro espacio de búsqueda a la mitad cada vez, entonces el espacio de búsqueda se va haciendo mas pequeña y eficiente.

# Si tenemos un conjunto de números del 1 al 10 y queremos encontrar el 7, podemos empezar en 5 que es la mitad, y entre 6 y 10 la mitad es 8 y como 7 no es mayor que 8, el espacio de busqueda se quedara entre el 6 y el 7. OJO. el Conjunto de los numeros debe estar ordenado.

# Para realizar un ejemplo práctico crearemos un programa para buscar raíces cuadradas.

# 1.	definimos nuestra variable objetivo donde guardaremos como valor el int, que mediante el input, el usuario nos ingrese
# 2.	Definimos nuestra variable épsilon y la inicializamos en 0.01
# 3.	Definimos nuestro bajo que será nuestro limite inferior que será de 0.0
# 4.	Definimos nuestro alto y contendrá una nueva función que se llama max() que nos regresa el valor mas alto entre dos valores, y dentro de esta, le diremos que nos regrese (1.0, objetivo)
# 5.	Definimos nuestra variable respuesta que contendrá nuestra respuesta inicial y recordemos que debemos encontrar la mitad de alto y bajo, esto será (alto + bajo) / 2 
# 6.	Ahora definimos nuestro ciclo while abs(respuesta**2 - objetivo) >= épsilon: Y no ponemos la segunda condición, porque con alto estamos garantizando, que nuestro objetivo, lo mínimo que va poder ser es 1.0 y asi garantizamos que no es un numero negativo
# 7.	dentro de nuestro ciclo generamos el if statement o condición con la siguiente lógica: si respuesta al cuadrado es menor que objetivo: entonces bajo es nuestra nueva respuesta, else, alto es nuestra nueva respuesta. Con eso definimos si nos vamos a bajo nos vamos a alto.
#       Una vez completado el ciclo, la respuesta en cada iteración la volveremos mas pequeña esto lo hacemos con la sintaxis respuesta = (alto + bajo) / 2. Es decir, que en cada iteración estamos dividiendo entre dos nuestro espacio de búsqueda y estamos redefiniendo tanto bajo como alto
# 8.	Por ultimo le pedimos al usuario mediante un string de formato que 
#       print(f’La raíz cuadrada de {objetivo} es {respuesta}’)
# 9.	Para ver que esta sucediendo en la ejecución del algoritmo, agregaremos a nuestro ciclo while un print statement
#       print(f’bajo={bajo}, alto={alto}, respuesta={respuesta}’).


objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
