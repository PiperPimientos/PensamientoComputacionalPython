#Algoritmo de aproximacion

# El algoritmo de aproximación de soluciones sirve para dar una respuesta lo  mas aproximado a la solución posible. Es similar a una enumeración  exhaustiva, pero no necesita una respuesta exacta. Podemos aproximar soluciones con un margen de error que llamaremos epsilon.

# Mientras épsilon esta mas cerca a la solución, es decir, es mas preciso, el PC tendrá que hacer mas ciclos de computo. Si nosotros no queremos aproximarla de manera tan exacta, podemos  ir rápido, pero no podemos tener las dos cosas.
# Básicamente epsilon es un porcentaje de error en este caso el 0.01 que sería el 1% de error que aceptamos para la respuesta, por eso recibimos 1.97 en vez de 2 como raiz cuadrada de 4. Se puede incrementar la precisión de la respuesta disminuyendo el porcentaje de error que como vemos en el video, puede ser de 0.001 lo que quiere decir que solo aceptamos el .1% de error en vez del 1% pero la computadora tardaría mucho mas tiempo en encontrar la respuesta que en este caso seria 1.99 o aproximado.

# Lo que haremos es lo siguiente:

# 1.	Creamos la variable objetivo que contendrá el int en un input que le pedimos al usuario
# 2.	definimos nuestro épsilon que será de 0.01 aunque también podríamos preguntarle al usuario cual quiere que sea su épsilon
# 3.	definimos nuestra variable paso que será de épsilon**2, esto es un valor mucho mas pequeño que épsilon (0.01 * 0.01) 
# 4.	ahora la variable respuesta donde inicializaremos nuestra respuesta y comenzara con el valor de 0.0
# 5.	Haremos el ciclo while y utilizaremos una nueva función que se llama abs y nos devuelve un valor absoluto. Nosotros queremos encontrar la raíz cuadrada, entonces la lógica es que si la respuesta al cuadrado menos el objetivo, se esta acercando a lo que queremos llegar. Entonces conforme el valor absoluto se vaya acercando a nuestro épsilon, es decir a 0.01, significa que cada vez llegaremos mas cerca y mas cerca.
#       Ademas agregaremos un and para decir que la respuesta es menor o igual que el objetivo. Con la finalidad de eliminar numeros negativos.
#       while abs(respuesta**2 - objetivo) >= épsilon and respuesta <= objetivo:
#       Entonces a la respuesta le vamos a aumentar cada vez el paso, respuesta += paso. Esto quiere decir que nuestra respuesta inicia en 0, pero le vamos aumentando 0.001 con cada paso

# 6.	Una vez que ya tenemos definido como dar la respuesta. Nos falta la condicional if para saber si si llegamos a esa respuesta, de esta forma:
#       Notese que también utilizaremos la misma condición, con el valor absoluto. La lógica es: si el valor absoluto de la respuesta al cuadrado menos el objetivo, es mayor o igual a épsilon: entonces no encontramos la respuesta, es decir que nos pasamos, entonces: imprime que no se encontró la raíz cuadrada del objetivo. Else, imprime en cadena de formato que la raíz cuadrada de {objetivo} es {respuesta}
# 7.	Si queremos ver como se procesa la respuesta utilizaremos un print statement en nuestro ciclo while
#       print(abs(respuesta**2 – objetivo), respuesta)
#  8.	Si queremos saber cuanto tiempo se demora, tenemos que importar el modulo time
#       from time import time
#       Y dentro de nuestro ciclo while, al final, incluiremos una variable llamada tiempo_total que guardara como valor time() – tiempo_inicio, tiempo_inicio debemos declararla al principio del programa con el valor de la función time()


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

